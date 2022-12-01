# `pasty` Testing

## Results from Completed _P. aeruginosa_ Genomes

On November 30th, 2022, I used [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download),
to download all available completed genomes for _P. aeruginosa_ available from RefSeq. I then ran each
completed genome through `pasty`.

The results are available at [completed-genomes.tsv](https://github.com/rpetit3/pasty/tree/main/test/completed-genomes.tsv)

### Commands Used

```{bash}
mkdir genomes
ncbi-genome-download bacteria \
    --genera "Pseudomonas aeruginosa" \
    --assembly-levels complete \
    --formats fasta \
    --output-folder genomes \
    --parallel 4

mkdir results
find genomes/ -name "*.fna.gz" | \
    awk '{split($1,a,"/");split(a[4],b,"."); print "--assembly "$1" --prefix "b[1]" --outdir results/"}' | \
    xargs -I {} -P 10 -n 1 bash -c 'pasty {}'

head -n 1 results/GCF_905071885.tsv > completed-genomes.tsv
ls results/ | \
    grep -v "details" | \
    grep -v "blastn" | \
    xargs -I {} grep -v "fragments" results/{} | \
    sort -k1 >> completed-genomes.tsv
```

## Serogroups from Completed Genomes
The individual [output files](https://github.com/rpetit3/pasty#output-files) from each execution
are available in the [expected_results folder](https://github.com/rpetit3/pasty/tree/main/test/expected_results/)

### O1

```{bash}
pasty \
    --assembly test/O1-GCF_000504045.fna.gz \
    --prefix O1-GCF_000504045 \
    --outdir expected_results/O1-GCF_000504045/

Running pasty with following parameters:
    --assembly test/O1-GCF_000504045.fna.gz
    --db test/../db/OSAdb.fasta
    --prefix O1-GCF_000504045
    --outdir expected_results/O1-GCF_000504045/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/O1-GCF_000504045/O1-GCF_000504045.blastn.tsv

                   Serogroup Results
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O1-GCF_000504045 │ O1        │ 100.01   │ 1         │
│ O1-GCF_000504045 │ O2        │ 9.85     │ 2         │
│ O1-GCF_000504045 │ O3        │ 11.20    │ 2         │
│ O1-GCF_000504045 │ O4        │ 14.36    │ 2         │
│ O1-GCF_000504045 │ O5        │ 0        │ 0         │
│ O1-GCF_000504045 │ O6        │ 14.07    │ 2         │
│ O1-GCF_000504045 │ O7        │ 11.56    │ 2         │
│ O1-GCF_000504045 │ O9        │ 36.66    │ 1         │
│ O1-GCF_000504045 │ O10       │ 12.52    │ 2         │
│ O1-GCF_000504045 │ O11       │ 15.85    │ 2         │
│ O1-GCF_000504045 │ O12       │ 1.28     │ 1         │
│ O1-GCF_000504045 │ O13       │ 15.39    │ 2         │
│ O1-GCF_000504045 │ WyzB      │ 0        │ 0         │
└──────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/O1-GCF_000504045/O1-GCF_000504045.details.tsv

                       Predicted Serogroup
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ O1-GCF_000504045 │ O1        │ 100.01   │ 1         │         │
└──────────────────┴───────────┴──────────┴───────────┴─────────┘
Predicted serogroup result written to expected_results/O1-GCF_000504045/O1-GCF_000504045.tsv
```

### O2

```{bash}
pasty \
    --assembly test/O2-GCF_000006765.fna.gz \
    --prefix O2-GCF_000006765 \
    --outdir expected_results/O2-GCF_000006765/

Running pasty with following parameters:
    --assembly test/O2-GCF_000006765.fna.gz
    --db test/../db/OSAdb.fasta
    --prefix O2-GCF_000006765
    --outdir expected_results/O2-GCF_000006765/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/O2-GCF_000006765/O2-GCF_000006765.blastn.tsv

                   Serogroup Results
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O2-GCF_000006765 │ O1        │ 12.52    │ 2         │
│ O2-GCF_000006765 │ O2        │ 100.00   │ 1         │
│ O2-GCF_000006765 │ O3        │ 1.43     │ 1         │
│ O2-GCF_000006765 │ O4        │ 13.86    │ 2         │
│ O2-GCF_000006765 │ O5        │ 0        │ 0         │
│ O2-GCF_000006765 │ O6        │ 14.78    │ 2         │
│ O2-GCF_000006765 │ O7        │ 11.82    │ 2         │
│ O2-GCF_000006765 │ O9        │ 11.42    │ 1         │
│ O2-GCF_000006765 │ O10       │ 12.97    │ 2         │
│ O2-GCF_000006765 │ O11       │ 15.87    │ 2         │
│ O2-GCF_000006765 │ O12       │ 0.00     │ 0         │
│ O2-GCF_000006765 │ O13       │ 16.22    │ 2         │
│ O2-GCF_000006765 │ WyzB      │ 0        │ 0         │
└──────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/O2-GCF_000006765/O2-GCF_000006765.details.tsv

                       Predicted Serogroup
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ O2-GCF_000006765 │ O2        │ 100.00   │ 1         │         │
└──────────────────┴───────────┴──────────┴───────────┴─────────┘
Predicted serogroup result written to expected_results/O2-GCF_000006765/O2-GCF_000006765.tsv
```

### O3

```{bash}
pasty \
    --assembly O3-GCF_000271365.fna.gz \
    --prefix O3-GCF_000271365 \
    --outdir expected_results/O3-GCF_000271365/

Running pasty with following parameters:
    --assembly test/O3-GCF_000271365.fna.gz
    --db test/../db/OSAdb.fasta
    --prefix O3-GCF_000271365
    --outdir expected_results/O3-GCF_000271365/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/O3-GCF_000271365/O3-GCF_000271365.blastn.tsv

                   Serogroup Results
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O3-GCF_000271365 │ O1        │ 12.34    │ 2         │
│ O3-GCF_000271365 │ O2        │ 1.24     │ 1         │
│ O3-GCF_000271365 │ O3        │ 100.02   │ 2         │
│ O3-GCF_000271365 │ O4        │ 13.92    │ 2         │
│ O3-GCF_000271365 │ O5        │ 0        │ 0         │
│ O3-GCF_000271365 │ O6        │ 14.73    │ 2         │
│ O3-GCF_000271365 │ O7        │ 10.55    │ 1         │
│ O3-GCF_000271365 │ O9        │ 12.73    │ 2         │
│ O3-GCF_000271365 │ O10       │ 11.35    │ 1         │
│ O3-GCF_000271365 │ O11       │ 15.85    │ 2         │
│ O3-GCF_000271365 │ O12       │ 1.11     │ 1         │
│ O3-GCF_000271365 │ O13       │ 16.57    │ 2         │
│ O3-GCF_000271365 │ WyzB      │ 0        │ 0         │
└──────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/O3-GCF_000271365/O3-GCF_000271365.details.tsv

                       Predicted Serogroup
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ O3-GCF_000271365 │ O3        │ 100.02   │ 2         │         │
└──────────────────┴───────────┴──────────┴───────────┴─────────┘
Predicted serogroup result written to expected_results/O3-GCF_000271365/O3-GCF_000271365.tsv
```

### O4

```{bash}
pasty \
    --assembly O4-GCF_024652945.fna.gz \
    --prefix O4-GCF_024652945 \
    --outdir expected_results/O4-GCF_024652945/

Running pasty with following parameters:
    --assembly test/O4-GCF_024652945.fna.gz
    --db test/../db/OSAdb.fasta
    --prefix O4-GCF_024652945
    --outdir expected_results/O4-GCF_024652945/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/O4-GCF_024652945/O4-GCF_024652945.blastn.tsv

                   Serogroup Results
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O4-GCF_024652945 │ O1        │ 11.94    │ 2         │
│ O4-GCF_024652945 │ O2        │ 9.09     │ 2         │
│ O4-GCF_024652945 │ O3        │ 10.52    │ 2         │
│ O4-GCF_024652945 │ O4        │ 100.00   │ 1         │
│ O4-GCF_024652945 │ O5        │ 0        │ 0         │
│ O4-GCF_024652945 │ O6        │ 14.23    │ 2         │
│ O4-GCF_024652945 │ O7        │ 10.84    │ 2         │
│ O4-GCF_024652945 │ O9        │ 12.72    │ 2         │
│ O4-GCF_024652945 │ O10       │ 12.01    │ 2         │
│ O4-GCF_024652945 │ O11       │ 1.99     │ 1         │
│ O4-GCF_024652945 │ O12       │ 1.07     │ 1         │
│ O4-GCF_024652945 │ O13       │ 15.43    │ 2         │
│ O4-GCF_024652945 │ WyzB      │ 0        │ 0         │
└──────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/O4-GCF_024652945/O4-GCF_024652945.details.tsv

                       Predicted Serogroup
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ O4-GCF_024652945 │ O4        │ 100.00   │ 1         │         │
└──────────────────┴───────────┴──────────┴───────────┴─────────┘
Predicted serogroup result written to expected_results/O4-GCF_024652945/O4-GCF_024652945.tsv
```

### O6

```{bash}
pasty \
    --assembly O6-GCF_001457615.fna.gz \
    --prefix O6-GCF_001457615 \
    --outdir expected_results/O6-GCF_001457615/

Running pasty with following parameters:
    --assembly test/O6-GCF_001457615.fna.gz
    --db test/../db/OSAdb.fasta
    --prefix O6-GCF_001457615
    --outdir expected_results/O6-GCF_001457615/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/O6-GCF_001457615/O6-GCF_001457615.blastn.tsv

                   Serogroup Results
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O6-GCF_001457615 │ O1        │ 11.99    │ 2         │
│ O6-GCF_001457615 │ O2        │ 9.92     │ 2         │
│ O6-GCF_001457615 │ O3        │ 11.41    │ 2         │
│ O6-GCF_001457615 │ O4        │ 14.58    │ 2         │
│ O6-GCF_001457615 │ O5        │ 0        │ 0         │
│ O6-GCF_001457615 │ O6        │ 100.00   │ 1         │
│ O6-GCF_001457615 │ O7        │ 11.75    │ 2         │
│ O6-GCF_001457615 │ O9        │ 12.76    │ 2         │
│ O6-GCF_001457615 │ O10       │ 12.48    │ 2         │
│ O6-GCF_001457615 │ O11       │ 15.94    │ 2         │
│ O6-GCF_001457615 │ O12       │ 1.12     │ 1         │
│ O6-GCF_001457615 │ O13       │ 0.00     │ 0         │
│ O6-GCF_001457615 │ WyzB      │ 0        │ 0         │
└──────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/O6-GCF_001457615/O6-GCF_001457615.details.tsv

                       Predicted Serogroup
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ O6-GCF_001457615 │ O6        │ 100.00   │ 1         │         │
└──────────────────┴───────────┴──────────┴───────────┴─────────┘
Predicted serogroup result written to expected_results/O6-GCF_001457615/O6-GCF_001457615.tsv
```

### O7

```{bash}
pasty \
    --assembly O7-GCF_001482325.fna.gz \
    --prefix O7-GCF_001482325 \
    --outdir expected_results/O7-GCF_001482325/

Running pasty with following parameters:
    --assembly test/O7-GCF_001482325.fna.gz
    --db test/../db/OSAdb.fasta
    --prefix O7-GCF_001482325
    --outdir expected_results/O7-GCF_001482325/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/O7-GCF_001482325/O7-GCF_001482325.blastn.tsv

                   Serogroup Results
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O7-GCF_001482325 │ O1        │ 12.34    │ 2         │
│ O7-GCF_001482325 │ O2        │ 9.96     │ 2         │
│ O7-GCF_001482325 │ O3        │ 10.22    │ 1         │
│ O7-GCF_001482325 │ O4        │ 13.92    │ 2         │
│ O7-GCF_001482325 │ O5        │ 0        │ 0         │
│ O7-GCF_001482325 │ O6        │ 14.73    │ 2         │
│ O7-GCF_001482325 │ O7        │ 100.00   │ 1         │
│ O7-GCF_001482325 │ O9        │ 12.73    │ 2         │
│ O7-GCF_001482325 │ O10       │ 11.35    │ 1         │
│ O7-GCF_001482325 │ O11       │ 15.85    │ 2         │
│ O7-GCF_001482325 │ O12       │ 1.11     │ 1         │
│ O7-GCF_001482325 │ O13       │ 16.21    │ 2         │
│ O7-GCF_001482325 │ WyzB      │ 0        │ 0         │
└──────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/O7-GCF_001482325/O7-GCF_001482325.details.tsv

                       Predicted Serogroup
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ O7-GCF_001482325 │ O7        │ 100.00   │ 1         │         │
└──────────────────┴───────────┴──────────┴───────────┴─────────┘
Predicted serogroup result written to expected_results/O7-GCF_001482325/O7-GCF_001482325.tsv
```

### O9

```{bash}
pasty \
    --assembly O9-GCF_002075065.fna.gz \
    --prefix O9-GCF_002075065 \
    --outdir expected_results/O9-GCF_002075065/

Running pasty with following parameters:
    --assembly test/O9-GCF_002075065.fna.gz
    --db test/../db/OSAdb.fasta
    --prefix O9-GCF_002075065
    --outdir expected_results/O9-GCF_002075065/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/O9-GCF_002075065/O9-GCF_002075065.blastn.tsv

                   Serogroup Results
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O9-GCF_002075065 │ O1        │ 34.47    │ 1         │
│ O9-GCF_002075065 │ O2        │ 8.46     │ 1         │
│ O9-GCF_002075065 │ O3        │ 10.87    │ 2         │
│ O9-GCF_002075065 │ O4        │ 14.37    │ 2         │
│ O9-GCF_002075065 │ O5        │ 0        │ 0         │
│ O9-GCF_002075065 │ O6        │ 14.07    │ 2         │
│ O9-GCF_002075065 │ O7        │ 11.53    │ 2         │
│ O9-GCF_002075065 │ O9        │ 100.00   │ 1         │
│ O9-GCF_002075065 │ O10       │ 12.49    │ 2         │
│ O9-GCF_002075065 │ O11       │ 15.85    │ 2         │
│ O9-GCF_002075065 │ O12       │ 1.29     │ 1         │
│ O9-GCF_002075065 │ O13       │ 15.39    │ 2         │
│ O9-GCF_002075065 │ WyzB      │ 0        │ 0         │
└──────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/O9-GCF_002075065/O9-GCF_002075065.details.tsv

                       Predicted Serogroup
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ O9-GCF_002075065 │ O9        │ 100.00   │ 1         │         │
└──────────────────┴───────────┴──────────┴───────────┴─────────┘
Predicted serogroup result written to expected_results/O9-GCF_002075065/O9-GCF_002075065.tsv
```

### O10

```{bash}
pasty \
    --assembly O10-GCF_009676765.fna.gz \
    --prefix O10-GCF_009676765 \
    --outdir expected_results/O10-GCF_009676765/

Running pasty with following parameters:
    --assembly test/O10-GCF_009676765.fna.gz
    --db test/../db/OSAdb.fasta
    --prefix O10-GCF_009676765
    --outdir expected_results/O10-GCF_009676765/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/O10-GCF_009676765/O10-GCF_009676765.blastn.tsv

                   Serogroup Results
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample            ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O10-GCF_009676765 │ O1        │ 12.02    │ 2         │
│ O10-GCF_009676765 │ O2        │ 9.82     │ 2         │
│ O10-GCF_009676765 │ O3        │ 9.90     │ 1         │
│ O10-GCF_009676765 │ O4        │ 13.86    │ 2         │
│ O10-GCF_009676765 │ O5        │ 0        │ 0         │
│ O10-GCF_009676765 │ O6        │ 14.06    │ 2         │
│ O10-GCF_009676765 │ O7        │ 10.20    │ 1         │
│ O10-GCF_009676765 │ O9        │ 12.76    │ 2         │
│ O10-GCF_009676765 │ O10       │ 100.02   │ 2         │
│ O10-GCF_009676765 │ O11       │ 15.86    │ 2         │
│ O10-GCF_009676765 │ O12       │ 1.11     │ 1         │
│ O10-GCF_009676765 │ O13       │ 15.74    │ 2         │
│ O10-GCF_009676765 │ WyzB      │ 0        │ 0         │
└───────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/O10-GCF_009676765/O10-GCF_009676765.details.tsv

                       Predicted Serogroup
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample            ┃ serogroup ┃ coverage ┃ fragments ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ O10-GCF_009676765 │ O10       │ 100.02   │ 2         │         │
└───────────────────┴───────────┴──────────┴───────────┴─────────┘
Predicted serogroup result written to expected_results/O10-GCF_009676765/O10-GCF_009676765.tsv
```

### O11

```{bash}
pasty \
    --assembly O11-GCF_002192495.fna.gz \
    --prefix O11-GCF_002192495 \
    --outdir expected_results/O11-GCF_002192495/

Running pasty with following parameters:
    --assembly test/O11-GCF_002192495.fna.gz
    --db test/../db/OSAdb.fasta
    --prefix O11-GCF_002192495
    --outdir expected_results/O11-GCF_002192495/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/O11-GCF_002192495/O11-GCF_002192495.blastn.tsv

                   Serogroup Results
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample            ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O11-GCF_002192495 │ O1        │ 11.97    │ 2         │
│ O11-GCF_002192495 │ O2        │ 9.54     │ 2         │
│ O11-GCF_002192495 │ O3        │ 10.85    │ 2         │
│ O11-GCF_002192495 │ O4        │ 1.81     │ 1         │
│ O11-GCF_002192495 │ O5        │ 0        │ 0         │
│ O11-GCF_002192495 │ O6        │ 14.20    │ 2         │
│ O11-GCF_002192495 │ O7        │ 11.20    │ 2         │
│ O11-GCF_002192495 │ O9        │ 12.35    │ 2         │
│ O11-GCF_002192495 │ O10       │ 12.48    │ 2         │
│ O11-GCF_002192495 │ O11       │ 100.00   │ 1         │
│ O11-GCF_002192495 │ O12       │ 1.09     │ 1         │
│ O11-GCF_002192495 │ O13       │ 15.44    │ 2         │
│ O11-GCF_002192495 │ WyzB      │ 0        │ 0         │
└───────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/O11-GCF_002192495/O11-GCF_002192495.details.tsv

                       Predicted Serogroup
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample            ┃ serogroup ┃ coverage ┃ fragments ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ O11-GCF_002192495 │ O11       │ 100.00   │ 1         │         │
└───────────────────┴───────────┴──────────┴───────────┴─────────┘
Predicted serogroup result written to expected_results/O11-GCF_002192495/O11-GCF_002192495.tsv
```

### O12

```{bash}
pasty \
    --assembly O12-GCF_000981825.fna.gz \
    --prefix O12-GCF_000981825 \
    --outdir expected_results/O12-GCF_000981825/

Running pasty with following parameters:
    --assembly test/O12-GCF_000981825.fna.gz
    --db test/../db/OSAdb.fasta
    --prefix O12-GCF_000981825
    --outdir expected_results/O12-GCF_000981825/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/O12-GCF_000981825/O12-GCF_000981825.blastn.tsv

                   Serogroup Results
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample            ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O12-GCF_000981825 │ O1        │ 1.80     │ 1         │
│ O12-GCF_000981825 │ O2        │ 0.00     │ 0         │
│ O12-GCF_000981825 │ O3        │ 1.42     │ 1         │
│ O12-GCF_000981825 │ O4        │ 1.81     │ 1         │
│ O12-GCF_000981825 │ O5        │ 0        │ 0         │
│ O12-GCF_000981825 │ O6        │ 1.85     │ 1         │
│ O12-GCF_000981825 │ O7        │ 1.46     │ 1         │
│ O12-GCF_000981825 │ O9        │ 0.00     │ 0         │
│ O12-GCF_000981825 │ O10       │ 1.62     │ 1         │
│ O12-GCF_000981825 │ O11       │ 2.03     │ 1         │
│ O12-GCF_000981825 │ O12       │ 100.01   │ 1         │
│ O12-GCF_000981825 │ O13       │ 2.02     │ 1         │
│ O12-GCF_000981825 │ WyzB      │ 0        │ 0         │
└───────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/O12-GCF_000981825/O12-GCF_000981825.details.tsv

                       Predicted Serogroup
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample            ┃ serogroup ┃ coverage ┃ fragments ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ O12-GCF_000981825 │ O12       │ 100.01   │ 1         │         │
└───────────────────┴───────────┴──────────┴───────────┴─────────┘
Predicted serogroup result written to expected_results/O12-GCF_000981825/O12-GCF_000981825.tsv
```

## Unknown Serogroup or Poor Data

When a serogroup cannot be determined, you will get a message saying:

  _No match exceeded percent identity and/or coverage thresholds_

Either this is a poorly assembled _P. aeruginosa_, or some other organism. You has the expert,
can choose to adjust the `--min_pident` or the `--min_coverage`, if it makes sense (e.g. coverage
was 92%).

### Completed Genome

```{bash}
pasty \
    --assembly NT-GCF_000292685.fna.gz \
    --prefix NT-GCF_000292685 \
    --outdir expected_results/NT-GCF_000292685/

Running pasty with following parameters:
    --assembly test/NT-GCF_000292685.fna.gz
    --db test/../db/OSAdb.fasta
    --prefix NT-GCF_000292685
    --outdir expected_results/NT-GCF_000292685/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/NT-GCF_000292685/NT-GCF_000292685.blastn.tsv

                   Serogroup Results
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ NT-GCF_000292685 │ O1        │ 0        │ 0         │
│ NT-GCF_000292685 │ O2        │ 0        │ 0         │
│ NT-GCF_000292685 │ O3        │ 0        │ 0         │
│ NT-GCF_000292685 │ O4        │ 0        │ 0         │
│ NT-GCF_000292685 │ O5        │ 0        │ 0         │
│ NT-GCF_000292685 │ O6        │ 0        │ 0         │
│ NT-GCF_000292685 │ O7        │ 0        │ 0         │
│ NT-GCF_000292685 │ O9        │ 0        │ 0         │
│ NT-GCF_000292685 │ O10       │ 0        │ 0         │
│ NT-GCF_000292685 │ O11       │ 0        │ 0         │
│ NT-GCF_000292685 │ O12       │ 0        │ 0         │
│ NT-GCF_000292685 │ O13       │ 0        │ 0         │
│ NT-GCF_000292685 │ WyzB      │ 0        │ 0         │
└──────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/NT-GCF_000292685/NT-GCF_000292685.details.tsv

                                                  Predicted Serogroup
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃ comment                                                       ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ NT-GCF_000292685 │ NT        │ 0        │ 0         │ No match exceeded percent identity and/or coverage thresholds │
└──────────────────┴───────────┴──────────┴───────────┴───────────────────────────────────────────────────────────────┘
Predicted serogroup result written to expected_results/NT-GCF_000292685/NT-GCF_000292685.tsv
```

### Empty FASTA

```{bash}
pasty \
    --assembly empty.fasta \
    --prefix empty \
    --outdir expected_results/empty/

Running pasty with following parameters:
    --assembly test/empty.fasta
    --db test/../db/OSAdb.fasta
    --prefix empty
    --outdir expected_results/empty/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/empty/empty.blastn.tsv

              Serogroup Results
┏━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ empty  │ O1        │ 0        │ 0         │
│ empty  │ O2        │ 0        │ 0         │
│ empty  │ O3        │ 0        │ 0         │
│ empty  │ O4        │ 0        │ 0         │
│ empty  │ O5        │ 0        │ 0         │
│ empty  │ O6        │ 0        │ 0         │
│ empty  │ O7        │ 0        │ 0         │
│ empty  │ O9        │ 0        │ 0         │
│ empty  │ O10       │ 0        │ 0         │
│ empty  │ O11       │ 0        │ 0         │
│ empty  │ O12       │ 0        │ 0         │
│ empty  │ O13       │ 0        │ 0         │
│ empty  │ WyzB      │ 0        │ 0         │
└────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/empty/empty.details.tsv

                                             Predicted Serogroup
┏━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ sample ┃ serogroup ┃ coverage ┃ fragments ┃ comment                                                       ┃
┡━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ empty  │ NT        │ 0        │ 0         │ No match exceeded percent identity and/or coverage thresholds │
└────────┴───────────┴──────────┴───────────┴───────────────────────────────────────────────────────────────┘
Predicted serogroup result written to expected_results/empty/empty.tsv
```

### Improperly Formatted FASTA

```{bash}
pasty \
    --assembly not-a-fasta.fasta \
    --prefix not-a-fasta \
    --outdir expected_results/not-a-fasta/

Running pasty with following parameters:
    --assembly test/not-a-fasta.fasta
    --db test/../db/OSAdb.fasta
    --prefix not-a-fasta
    --outdir expected_results/not-a-fasta/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/not-a-fasta/not-a-fasta.blastn.tsv

                Serogroup Results
┏━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample      ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ not-a-fasta │ O1        │ 0        │ 0         │
│ not-a-fasta │ O2        │ 0        │ 0         │
│ not-a-fasta │ O3        │ 0        │ 0         │
│ not-a-fasta │ O4        │ 0        │ 0         │
│ not-a-fasta │ O5        │ 0        │ 0         │
│ not-a-fasta │ O6        │ 0        │ 0         │
│ not-a-fasta │ O7        │ 0        │ 0         │
│ not-a-fasta │ O9        │ 0        │ 0         │
│ not-a-fasta │ O10       │ 0        │ 0         │
│ not-a-fasta │ O11       │ 0        │ 0         │
│ not-a-fasta │ O12       │ 0        │ 0         │
│ not-a-fasta │ O13       │ 0        │ 0         │
│ not-a-fasta │ WyzB      │ 0        │ 0         │
└─────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/not-a-fasta/not-a-fasta.details.tsv

                                               Predicted Serogroup
┏━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ sample      ┃ serogroup ┃ coverage ┃ fragments ┃ comment                                                       ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ not-a-fasta │ NT        │ 0        │ 0         │ No match exceeded percent identity and/or coverage thresholds │
└─────────────┴───────────┴──────────┴───────────┴───────────────────────────────────────────────────────────────┘
Predicted serogroup result written to expected_results/not-a-fasta/not-a-fasta.ts
```

### Poor Quality Assembly

```{bash}
pasty \
    --assembly poor.fasta \
    --prefix poor \
    --outdir expected_results/poor/

Running pasty with following parameters:
    --assembly test/poor.fasta
    --db test/../db/OSAdb.fasta
    --prefix poor
    --outdir expected_results/poor/
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to expected_results/poor/poor.blastn.tsv

              Serogroup Results
┏━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ poor   │ O1        │ 0        │ 0         │
│ poor   │ O2        │ 0        │ 0         │
│ poor   │ O3        │ 0        │ 0         │
│ poor   │ O4        │ 0        │ 0         │
│ poor   │ O5        │ 0        │ 0         │
│ poor   │ O6        │ 0        │ 0         │
│ poor   │ O7        │ 0        │ 0         │
│ poor   │ O9        │ 0        │ 0         │
│ poor   │ O10       │ 0        │ 0         │
│ poor   │ O11       │ 0        │ 0         │
│ poor   │ O12       │ 0        │ 0         │
│ poor   │ O13       │ 0        │ 0         │
│ poor   │ WyzB      │ 0        │ 0         │
└────────┴───────────┴──────────┴───────────┘
Serogroup Results written to expected_results/poor/poor.details.tsv

                                             Predicted Serogroup
┏━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ sample ┃ serogroup ┃ coverage ┃ fragments ┃ comment                                                       ┃
┡━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ poor   │ NT        │ 0        │ 0         │ No match exceeded percent identity and/or coverage thresholds │
└────────┴───────────┴──────────┴───────────┴───────────────────────────────────────────────────────────────┘
Predicted serogroup result written to expected_results/poor/poor.tsv
```
