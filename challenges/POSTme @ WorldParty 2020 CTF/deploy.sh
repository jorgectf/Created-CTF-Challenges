#!/bin/bash

docker-compose -f POSTme/docker-compose.yml down
docker-compose -f POSTme/docker-compose.yml up -d --build -V