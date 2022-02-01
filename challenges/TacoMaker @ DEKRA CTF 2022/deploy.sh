#!/bin/bash

docker-compose -f tacomaker/docker-compose.yml down
docker-compose -f tacomaker/docker-compose.yml up --build
