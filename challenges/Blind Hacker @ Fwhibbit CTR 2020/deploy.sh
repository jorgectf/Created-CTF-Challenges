#!/bin/bash

docker-compose -f blind-hacker/docker-compose.yml down
docker-compose -f blind-hacker/docker-compose.yml up -d --build -V

apt install -y mysql-client-core-5.7
apt install -y postgresql

echo "[+] MYSQL: Configuring..."
mysql -h 127.0.0.1 -u root -pstrong-password < blind-hacker/php/sql/mysql.sql 2>/dev/null
while [ $? -ne 0 ]; do
  mysql -h 127.0.0.1 -u root -pstrong-password < blind-hacker/php/sql/mysql.sql 2>/dev/null
done
echo "[+] MYSQL: Configured Succesfully";

echo "[+] POSTGRESQL: Configuring..."
PGPASSWORD=strong-password psql -h 127.0.0.1 blindhackerdb < blind-hacker/php/sql/postgres.sql 2>/dev/null
while [ $? -ne 0 ]; do
  PGPASSWORD=strong-password psql -h 127.0.0.1 blindhackerdb < blind-hacker/php/sql/postgres.sql 2>/dev/null
done
echo "[+] POSTGRESQL: Configured Succesfully";
