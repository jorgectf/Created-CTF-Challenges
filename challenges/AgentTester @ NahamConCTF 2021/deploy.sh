#!/bin/bash

docker-compose -f AgentTester/docker-compose.yml down
docker-compose -f AgentTester/docker-compose.yml up --build
