# SPS-IMDB-PROJECT

This is the repository of the project for the 2022-2023 SPS course

## Dependencies

In order for this project to work, you need to install the following dependencies

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Taskfile](https://taskfile.dev/installation/)  

## How to run

Commands are defined in the `Taskfile.yml` file. Here you can find a brief explanation of the main commands:
### (default)

Download and process the imdb data through containerized process. The processed files are available for database migrations and query extraction

### run:server

Run three service containers:
- **db**

    Available on [http://localhost:5433](http://localhost:5433)

    A postgres database. You can connect to it using `psql` with _authenticator_ role and _sps_ as password

    ```bash
    psql -h localhost -p 5433 -d imdb -U authenticator 
    ```

  

- **backend**

    Available on [http://localhost:3000](http://localhost:3000)

    A postgREST API connected to the **db** service container. You can send queries via browser or  curl. It's available on []
- **swagger**

    Available on [http://localhost:3000](http://localhost:3001)

    A swagger editor which maps the backend service endpoints

### run:frontend

TODO
## FAQ

**How are postgREST queries structured?**

The ufficial documentation is available on the postgREST [website](https://postgrest.org/en/stable/api.html#)

Some real-world queries you can make:

```bash
# Select all fields of the row whose attribute tconst is tt9898930
curl -X "GET" http://localhost:3000/title_basics?tconst=eq.tt9898930

# Delete the row whose attribute tconst is tt9898930
curl -X "DELETE" http://localhost:3000/title_basics?tconst=eq.tt9898930
```
