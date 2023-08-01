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
    - [x] Improve horizontal scalability (through replication) and vertical scalability (through db tuning and resource enhancement) <*>
    - [] JMT - find the service rates of the systems' components and perform analysis

- ## Report
    - Write a boring report (latex)
        - Introduction:
            - [] aim of the report; (Enrico)
            - [] environment setup (brief explanation) (Enrico)

        - System Architecture:
            - [x] structure of the SUT; (Alessio)

        - Closed Loop Testing:
            - [x] define how the query set is created; (Alessio)
            - [] Closed Loop introduction (G.I. Joe)
            - for each test in (128mb, 1gb, 3be, 3be_33conn): (Alessio, Enrico, G.I. Joe)
                - [] test scalability of the system;
                - [] (Scalability of the system) State which is the number of users it can handle, through graphs and mathematical analysis... 
                - [] identify the bottleneck
                - [] draw some conclusions on the test
                - [] increase the performance of the bottleneck component and start over
            - identify the problem of the "repetitive service" policy and report the results of the tests (1BE with 1, 10, 450 users/connections) (Enrico / Alessio / G.I. Joe)
            - [x] re-do the tests (?) -> (Test 1BE 3 core DB) (at this point the Database should always be the bottleneck (?)) or just make a consideration on the new bottleneck, state that the new tests confirm the previous "single user" response time analysis 

        - JMT testing: (G.I. Joe)
            - for each test needed:
                - [] identify the bottleneck
                - [] state the number of users...is the number increased w.r.t. previous tests?
                - [] ...

        - Conclusion:
            - [] state the results of analysis and comment on the findings (Alessio / Enrico / G.I. Joe)
            - [x] add section of "future works" (Scheduling policies -> Alessio)