FROM postgres:14.2
EXPOSE 5432

COPY scripts/init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh

RUN mkdir /temp
RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime

USER postgres
