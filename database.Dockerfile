FROM postgres

RUN mkdir /data

COPY data/sanitized /data/

COPY data/migrate.sql /docker-entrypoint-initdb.d/

