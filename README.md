# Similarity analysis of metagenomes

1. Download data
1. Obtain sketches
1. Obtain similarity (pairwise)

Record the time and memory of these three steps. After these:

1. Compute the plots accordingly


## Download data
The data source is here: https://www.hmpdacc.org/hmp/HMASM/#data. We downloaded the summary file, which is HMASM.csv file.

1. Group by body sites
1. For each body site, get 5 smallest reads
1. Download the data
1. Check md5sum of the downloaded files to make sure download was done correctly.

DONE.

## Preprocess the data

1. For every tar.bz2 file we have to unzip
1. We have to get to the unzipped directory
1. We then have to concatenate the fastq files, and write the final file on which we will do subsequent analysis.

DONE.

## Obtain FracMinHash sketches

