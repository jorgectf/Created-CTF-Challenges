FROM ulsmith/alpine-apache-php7

ADD start.sh /bootstrap/start.sh

ADD html/ /app/public
ADD ./sql/mysql.sql /app/mysql.sql
ADD ./sql/postgres.sql /app/postgres.sql

RUN chmod +x /bootstrap/start.sh
RUN chown root:root /app -R

ENTRYPOINT ["/bootstrap/start.sh"]
