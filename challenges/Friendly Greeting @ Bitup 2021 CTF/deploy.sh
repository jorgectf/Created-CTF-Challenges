#!/bin/bash

docker-compose -f friendly-greeting/docker-compose.yml down
docker-compose -f friendly-greeting/docker-compose.yml up -d --build -V