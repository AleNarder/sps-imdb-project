create or replace view  imdb.title_info
as  select    x.*,y.averageRating, y.numVotes, y.prob
    from      imdb.title_basics x
    right join imdb.title_ratings y on x.tconst = y.tconst ;

grant all privileges on imdb.title_info to web_anon;