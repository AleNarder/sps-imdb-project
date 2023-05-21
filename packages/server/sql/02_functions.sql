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

-- Get Film's info by ID
create or replace function imdb.get_title_details(tconstvar text)
returns table(tconst text, titletype text ,
               primarytitle text, originaltitle text, isAdult boolean,
               startyear int, endyear int, runtimeMinutes int, genres text,
               averageRating float, numVotes int, prob float,
               directors text[], writers text[]) --crew and writers if you want
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
grant execute on function "imdb".get_title_details(tconstvar text) to web_anon;
