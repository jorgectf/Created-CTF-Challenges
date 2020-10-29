#!/bin/bash

docker-compose -f coming-home/docker-compose.yml down
docker-compose -f coming-home/docker-compose.yml up -d --build -V