from ulsmith/alpine-apache-php7

ADD start.sh /bootstrap/start.sh

ADD html/ /app/public
ADD twicat.sql /app/twicat.sql

RUN apk update && apk add sqlite mysql-client socat
RUN cat /app/twicat.sql | sqlite3 /app/twicat.db

RUN chmod +x /bootstrap/start.sh
RUN chown root:root /app -R

ENTRYPOINT ["/bootstrap/start.sh"]
