# SPS-IMDB-PROJECT

This is the repository of the project for the 2022-2023 Software Performance And Scalability course

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

    One (or more) replica(s) are reachable through the **dispatcher** at [http://localhost:3000](http://localhost:3000)

    A postgREST API connected to the **db** service container. Queries get forwared to this container with different policies by means of the **dispatcher**.

- **dispatcher**

    Available on [http://localhost:3000](http://localhost:3000)

    A NGINX dispatcher image connected to one (or more) replica(s) of the **backend** service container. You can send queries via browser or curl.

- **swagger**

    Available on [http://localhost:3001](http://localhost:3001)

    A swagger editor which explain the backend service endpoints through OpenAPI standard

### run:tsung:closed-loop

Perform a closed loop test with **tsung**. This command can be configured using the *variables* declared inside the *taskfile*

### generate:tsung:query-set

Build the query set necessary for closed loop testing. 10_000 random ids are chosen accordingly to their rating probability

## FAQ

**How are postgREST queries structured?**

The official documentation is available at the postgREST [website](https://postgrest.org/en/stable/api.html#)

Some real-world queries you can issue are:

```bash
# Select all fields of the row whose attribute tconst is tt9898930
curl -X "GET" http://localhost:3000/title_basics?tconst=eq.tt9898930

# Delete the row whose attribute tconst is tt9898930
curl -X "DELETE" http://localhost:3000/title_basics?tconst=eq.tt9898930
```
To test the perfomance of the system, two flavours of the same query can be issued:
```bash
# PERFORMANT query whose attribute tconst is tt9898930
curl -X "GET" http://localhost:3000/title_details?tconst=eq.tt9898930

# SLOW query whose attribute tconstvar is tt9898930
curl -X "GET" http://localhost:3000/rpc/get_title_details?tconstvar=tt9898930
```
