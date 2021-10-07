import io
import os
import pandas as pd


def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str},
        sep='\t'
    ).rename(columns={'#CHROM': 'CHROM'})

    path_to_file="C:\Users\floor\Documents\Geneeskunde\NEURO\VCF\GC027886.male.gcap_20_06.HaplotypeCaller.PL.cs1.PL30.vcf"

    dataframe = read_vcf(path=path_to_file

    print(dataframe)