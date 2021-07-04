#!/bin/bash

# script to start a docker database for development purposes.

if [ "docker ps -a | grep test_database -q" ]
then
    docker stop test_database
    docker rm test_database
    echo "old server stopped"
fi

docker run --name test_database -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres
export SQLALCHEMY_URI="postgresql://postgres:password@localhost/postgres"