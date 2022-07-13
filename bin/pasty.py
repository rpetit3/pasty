#!/usr/bin/env python3
"""
Thrane, S. W., Taylor, V. L., Lund, O., Lam, J. S., & Jelsbak, L. (2016).
Application of Whole-Genome Sequencing Data for O-Specific Antigen Analysis and In Silico 
Serotyping of Pseudomonas aeruginosa Isolates. Journal of Clinical Microbiology, 54(7), 1782–1788. 
https://doi.org/10.1128/JCM.00349-16
"""
import sys
from pathlib import Path
import rich_click as click

DB_FASTA = str(Path( __file__ ).parent.absolute()).replace("bin", "db/OSAdb.fasta")
VERSION = '0.0.1'
BLASTN_COLS = [
    "qseqid", "sseqid", "pident", "qlen", "slen", "length", "nident", "mismatch", "gapopen",
    "qstart", "qend", "sstart", "send", "evalue", "bitscore", "qseq", "sseq"
]

SEROGROUP = {
    "O1": ["O1"],
    "O2": ["O2","O16","wzyb"],
    "O3": ["O3","O15"],
    "O4": ["O4"],
    "O5": ["O5","O18","O20"], # O2 - wyzb
    "O6": ["O6"],
    "O7": ["O7","O8"],
    "O9": ["O9"],
    "O10": ["O10","O19"],
    "O11": ["O11","O17"],
    "O12": ["O12"],
    "O13": ["O13","O14"]
}

def check_file_exists(filename: str) -> str:
    """
    Check if file exists and return the absolute path of file, otherwise raise an error.

    Args:
        `filename`: Name of file to check.

    Returns:
        Absolute path of file.
    """
    if not Path(filename).exists():
        raise click.BadParameter(f'{filename} does not exist')
    return str(Path(filename).absolute())


def run_blastn(query: str, db: str, min_pident: float) -> dict:
    """
    Run BLASTN and save the output to a file.

    Args:
        `query`: Path to query file.
        `db`: Path to database file.
        `min_pident`: Minimum percent identity.

    Returns:
        Dictionary of BLASTN output.
    """
    from executor import ExternalCommand, ExternalCommandFailed

    outfmt = ' '.join(BLASTN_COLS)
    cat_type = 'zcat' if query.endswith('.gz') else 'cat'
    try:
        command = ExternalCommand(
            f"{cat_type} {query} | blastn -query - -subject {db} -outfmt '6 {outfmt}'",
            capture=True, 
            capture_stderr=True
        )
        command.start()

        # Convert results to list of dictionaries
        results = {}
        raw_results = []
        for line in str(command.decoded_stdout).split("\n"):
            if line:
                raw_results.append(line)
                result = dict(zip(BLASTN_COLS, line.split('\t')))

                if result['sseqid'] not in results:
                    results[result['sseqid']] = {'hits': [], 'slen': result['slen'], 'length': 0}

                if float(result['pident']) >= min_pident:
                    # Add hit to list of hits
                    results[result['sseqid']]['hits'].append(result)
                    # Add length of hit to total length (includes gaps and mismatches)
                    results[result['sseqid']]['length'] += int(result['length'])

        return [results, raw_results, command.decoded_stderr]
    except ExternalCommandFailed as e:
        print(e, file=sys.stderr)
        sys.exit(e.returncode)


