#!/bin/bash

docker-compose -f mike-dungeon/docker-compose.yml down
docker-compose -f mike-dungeon/docker-compose.yml up -d --build -V