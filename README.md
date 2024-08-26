[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/rpetit3/pasty)

# pasty
A tool easily taken advantage of for in silico serogrouping of _Pseudomonas aeruginosa_ isolates

## A Quick Note

_Pseudomonas aeruginosa_ serotyper (PAst) is available as a web-service from
[CGE - PAst](https://cge.cbs.dtu.dk/services/PAst-1.0/). The web-service
works great, but is not the most efficient for 100s of genomes. I also looked into the
original implementation available at [PAst](https://github.com/Sandramses/PAst).
I tried my best to start tweaking it to meet my needs, but unfortunately my Perl skills
have dulled over the years! And it ended up being easier and quicker to just rewrite it.

## Introduction

`pasty` is built using [camlhmp](https://github.com/rpetit3/camlhmp) to identify the
serogroup of _Pseudomonas aeruginosa_ isolates. Using an input assembly (uncompressed or
gzip-compressed), the sequences are blasted against a set of O-antigens. The serogroup is
then predicted based on these results.

The serogroup logic is based on [Table 1](https://journals.asm.org/doi/10.1128/JCM.00349-16#T1)
of the original PAst publication (citation below).

## Installation

`pasty` Is available from Bioconda

### Conda

```{bash}
mamba create -n pasty -c conda-forge -c bioconda pasty
conda activate pasty
pasty --help
```

## Usage

```{bash}
 Usage: camlhmp-blast-regions [OPTIONS]

 🐪 camlhmp-blast-regions 🐪 - Classify assemblies with a camlhmp schema using BLAST against
 larger genomic regions

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────╮
│ *  --input         -i  TEXT     Input file in FASTA format to classify [required]             │
│ *  --yaml          -y  TEXT     YAML file documenting the targets and types                   │
│                                 [default: bin/../data/pa-osa.yaml]                            │
│                                 [required]                                                    │
│ *  --targets       -t  TEXT     Query targets in FASTA format                                 │
│                                 [default: bin/../data/pa-osa.fasta]                           │
│                                 [required]                                                    │
│    --outdir        -o  PATH     Directory to write output [default: ./]                       │
│    --prefix        -p  TEXT     Prefix to use for output files [default: camlhmp]             │
│    --min-pident        INTEGER  Minimum percent identity to count a hit [default: 90]         │
│    --min-coverage      INTEGER  Minimum percent coverage to count a hit [default: 90]         │
│    --force                      Overwrite existing reports                                    │
│    --verbose                    Increase the verbosity of output                              │
│    --silent                     Only critical errors will be printed                          │
│    --version       -V           Print schema and camlhmp version                              │
│    --help                       Show this message and exit.                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────╯
```

### --input

An assembly in FASTA format (compressed with gzip, or uncompressed) to predict the serogroup on.

### --yaml && --targets

__*Note: These should be automatically set for you!*__

These are the required inputs for `camlhmp` to specify the schema and targets for
serogrouping _P. aeruginosa_.

### --prefix

The prefix to use for the output files. If a prefix is not given, the basename
of the input assembly will be used.

### --outdir

The directory to save result files. If the directory does not exist is will be created.

### --min-pident

__*Note: This should be automatically set for you!*__

The minimum percent identity for a blast hit to be considered for serogrouping. The is compared
against the `pident` column of the blast output.

### --min-coverage

__*Note: This should be automatically set for you!*__

The minimum coverage of a O-antigen to be considered for serogrouping. This looks at the percent
of the O-antigen that was aligned to. This calculation does include mismatches and gaps,
but those should be expected to be minimal if `--min_pident` is set to the default (95%) or
similar.

## Output Files

| Filename               | Description                                          |
|------------------------|------------------------------------------------------|
| `{PREFIX}.tsv`         | A tab-delimited file with the predicted serogroup    |
| `{PREFIX}.blastn.tsv`  | A tab-delimited file of all blast hits               |
| `{PREFIX}.details.tsv` | A tab-delimited file with details for each serogroup |

### Example `{PREFIX}.tsv`

This file will contain the final predicted serogroup based on highest coverage. Here's what
to expect the output to look like:

```{bash}
sample	type	targets	coverage	hits	schema	schema_version	camlhmp_version	params	comment
O1-GCF_001420225	O1	O1	100.00	1	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	
```

| Column Name     | Description                                                              |
|-----------------|--------------------------------------------------------------------------|
| sample          | Name of the sample processed                                             |
| type            | The predicted serogroup                                                  |
| targets         | The targets for the serogroup (_type column_) with a passing hit         |
| coverage        | The percent of the O-antigen that was aligned to                         |
| hits            | The number of blast hits included in the prediction (_fewer the better_) |
| schema          | The schema used for the prediction                                       |
| schema_version  | The version of the schema used for the prediction                        |
| camlhmp_version | The version of camlhmp used for the prediction                           |
| params          | The parameters used for the prediction                                   |
| comment         | Any comments produced during analysis                                    |

### Example `{PREFIX}.blastn.tsv`

The blast results are in standard `-outfmt 6`, and will be similar to this:

```{bash}
qseqid	sseqid	pident	qcovs	qlen	slen	length	nident	mismatch	gapopen	qstart	qend	sstart	send	evalue	bitscore
O1	NZ_LJNU01000023.1	100.000	100	18368	73203	18368	18368	0	0	1	18368	21280	39647	0.0	33920
O2	NZ_LJNU01000023.1	97.823	10	23303	73203	1975	1932	41	2	1	1974	39647	37674	0.0	3408
O2	NZ_LJNU01000023.1	96.296	10	23303	73203	324	312	11	1	22980	23303	21602	21280	2.06e-149	531
O3	NZ_LJNU01000023.1	97.468	11	20210	73203	1975	1925	48	2	1	1974	39647	37674	0.0	3369
O3	NZ_LJNU01000023.1	100.000	11	20210	73203	292	292	0	0	19919	20210	21571	21280	2.96e-152	540
O4	NZ_LJNU01000023.1	96.350	14	15279	73203	1918	1848	70	0	1	1918	39647	37730	0.0	3155
O4	NZ_LJNU01000023.1	99.275	14	15279	73203	276	274	2	0	15004	15279	21555	21280	3.80e-140	499
O6	NZ_LJNU01000023.1	97.809	14	15649	73203	1917	1875	42	0	1	1917	39647	37731	0.0	3308
O6	NZ_LJNU01000023.1	99.649	14	15649	73203	285	284	1	0	15365	15649	21564	21280	8.31e-147	521
O7	NZ_LJNU01000023.1	97.722	12	19617	73203	1975	1930	43	2	17644	19617	37674	39647	0.0	3397
O7	NZ_LJNU01000023.1	100.000	12	19617	73203	292	292	0	0	1	292	21280	21571	2.88e-152	540
O9	NZ_LJNU01000023.1	98.010	39	17263	73203	6332	6206	122	2	1	6331	39647	33319	0.0	10992
O9	NZ_LJNU01000023.1	88.664	39	17263	73203	494	438	39	12	16778	17263	21764	21280	3.20e-166	586
O10	NZ_LJNU01000023.1	98.382	13	17635	73203	1916	1885	31	0	15720	17635	37732	39647	0.0	3367
O10	NZ_LJNU01000023.1	98.973	13	17635	73203	292	289	3	0	1	292	21280	21571	2.60e-147	523
O11	NZ_LJNU01000023.1	96.296	16	13868	73203	1917	1846	71	0	11952	13868	37731	39647	0.0	3147
O11	NZ_LJNU01000023.1	98.932	16	13868	73203	281	278	3	0	1	281	21280	21560	2.67e-141	503
O12	NZ_LJNU01000023.1	90.449	9	25864	73203	1916	1733	183	0	23949	25864	37732	39647	0.0	2525
O12	NZ_LJNU01000023.1	95.455	9	25864	73203	330	315	11	3	1	328	21280	21607	3.82e-147	523
O13	NZ_LJNU01000023.1	97.767	15	14316	73203	1926	1883	43	0	1	1926	39647	37722	0.0	3319
O13	NZ_LJNU01000023.1	99.650	15	14316	73203	286	285	1	0	14031	14316	21565	21280	2.11e-147	523
```

### Example `{PREFIX}.details.tsv`

This file provides the the coverage and number of hits for each of the serogroups. This
can be useful for a deeper review, and it should look like the following:

```{bash}
sample	type	status	targets	missing	coverage	hits	schema	schema_version	camlhmp_version	params	comment
O1-GCF_001420225	O1	True	O1		100.00	1	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	
O1-GCF_001420225	O2	False		O2,wzyB	9.86,0.00	2,0	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	O2:Coverage based on 2 hits
O1-GCF_001420225	O3	False		O3	11.21	2	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	Coverage based on 2 hits
O1-GCF_001420225	O4	False		O4	14.36	2	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	Coverage based on 2 hits
O1-GCF_001420225	O5	False		O2	9.86	2	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	Coverage based on 2 hits
O1-GCF_001420225	O6	False		O6	14.07	2	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	Coverage based on 2 hits
O1-GCF_001420225	O7	False		O7	11.55	2	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	Coverage based on 2 hits
O1-GCF_001420225	O9	False		O9	36.67	1	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	
O1-GCF_001420225	O10	False		O10	12.52	2	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	Coverage based on 2 hits
O1-GCF_001420225	O11	False		O11	15.85	2	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	Coverage based on 2 hits
O1-GCF_001420225	O12	False		O12	1.27	1	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	
O1-GCF_001420225	O13	False		O13	15.45	2	pasty	1.0.0	0.2.1	min-coverage=95;min-pident=95	Coverage based on 2 hits

```

| Column Name     | Description                                                              |
|-----------------|--------------------------------------------------------------------------|
| sample          | Name of the sample processed                                             |
| type            | The predicted serogroup                                                  |
| targets         | The targets for the serogroup (_type column_) __with__ a passing hit     |
| missing         | The targets for the serogroup (_type column_) __without__ a passing hit  |
| coverage        | The percent of the O-antigen that was aligned to                         |
| hits            | The number of blast hits included in the prediction (_fewer the better_) |
| schema          | The schema used for the prediction                                       |
| schema_version  | The version of the schema used for the prediction                        |
| camlhmp_version | The version of camlhmp used for the prediction                           |
| params          | The parameters used for the prediction                                   |
| comment         | Any comments produced during analysis                                    |

## Naming

The original implementation was called _PAst_, and given this is a Python version I originally
went with _PAst-py_. But decided, _"nah, let's go with pasty"_. Hopefully `pasty` will be
your patsy when it comes to serogrouping your _P. aeruginosa_ isolates.

### License Choice

The original PAst did not include a license, so I selected Apache 2.0 as the license to match other CGE tools.

## Citation

If you use this tool please cite the following:

__Serogroup Method__  
_Thrane SW, Taylor VL, Lund O, Lam JS, Jelsbak L [Application of Whole-Genome Sequencing Data for O-Specific Antigen Analysis and In Silico Serotyping of Pseudomonas aeruginosa Isolates.](https://doi.org/10.1128/JCM.00349-16) Journal of Clinical Microbiology, 54(7), 1782–1788. (2016)_  

__pasty__  
_Petit III RA [pasty: A tool easily taken advantage of for in silico serogrouping of Pseudomonas aeruginosa isolates](https://github.com/rpetit3/pasty) (GitHub)_  

__camlhmp__  
_Petit III RA [camlhmp: Classification through yAML Heuristic Mapping Protocol](https://github.com/rpetit3/camlhmp) (GitHub)_  

__BLAST+__  
_Camacho C, Coulouris G, Avagyan V, Ma N, Papadopoulos J, Bealer K, Madden TL [BLAST+: architecture and applications.](http://dx.doi.org/10.1186/1471-2105-10-421) BMC Bioinformatics 10, 421 (2009)_  
