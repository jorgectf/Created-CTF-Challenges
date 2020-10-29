#!/bin/bash

apt update && apt install mysql-client -y

docker-compose -f twicat/docker-compose.yml down
docker-compose -f twicat/docker-compose.yml up -d --build -V

IP=$(docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' twicat_mysql_1)
echo "Creating database..."
mysql -u root -pstrong-password -h $IP < twicat/mysql.sql 2>/dev/null
while [ $? -ne 0 ]; do
  mysql -u root -pstrong-password -h $IP < twicat/mysql.sql 2>/dev/null
done