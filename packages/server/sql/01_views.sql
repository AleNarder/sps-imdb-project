drop view imdb.director2 ;
drop view imdb.title_fullprova;
drop view imdb.title_infoplus2;


create or replace view  imdb.title_info
as  select    x.*,y.averageRating, y.numVotes, y.prob
    from      imdb.title_basics x
    right join imdb.title_ratings y on x.tconst = y.tconst ;

create or replace view imdb.director
as  select c.tconst, n.nconst , n.primaryname
    from 
        (
        select x.tconst , unnest(x.directors) 
        from imdb.title_crew as x
        ) 
        as c(tconst, nconst)
    left join 
        (
        select y.nconst , y.primaryname
        from imdb.name_basics y
        ) 
        as n(nconst , primaryname) 
    on  n.nconst = c.nconst;

/*create or replace view imdb.title_fullprova
as  select i.* , d.directors
    from imdb.title_info i left join
    imdb.director d on i.tconst = d.tconst;*/

create or replace view  imdb.title_infoplus
as  select  b.tconst, b.titletype, b.primarytitle, b.originaltitle, b.isAdult, b.startyear, b.endyear, b.runtimeminutes, b.genres,
            r.averageRating, r.numVotes, r.prob , 
            c.directors , c.writers,
            array_agg(p.nconst) as crew
    from    imdb.title_basics b
    right join imdb.title_ratings r on b.tconst = r.tconst 
    left join imdb.title_crew c on r.tconst = c.tconst
    left join imdb.title_principals p on p.tconst = c.tconst
    group by b.tconst, b.titletype, b.primarytitle, b.originaltitle, b.isAdult, b.startyear, b.endyear, b.runtimeminutes, b.genres,
            r.averageRating, r.numVotes, r.prob , 
            c.directors , c.writers;



create or replace view imdb.director2
as  select c.tconst, n.nconst , n.primaryname
    from 
        (
        select x.tconst , unnest(x.directors) 
        from imdb.title_crew as x
        ) 
        as c(tconst, nconst)
    left join 
        (
        select y.nconst , y.primaryname
        from imdb.name_basics y
        ) 
        as n(nconst , primaryname) 
    on  n.nconst = c.nconst;




create or replace view  imdb.title_infoplus2
as  select  b.tconst, b.titletype, b.primarytitle, b.originaltitle, b.isAdult, b.startyear, b.endyear, b.runtimeminutes, b.genres,
            r.averageRating, r.numVotes, r.prob , 
            d.directors, 
            jsonb_agg(s.*) as crew
    from    imdb.title_basics b
    right join imdb.title_ratings r on b.tconst = r.tconst 
    left join (select c.tconst , jsonb_agg(n.*) as directors
                from imdb.name_basics n 
                left join imdb.director2 c
                on n.nconst = c.nconst
                group by c.tconst
                ) as d
                on d.tconst = r.tconst
    left join (select n.nconst , p.tconst , n.primaryname
               from imdb.name_basics n 
               left join imdb.title_principals p
               on n.nconst = p.nconst 
            ) as s
               on s.tconst = d.tconst
    group by b.tconst, b.titletype, b.primarytitle, b.originaltitle, b.isAdult, b.startyear, b.endyear, b.runtimeminutes, b.genres,
            r.averageRating, r.numVotes, r.prob ,
            d.directors;

grant all privileges on imdb.title_info to web_anon;
grant all privileges on imdb.title_infoplus to web_anon;
grant all privileges on imdb.director to web_anon;
grant all privileges on imdb.title_fullprova to web_anon;
grant all privileges on imdb.director2 to web_anon;
grant all privileges on imdb.title_infoplus2 to web_anon;





