# `pasty` Testing

## Results from Completed _P. aeruginosa_ Genomes

On July 22nd, 2024, [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download) was used
to download all available completed genomes for _P. aeruginosa_ available from RefSeq. Each genome
was then analyzed using `pasty` to determine the serogroup.

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
    awk '{split($1,a,"/");split(a[4],b,"."); print "--input "$1" --prefix "b[1]" --outdir results/ --force"}' | \
    xargs -I {} -P 10 -n 1 bash -c '../bin/pasty {}'

head -n 1 results/GCF_905071885.tsv > completed-genomes.tsv
ls results/ | \
    grep -v "details" | \
    grep -v "blastn" | \
    xargs -I {} grep -v "schema_version" results/{} | \
    sort -k1 >> completed-genomes.tsv
```

## Reference Genomes

For `pasty`, [Table S1](https://journals.asm.org/doi/suppl/10.1128/mbio.01396-15/suppl_file/mbo005152473st1.pdf) from
[S. Thrane et. al.](https://doi.org/10.1128/mbio.01396-15) was used to identify the reference genomes for each of the
serogroups. Below is a table of each serogroup and the corresponding reference genome.

| Serogroup | Accession |
|-----------|-----------|
| O1        | [GCF_001420225.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001420225.1/)|
| O2        | [GCF_001420185.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001420185.1/)|
| O3        | [GCF_001420205.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001420205.1/)|
| O4        | [GCF_001420245.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001420245.1/)|
| O5        | [GCF_001420265.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001420265.1/)|
| O6        | [GCF_001444755.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001444755.1/)|
| O7        | [GCF_001444745.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001444745.1/)|
| O9        | [GCF_001444815.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001444815.1/)|
| O10       | [GCF_001444835.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001444835.1/)|
| O11       | [GCF_001444955.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001444955.1/)|
| O12       | [GCF_001444975.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001444975.1/)|
| O13       | [GCF_001444995.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001444995.1/)|
