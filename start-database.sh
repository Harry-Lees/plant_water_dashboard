#!/bin/bash

# script to start a docker database for development purposes.

if [ "docker ps -a | grep test_database -q" ]
then
    docker stop test_database
    docker rm test_database
    echo "old server stopped"
fi

docker build . -f Dockerfile -t test_database
docker run -l test_database -p 5432:5432 -d test_database