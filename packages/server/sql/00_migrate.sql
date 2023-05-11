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

create table imdb.title_ratings (
    tconst text primary key,
    averageRating float,
    numVotes integer,
    prob float
);

COPY imdb.title_ratings
FROM '/data/title.ratings.tsv'
DELIMITER E'\t'
QUOTE '"'
CSV HEADER;

create table imdb.title_crew (
    tconst text primary key,
    directors text[],
    writers text[]
);

COPY imdb.title_crew
FROM '/data/title.crew.tsv'
DELIMITER E'\t'
QUOTE '"'
CSV HEADER;

create table imdb.title_episode (
    tconst text primary key,
    parenttconst text , 
    seasonnumber integer,
    episodenumber integer
);

COPY imdb.title_episode
FROM '/data/title.episode.tsv'
DELIMITER E'\t'
QUOTE '"'
CSV HEADER;

/* 
create table imdb.title_principals (
    tconst text , --should be foreing
    ordering integer,
    nconst text , 
    category text,
    job text, 
    characters text,
    primary key (tconst , ordering)
);

COPY imdb.title_principals
FROM '/data/title.principals.tsv'
DELIMITER E'\t'
QUOTE '"'
CSV HEADER;
*/

/*
create table imdb.name_basics (
    nconst text primary key,
    primaryName text , 
    birthyear integer,
    deathyear integer,
    primaryprofession text[],
    knownfortitles text[]
);
COPY imdb.name_basics
FROM '/data/name.basics.tsv'
DELIMITER E'\t'
QUOTE '"'
CSV HEADER;
*/

create role web_anon nologin;

grant usage on schema imdb to web_anon;
grant select on imdb.title_basics to web_anon;
grant select on imdb.title_ratings to web_anon;
grant select on imdb.title_crew to web_anon;
grant select on imdb.title_episode to web_anon;
--- grant select on imdb.title_principals to web_anon;
--- grant select on imdb.name_basics to web_anon;


grant web_anon to authenticator;