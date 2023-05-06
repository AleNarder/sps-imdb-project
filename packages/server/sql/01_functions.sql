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



create function imdb.get_basics_count()
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
create  function imdb.get_ratings_count()
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


create  function imdb.get_crew_count()
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




--grant execute on function imdb.pgrst_watch() to web_anon;
grant execute on function "imdb".get_basics_count() to web_anon;
grant execute on function "imdb".get_ratings_count() to web_anon;
grant execute on function "imdb".get_crew_count() to web_anon;
