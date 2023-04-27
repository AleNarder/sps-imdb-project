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
    - 
- ## Backend
    - [x] Create basic postgREST docker image
    - [x] Add postgREST service container to docker compose services


- ## Tests
    - [x] Create a query set. The probability that a film is searched is proportional to the number of rating that it has received
    - [x] Perform a closed-loop test with tsung using the query set
    - [] Improve horizontal scalability (through replication) and vertical scalability (through db tuning and resource enhancement)
    - [] Test the system using JMT to study the expected response time as function of the number of users. Find the optimal number of users

- ## Report
    - [] Write a boring report