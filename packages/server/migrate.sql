create schema imdb;

create table imdb.title_basics (
    tconst text primary key,
    titleType text, 
    primaryTitle text,
    originalTitle text,
    isAdult boolean,
    startYear integer,
    endYear integer,
    runtimeMinutes integer,
    genres text
);

COPY imdb.title_basics
FROM '/data/title.basics.tsv'
DELIMITER E'\t'
QUOTE '"'
CSV HEADER;

create role web_anon nologin;

grant usage on schema imdb to web_anon;
grant select on imdb.title_basics to web_anon;

grant web_anon to authenticator;