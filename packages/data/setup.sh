#!/bin/bash

touch raw/title.ratings.tsv raw/title.basics.tsv

if [ ! -s raw/title.ratings.tsv ]
then
    wget -O - https://datasets.imdbws.com/title.ratings.tsv.gz | gzip -d > raw/title.ratings.tsv
    echo "[setup]: Downloading title ratings..."
else
    echo "[setup]: Title ratings already downloaded"
fi


if [ ! -s raw/title.basics.tsv ]
then
    echo "[setup]: Downloading title basics..."
    wget -O - https://datasets.imdbws.com/title.basics.tsv.gz | gzip -d > raw/title.basics.tsv
else
    echo "[setup]: Title basics already downloaded"
fi


if [ ! -s processed/title.ratings.tsv ]
then
    python3 process.py
else
    echo "[setup]: data already processed"
fi