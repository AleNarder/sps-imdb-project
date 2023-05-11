#!/bin/bash

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


if [ ! -s raw/title.crew.tsv ]
then
    echo "[setup]: Downloading title crew..."
    wget -O - https://datasets.imdbws.com/title.crew.tsv.gz | gzip -d > raw/title.crew.tsv
else
    echo "[setup]: Title crew already downloaded"
fi

if [ ! -s raw/title.episode.tsv ]
then
    echo "[setup]: Downloading title episode..."
    wget -O - https://datasets.imdbws.com/title.episode.tsv.gz | gzip -d > raw/title.episode.tsv
else
    echo "[setup]: Title episode already downloaded"
fi

#   if [ ! -s raw/title.principals.tsv ]
#   then
#       echo "[setup]: Downloading title principals..."
#       wget -O - https://datasets.imdbws.com/title.principals.tsv.gz | gzip -d > raw/title.principals.tsv
#   else
#       echo "[setup]: Title principals already downloaded"
#   fi

#   if [ ! -s raw/name.basics.tsv ]
#   then
#       echo "[setup]: Downloading name basics..."
#       wget -O - https://datasets.imdbws.com/name.basics.tsv.gz | gzip -d > raw/name.basics.tsv
#   else
#       echo "[setup]: Name basics already downloaded"
#   fi

if [ ! -s processed/title.basics.tsv ]
then
    python3 scripts/p_title_basics.py
else
    echo "[setup]: title.basics.tsv already processed"
fi

if [ ! -s processed/title.ratings.tsv ]
then
    python3 scripts/p_title_ratings.py
else
    echo "[setup]: title.ratings.tsv already processed"
fi

if [ ! -s processed/title.crew.tsv ]
then
    python3 scripts/p_title_crew.py
else
    echo "[setup]: title.crew.tsv already processed"
fi

if [ ! -s processed/title.episode.tsv ]
then
    python3 scripts/p_title_episode.py
else
    echo "[setup]: title.episode.tsv already processed"
fi

#   if [ ! -s processed/title.principals.tsv ]
#   then
#       python3 scripts/p_title_principals.py
#   else
#        echo "[setup]: title.principals.tsv already processed"
#   fi

#   if [ ! -s processed/name.basics.tsv ]
#   then
#       python3 scripts/p_name_basics.py
#   else
#       echo "[setup]: title.name.tsv already processed"
#   fi
