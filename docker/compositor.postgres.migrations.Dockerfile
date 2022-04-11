FROM python:3.10

WORKDIR /app
RUN pip3 install sqlalchemy && pip3 install alembic && pip3 install psycopg[binary]

COPY ./src/postgres_migrations .

CMD [ "python3", "migrate.py"]
