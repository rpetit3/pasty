# pasty
A tool easily taken advantage of for in silico serogrouping of _Pseudomonas aeruginosa_ isolates

## A Quick Note

_Pseudomonas aeruginosa_ serotyper (PAst) is available as a web-service from
[CGE - PAst](https://cge.cbs.dtu.dk/services/PAst-1.0/). The web-service
works great, but is not the most efficient for 100s of genomes. I also looked into the
original implementation available at [PAst](https://github.com/Sandramses/PAst).
I tried my best to start tweaking it to meet my needs, but unfortunately my Perl skills
have dulled over the years! And it ended up being easier and quicker to just rewrite it in Python.

## Introduction

`pasty` is a tool to identify the serogroup of _Pseudomonas aeruginosa_ isolates. Using an
input assembly (uncompressed or gzip-compressed), the sequences are blasted against a set of O-antigens.
The serogroup is then predicted based on these results. 

The serogroup logic is based on [Table 1](https://journals.asm.org/doi/10.1128/JCM.00349-16#T1)
of the original PAst publication (citation below).

## Installation

`pasty` will be added to Bioconda once the first release is made. But for the time being
the required dependencies can be installed like so:

```{bash}
mamba create -n pasty-dev -c conda-forge -c bioconda rich-click executor 'python>=3.7' blast
mamba activate pasty-dev
git@github.com:rpetit3/pasty.git
cd pasty
bin/pasty --help
```

## Usage

![pasty](https://user-images.githubusercontent.com/5334269/178814734-e8099ddd-6a10-4030-8f30-a70167f17ec1.svg)

```{bash}
 Usage: pasty [OPTIONS]

 A tool easily taken advantage of for in silico serogrouping of Pseudomonas aeruginosa isolates

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────╮
│    --version                  Show the version and exit.                                            │
│ *  --assembly        TEXT     Input assembly in FASTA format (gzip is OK) [required]                │
│    --db              TEXT     Input database in uncompressed FASTA format [default: db/OSAdb.fasta] │
│    --prefix          TEXT     Prefix to use for output files [default: basename of input]           │
│    --outdir          TEXT     Directory to save output files [default: ./]                          |
│    --min_pident      INTEGER  Minimum percent identity to count a hit [default: 95]                 │
│    --min_coverage    INTEGER  Minimum percent coverage to count a hit [default: 95]                 │
│    --help                     Show this message and exit.                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### --assembly

An assembly in FASTA format (compressed with gzip, or uncompressed) to predict the serogroup on.

### --db

A FASTA file with nucleotide sequences of each O-antigen and _WyzB_. In most cases using the
default value will be all that is needed.

### --prefix

The prefix to use for the output files. If a prefix is not given, the basename
of the input assembly will be used.

### --outdir

The directory to save result files. If the directory does not exist is will be created.

### --min_pident

The minimum percent identity for a blast hit to be considered for serogrouping. The is compared
against the `pident` column of the blast output.

### --min_coverage

The minimum coverage of a O-antigen to be considered for serogrouping. This looks at the percent
of the O-antigen that was aligned to. This calculation does include mismatches and gaps,
but those should be expected to be minimal if `--min_pident` is set to the default (95%) or
similar.

## Output Files

| Filename               | Description                                          |
|------------------------|------------------------------------------------------|
| `{PREFIX}.tsv`         | A tab-delimited file with the predicted serogroup    |
| `{PREFIX}.blasn.tsv`   | A tab-delimited file of all blast hits               |
| `{PREFIX}.details.tsv` | A tab-delimited file with details for each serogroup |

### Example `{PREFIX}.tsv`

This file will contain the final predicted serogroup based on highest coverage. Here's what 
to expect the output to look like:

```{bash}
sample  serogroup       coverage        fragments
GCF_003000695       O2      100.00  1
```

| Column Name | Description                                                              |
|-------------|--------------------------------------------------------------------------|
| sample      | Name of the sample processed                                             |
| serogroup   | The predicted serogroup                                                  |
| coverage    | The percent of the O-antigen that was aligned to                         |
| fragments   | The number of blast hits included in the prediction (_fewer the better_) |

### Example `{PREFIX}.blastn.tsv`

The blast results include sequences which won't display very nicely here. But, don't fret,
it is the standard `-outfmt 6`, so tab-delimited and easy to parse.

### Example `{PREFIX}.details.tsv`

This file provides the the coverage and number of fragments for each of the serogroups. This
can be useful for a deeper review, and it should look like the following:

```{bash}
sample  serogroup       coverage        fragments
GCF_003000695       O1      12.52   2
GCF_003000695       O2      100.00  1
GCF_003000695       O3      1.43    1
GCF_003000695       O4      13.86   2
GCF_003000695       O6      14.78   2
GCF_003000695       O7      11.82   2
GCF_003000695       O9      11.42   1
GCF_003000695       O10     12.97   2
GCF_003000695       O11     15.87   2
GCF_003000695       O12     0.00    0
GCF_003000695       O13     16.22   2
GCF_003000695       WzyB    0.00    0
```

| Column Name | Description                                                              |
|-------------|--------------------------------------------------------------------------|
| sample      | Name of the sample processed                                             |
| serogroup   | The predicted serogroup                                                  |
| coverage    | The percent of the O-antigen that was aligned to                         |
| fragments   | The number of blast hits included in the prediction (_fewer the better_) |

## Naming

The original implementation was called _PAst_, and given this is a Python version I originally
went with _PAst-py_. But decided, _"nah, let's go with pasty"_. Hopefully `pasty` will be
your patsy when it comes to serogrouping your _P. aeruginosa_ isolates.

### License Choice

The original PAst did not include a license, so I selected Apache 2.0 as the license to match other CGE tools.

## Citation

If you use this tool please cite the following:

**Serogroup Method**  
_Thrane SW, Taylor VL, Lund O, Lam JS, Jelsbak L [Application of Whole-Genome Sequencing Data for O-Specific Antigen Analysis and In Silico Serotyping of Pseudomonas aeruginosa Isolates.](https://doi.org/10.1128/JCM.00349-16) Journal of Clinical Microbiology, 54(7), 1782–1788. (2016)_  

**pasty**  
_Petit III RA [pasty: A tool easily taken advantage of for in silico serogrouping of Pseudomonas aeruginosa isolates](https://github.com/rpetit3/pasty) (GitHub)_  

**BLAST+**  
_Camacho C, Coulouris G, Avagyan V, Ma N, Papadopoulos J, Bealer K, Madden TL [BLAST+: architecture and applications.](http://dx.doi.org/10.1186/1471-2105-10-421) BMC Bioinformatics 10, 421 (2009)_  
