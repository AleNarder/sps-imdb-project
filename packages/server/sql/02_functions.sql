-- Create an event trigger function

CREATE OR REPLACE FUNCTION pgrst_watch() RETURNS event_trigger
  LANGUAGE plpgsql
  AS $$
BEGIN
  NOTIFY pgrst, 'reload schema';
END;
$$;

-- This event trigger will fire after every ddl_command_end event
CREATE EVENT TRIGGER pgrst_watch
  ON ddl_command_end
  EXECUTE PROCEDURE pgrst_watch();


create table  if not exists imdb.title_principals (
    tconst text , --should be foreing
    ordering integer,
    nconst text , 
    category text,
    job text, 
    characters text,
    primary key (tconst , ordering)
);

create or replace function imdb.get_basics_count()
returns int
language plpgsql
as
$$
declare
   film_count integer;
begin
   select count(*) 
   into film_count
   from imdb.title_basics;
   
   return film_count;
end;
$$;


-- Give the size of the title_ratings table
create or replace  function imdb.get_ratings_count()
returns int
language plpgsql
as
$$
declare
   film_count integer;
begin
   select count(*) 
   into film_count
   from imdb.title_ratings;
   
   return film_count;
end;
$$;


create or replace  function imdb.get_crew_count()
returns int
language plpgsql
as
$$
declare
   film_count integer;
begin
   select count(*) 
   into film_count
   from imdb.title_crew;
   
   return film_count;
end;
$$;

create or replace  function imdb.get_episode_count()
returns int
language plpgsql
as
$$
declare
   film_count integer;
begin
   select count(*) 
   into film_count
   from imdb.title_episode;
   
   return film_count;
end;
$$;


create or replace  function imdb.get_name_count()
returns int
language plpgsql
as
$$
declare
   film_count integer;
begin
   select count(*) 
   into film_count
   from imdb.name_basics;
   
   return film_count;
end;
$$;


--get info for directors of a specific input title
create or replace function imdb.get_title_directors(tconstvar text)
returns table(tconst text ,nconst text , primaryname text  , 
               birthyear int , deathyear int , 
               primaryprofession text[] , knownfortitles text[])
language plpgsql as $$
begin 
   return query
   select c.tconst, n.*
   from (
        select x.tconst , unnest(x.directors) 
        from imdb.title_crew as x
        ) 
        as c(tconst, nconst)
         left join 
        (
        select y.nconst , y.primaryname, y.birthyear , y.deathyear, y.primaryprofession ,y.knownfortitles
        from imdb.name_basics y
        ) 
        as n(nconst , primaryname , birthyear, deathyear , primaryprofession , knownfortitles) 
      on  n.nconst = c.nconst
      where c.tconst = tconstvar;
end;
$$;


create or replace function imdb.get_title_writers(tconstvar text)
returns table(tconst text ,nconst text , primaryname text  , 
               birthyear int , deathyear int , 
               primaryprofession text[] , knownfortitles text[])
language plpgsql as $$
begin 
   return query
   select c.tconst, n.*
   from (
        select x.tconst , unnest(x.writers) 
        from imdb.title_crew as x
        ) 
        as c(tconst, nconst)
         left join 
        (
        select y.nconst , y.primaryname, y.birthyear , y.deathyear, y.primaryprofession ,y.knownfortitles
        from imdb.name_basics y
        ) 
        as n(nconst , primaryname , birthyear, deathyear , primaryprofession , knownfortitles) 
      on  n.nconst = c.nconst
      where c.tconst = tconstvar;
end;
$$;


create or replace function imdb.get_title_crew(tconstvar text)
returns table(tconst text ,ordering int , nconst text , primaryname text  , 
               birthyear int , deathyear int , 
               primaryprofession text[] , knownfortitles text[] ,
               category text ,  job text , charachers text )
language plpgsql as $$
begin 
   return query
   select p.tconst , p.ordering , n.* , p.category , p.job , p.characters
   from title_principals p 
         left join 
        (
        select y.nconst , y.primaryname, y.birthyear , y.deathyear, y.primaryprofession ,y.knownfortitles
        from imdb.name_basics y
        ) 
        as n(nconst , primaryname , birthyear, deathyear , primaryprofession , knownfortitles) 
      on  n.nconst = p.nconst
      where p.tconst = tconstvar;
