#!/bin/bash

touch raw/title.ratings.tsv raw/title.basics.tsv
wget -O - https://datasets.imdbws.com/title.ratings.tsv.gz | gzip -d > raw/title.ratings.tsv 
wget -O - https://datasets.imdbws.com/title.basics.tsv.gz | gzip -d > raw/title.basics.tsv
python3 process.py