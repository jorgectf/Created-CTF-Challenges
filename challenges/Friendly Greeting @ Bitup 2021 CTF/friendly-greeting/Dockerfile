FROM ulsmith/alpine-apache-php7

ADD html/ /app/public
ADD start.sh /bootstrap/start.sh

RUN rm /app/public/index.html || true
RUN chmod +x /bootstrap/start.sh
RUN chown root:root /app -R
RUN chmod 700 /var/tmp

ENTRYPOINT ["/bootstrap/start.sh"]