def predict_serogroup(hits: dict, min_coverage: float) -> dict:
    """
    Determine serotype from BLASTN hits.

    Args:
        `hits`: Dictionary of BLASTN hits.

    Returns:
        Dictionary of serotype results.
    """

    # Check is WzyB is present
    serogroups = {'WzyB': {'cov': 0, 'hits': 0}}
    wzyb = False
    if 'WzyB' in hits:
        wyzb_cov = 100 - (100 * (int(hits['WzyB']['slen']) - int(hits['WzyB']['length'])) / float(hits['WzyB']['slen']))
        wzyb = True if wyzb_cov >= min_coverage else False
        serogroups['WzyB'] = {'cov': f"{wyzb_cov:.2f}", 'hits': len(hits['WzyB']['hits'])}


    highest_coverage = 0
    predicted_antigen = None
    for antigen, hit in hits.items():
        if antigen == 'WzyB':
            continue

        # Check if antigen is present
        cov = 100 - (100 * (int(hit['slen']) - int(hit['length'])) / float(hit['slen']))
        serogroups[antigen] = {'cov': f"{cov:.2f}", 'hits': len(hit['hits'])}
        if cov >= min_coverage:
            if cov > highest_coverage:
                highest_coverage = cov
                predicted_antigen = antigen

    # Predict serotype
    predicted_serogroup = {'serogroup': 'NT', 'cov': highest_coverage, 'fragments': 0}
    if predicted_antigen:
        if predicted_antigen == 'O2' and wzyb:
            predicted_serogroup['serogroup'] = 'O2'
        elif predicted_antigen == 'O2':
            predicted_serogroup['serogroup'] = 'O2'
        else:
            predicted_serogroup['serogroup'] = predicted_antigen
        predicted_serogroup['cov'] = serogroups[predicted_antigen]['cov']
        predicted_serogroup['fragments'] = len(hits[predicted_antigen]['hits'])

    # If multiple hits, return the one with the longest length
    return [serogroups, predicted_serogroup]





@click.command()
@click.version_option(VERSION)
@click.option('--assembly', required=True, help='Input assembly in FASTA format (gzip is OK)')
@click.option('--db', default=DB_FASTA, show_default=True, help='Input database in uncompressed FASTA format')
@click.option('--prefix', default="basename of input", show_default=True, help='Prefix to use for output files')
@click.option('--min_pident', default=95, show_default=True, help='Minimum percent identity to count a hit')
@click.option('--min_coverage', default=95, show_default=True, help='Minimum percent coverage to count a hit')
def pasty(assembly, db, prefix, min_pident, min_coverage):
    """In-silico serotyping of Pseudomonas aeruginosa isolates"""
    assembly = check_file_exists(assembly)
    db = check_file_exists(db)
    prefix = str(Path(assembly).stem) if prefix == "basename of input" else prefix

    print("Running BLASTN", file=sys.stderr)
    blastn_parsed, blastn_stdout, blastn_stderr = run_blastn(assembly, db, min_pident)
    serogroups, predicted_serogroup = predict_serogroup(blastn_parsed, min_coverage)

    # Write outputs
    print(f"Writing outputs", file=sys.stderr)
    print(f"BLASTN results written to {prefix}.blastn.tsv", file=sys.stderr)
    with open(f"{prefix}.blastn.tsv", 'wt') as fh_out:
        fh_out.write("\t".join(BLASTN_COLS) + "\n")
        for result in blastn_stdout:
            fh_out.write(f"{result}\n")
    
    # Serogroup Results
    print(f"\nSerogroup results written to {prefix}.details.tsv", file=sys.stderr)
    with open(f"{prefix}.details.tsv", 'wt') as fh_out:
        print(f"serogroup\tcoverage\tfragments", file=sys.stderr)
        fh_out.write("serogroup\tcoverage\tfragments\n")
        for serogroup, detail in serogroups.items():
            print(f"{serogroup}\t{detail['cov']}\t{detail['hits']}", file=sys.stderr)
            fh_out.write(f"{serogroup}\t{detail['cov']}\t{detail['hits']}\n")

    # Predicted Serogroup
    print(f"\nPredicted serogroup results written to {prefix}.tsv", file=sys.stderr)
    with open(f"{prefix}.tsv", 'wt') as fh_out:
        print(f"sample\tserogroup\tcoverage\tfragments", file=sys.stderr)
        print(f"{prefix}\t{predicted_serogroup['serogroup']}\t{predicted_serogroup['cov']}\t{predicted_serogroup['fragments']}", file=sys.stderr)
        fh_out.write("sample\tserogroup\tcoverage\tfragments\n")
        fh_out.write(f"{prefix}\t{predicted_serogroup['serogroup']}\t{predicted_serogroup['cov']}\t{predicted_serogroup['fragments']}\n")


if __name__ == '__main__':
    pasty()
