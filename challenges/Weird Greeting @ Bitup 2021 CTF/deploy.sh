#!/bin/bash

docker-compose -f weird-greeting/docker-compose.yml down
docker-compose -f weird-greeting/docker-compose.yml up -d --build -V