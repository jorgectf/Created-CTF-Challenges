#!/bin/bash

docker-compose -f walow3b/docker-compose.yml down
docker-compose -f walow3b/docker-compose.yml up --build 