end;
$$;

create or replace function imdb.get_title_details_2(tconstvar text)
returns table(tconst text, titletype text ,
               primarytitle text , originaltitle text, isAdult boolean,
               startyear int , endyear int , runtimeMinutes int, genres text,
               averageRating float , numVotes int , prob float)
language plpgsql as $$
begin 
   return query 
   select    x.*,y.averageRating, y.numVotes, y.prob
   from      imdb.title_basics x
   right join imdb.title_ratings y on x.tconst = y.tconst 
   where y.tconst = tconstvar;

end;
$$;

create or replace function imdb.get_title_full(tconstvar text)
returns table(tconst text, titletype text ,
               primarytitle text , originaltitle text, isAdult boolean,
               startyear int , endyear int , runtimeMinutes int, genres text,
               averageRating float , numVotes int , prob float,
               directors jsonb) --crew and writers if you want if you want
language plpgsql as $$
begin 
   return query
   select   b.tconst, b.titletype, b.primarytitle, 
            b.originaltitle, b.isAdult, b.startyear,
            b.endyear, b.runtimeminutes, b.genres,
            r.averageRating, r.numVotes, r.prob , 
            d.directors
   from  imdb.title_basics b
   right join  imdb.title_ratings r on b.tconst = r.tconst 
   left join   (select  c.tconst ,
                        jsonb_agg(n.*) as directors
               from imdb.name_basics n 
               left join   (select  v.tconst, -- getting directors for films with some info
                                    n.nconst , 
                                    n.primaryname
                           from  
                                 (select x.tconst , unnest(x.directors) 
                                 from imdb.title_crew as x) 
                                 as v(tconst, nconst)
                           left join
                                 (select y.nconst , y.primaryname
                                 from imdb.name_basics y) 
                                 as n(nconst , primaryname) 
                           on  n.nconst = v.nconst
                           )as c
               on n.nconst = c.nconst
               group by c.tconst
               )as d
   on d.tconst = r.tconst
   where b.tconst = tconstvar
   group by b.tconst, b.titletype, b.primarytitle, b.originaltitle, b.isAdult, b.startyear, b.endyear, b.runtimeminutes, b.genres,
   r.averageRating, r.numVotes, r.prob ,
   d.directors;
   
end;
$$;

DROP function imdb.get_title_details(text);
create or replace function imdb.get_title_details(tconstvar text)
returns table(tconst text, titletype text ,
               primarytitle text , originaltitle text, isAdult boolean,
               startyear int , endyear int , runtimeMinutes int, genres text,
               averageRating float , numVotes int , prob float,
               directors text[], writers text[]) --crew and writers if you want if you want
language plpgsql as $$
begin 
   return query
   select   b.tconst, b.titletype, b.primarytitle, b.originaltitle, 
            b.isAdult, b.startyear, b.endyear, b.runtimeminutes, b.genres,
            r.averageRating, r.numVotes, r.prob, 
            c.directors , c.writers
   from    imdb.title_basics b
   right join imdb.title_ratings r on b.tconst = r.tconst
   left join imdb.title_crew c on r.tconst = c.tconst
   where b.tconst=tconstvar;            
end;
$$;

--grant execute on function imdb.pgrst_watch() to web_anon;
grant select on imdb.title_principals to web_anon;
grant execute on function "imdb".get_basics_count() to web_anon;
grant execute on function "imdb".get_ratings_count() to web_anon;
grant execute on function "imdb".get_crew_count() to web_anon;
grant execute on function "imdb".get_episode_count() to web_anon;
grant execute on function "imdb".get_name_count() to web_anon;
grant execute on function "imdb".get_title_directors(tconstvar text) to web_anon;
grant execute on function "imdb".get_title_writers(tconstvar text) to web_anon;
grant execute on function "imdb".get_title_crew(tconstvar text) to web_anon;
grant execute on function "imdb".get_title_details(tconstvar text) to web_anon;
grant execute on function "imdb".get_title_full(tconstvar text) to web_anon;
grant execute on function "imdb".get_title_info(tconstvar text) to web_anon;

