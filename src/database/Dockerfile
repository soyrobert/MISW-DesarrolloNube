FROM postgres:latest

ENV POSTGRES_DB=idlr_db
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
