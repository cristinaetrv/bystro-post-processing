#!/bin/sh
# reference: hg38 
# PLINK v1.90b3.32 64-bit (24 Feb 2016)      https://www.cog-genomics.org/plink2

#All references to Rnd 2 indicate the second batch of sequenced individuals merged with the original group
cd Desktop/FXPOIwgsAnalysis/
mkdir -p raw_plink_files
mkdir -p binary_files
mkdir -p merged_files
mkdir -p snpcleaning
mkdir -p gwas
mkdir -p rare
mkdir -p skat
mkdir -p data_formatting_scripts
mkdir -p PCA
mkdir -p HapmapAncr
mkdir -p vcf

cd Desktop/FXPOIwgsAnalysis/
RawPath="$PWD"/raw_plink_files
BinPath="$PWD"/binary_files
MerPath="$PWD"/merged_files
SnpPath="$PWD"/snpcleaning
GwasPath="$PWD"/gwas
RarePath="$PWD"/rare
skatpath="$PWD"/skat
daPath="$PWD"/data_formatting_scripts
PcaPath="$PWD"/PCA
export PATH=$PATH:/Applications/GenomicsTools
#add plink and other tools into genomics tools folder and run this before starting

mkdir -p $RawPath/original_multialleles

