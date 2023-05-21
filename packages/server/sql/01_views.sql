create or replace view  imdb.title_details
as  select  b.tconst, b.titletype, b.primarytitle, b.originaltitle, b.isAdult, b.startyear, b.endyear, b.runtimeminutes, b.genres,
            r.averageRating, r.numVotes, r.prob,
            c.directors , c.writers
    from    imdb.title_basics b
    right join imdb.title_ratings r on b.tconst = r.tconst 
    left join imdb.title_crew c on r.tconst = c.tconst;


grant all privileges on imdb.title_details to web_anon;
