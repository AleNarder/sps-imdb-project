# TODO

- ## Ingestion
    - [x] Download basic title data from imdb
    - [x] Download ratings from imdb
    - [x] Process basic title data for db migration
    - [x] Process ratings in order to add extraction probability
    
- ## Database
    - [x] Create a migration script for basic title data ingestion
    - [x] Create basic Postgres docker image 
    - [x] Add Postgres service container to docker compose services
    - [x] Cleaning up views and functions (just the one required for optimization) <Joe, Enrico>
    - [x] Define a heavy query (with many joins) to use with the query set -> this ensures that a view built with the required joins will speed up the system <Enrico>

- ## Backend
    - [x] Create basic postgREST docker image
    - [x] Add postgREST service container to docker compose services

- ## Dispatcher
    - [x] Set up an **nginx** dispatcher
    - [] Test different dispatching policies

- ## Tests
    - [x] Create a query set. The probability that a film is searched is proportional to the number of rating that it has received
    - [x] Perform a closed-loop test with tsung using the query set
    - [x] Limit resources usage of containers for permance testing
    - [] Improve horizontal scalability (through replication) and vertical scalability (through db tuning and resource enhancement) <*>
    - [] JMT - find the service rates of the systems' components and perform analysis

- ## Report
    - [] Write a boring report (latex)