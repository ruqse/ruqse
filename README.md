# Hi, I’m Faruk 👋

[![GitHub followers](https://img.shields.io/github/followers/ruqse?label=Follow&style=social)](https://github.com/ruqse)

I’m a bioinformatician working on microbiomes, multi-omics, and reproducible analysis. My work spans the vaginal virome, bacterial vaginosis, and drug response in parasitic nematodes. On the side, I build tools that make research life a little easier.

## Microbiomes and viromes

### [Vaginal VirBench](https://github.com/ruqse/vaginal_virbench)

A benchmark of virus identification tools on vaginal metagenomes.

- Tests **14 tools** from five methodological approaches on controlled genome fragments, simulated viral spike-ins, real assemblies, and RCA-enriched viromes
- Replicates the tool ranking in an independent **30-sample MiTCH cohort**
- Maps the trade-off between confident viral calls and recovery of harder-to-detect viruses
- Ships the analysis code, derived data, and workflows to reproduce the figures and tables

### [MiTCH: Multi-omics of bacterial vaginosis](https://github.com/ruqse/mitch_manuscript)

How vaginal microbes and metabolites relate to bacterial vaginosis.

- Integrates shotgun metagenomics and targeted metabolomics from **111 women** (29 with BV, 82 controls)
- Builds a *Gardnerella* pangenome from 61 metagenome-assembled genomes and links genomes to metabolites
- Includes analysis code, processed data, figures, and supplementary tables

Co-first-author paper in [*npj Women’s Health* (2026)](https://doi.org/10.1038/s44294-026-00163-6).

### [MetaPhlAn 4 vs VIRGO2 for *Gardnerella*](https://github.com/ruqse/metaphlan4-vs-virgo2-gardnerella)

How two reference databases represent *Gardnerella* diversity.

- Shows that MetaPhlAn 4 merges the four named *Gardnerella* species into composite bins
- Shows that VIRGO2 resolves all four, plus seven *G. vaginalis* sub-clades
- Reproduces in about a minute, and precomputed outputs let you check the tables without downloading anything

## Pipelines and analysis tools

### [PLAGUE](https://github.com/h-mel/plague)

**PLasmid Assembly Genetic Unit Evaluator**: a Nextflow pipeline that recovers and validates plasmids from assembled bacterial genomes.

- Reconstructs and types plasmids with MOB-suite
- Screens for antimicrobial-resistance genes with Abricate
- Validates candidates with circularisation checks and, when reads are supplied, coverage and copy-number estimates

### [StagNF](https://github.com/ruqse/StagNF)

A Nextflow reimplementation of part of the StaG-mwc metagenomics workflow.

- Runs quality control, host removal, and taxonomic profiling, with a MultiQC report
- Ships profiles for UPPMAX, generic SLURM, and SGE clusters

### [Parascaris gene co-expression networks](https://github.com/ruqse/Parascaris-IVM-GeneNetwork)

How *Parascaris univalens* responds to ivermectin.

- Uses RNA-seq of the anterior end and intestine to build gene co-expression networks
- Identifies seven gene modules and 219 core genes associated with the drug response

### [C. elegans RNA-seq pipeline](https://github.com/ruqse/N2IVM)

A Nextflow workflow for RNA-seq of ivermectin-exposed *C. elegans*.

- Runs quality control, rRNA removal, trimming, and Salmon quantification
- Produces transcript abundances ready for differential expression with DESeq2 or edgeR

### [Mapping ivermectin response in C. elegans](https://github.com/ruqse/MLgenePositions)

Visualising the genomics of drug response.

- Draws Manhattan plots of GWA mappings after ivermectin exposure, using AndersenLab data
- Adds a rug plot of genes implicated in ivermectin resistance

## Side projects

### [C. elegans Atlas](https://github.com/ruqse/c-elegans-atlas)

An interactive 3D explorer of *C. elegans* anatomy.

- Search for structures, then inspect, focus on, or isolate them
- Switch between whole-body and neural EM views
- Spread structures apart to see them more clearly

[Explore the atlas →](https://c-elegans-atlas.vercel.app/)

### [PhDplanner](https://phdplanner.com)

Find doctoral courses and plan your PhD defence in one place.

- Search courses across Sweden by topic, university, location, and delivery mode
- See deadlines and links to official course pages
- Work backwards from your defence date to plan milestones

[Browse courses](https://phdplanner.com/courses360) · [Plan a defence](https://phdplanner.com/defence-plan)

## Tools I work with

- **Analysis:** Python · R · Bash
- **Workflows and computing:** Nextflow · SLURM/HPC · Docker · Apptainer/Singularity · Git
- **Web:** Django · CSS

## Get in touch

Always happy to talk microbiomes, reproducible workflows, or research tools.

[LinkedIn](https://www.linkedin.com/in/farukdube)
