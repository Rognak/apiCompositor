#!/bin/bash

set -e

readonly REQUIRED_ENV_VARS=(
  "POSTGRES_DB_NAME"
  "POSTGRES_DB_USER"
  "POSTGRES_DB_PASSWORD")

main() {
  check_env_vars_set
  init_users_and_db
}

check_env_vars_set() {
  for required_env_var in ${REQUIRED_ENV_VARS[@]}; do
    if [[ -z "${!required_env_var}" ]]; then
      echo "Error:
    Environment variable '$required_env_var' not set.
    Make sure you have the following environment variables set:
      ${REQUIRED_ENV_VARS[@]}
Aborting."
      exit 1
    fi
  done
}

init_users_and_db() {
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
create role $POSTGRES_DB_USER with login password '$POSTGRES_DB_PASSWORD' superuser;

CREATE DATABASE $POSTGRES_DB_NAME
  WITH OWNER = $POSTGRES_DB_USER
       ENCODING = 'UTF8'
       LC_COLLATE = 'en_US.utf8'
       LC_CTYPE = 'en_US.utf8'
       connection limit = -1;

alter database $POSTGRES_DB_NAME set time zone 'Europe/Moscow';

grant all on database $POSTGRES_DB_NAME to $POSTGRES_DB_NAME;
revoke all on database $POSTGRES_DB_NAME from public;
revoke create on schema public from public;

EOSQL


{ echo "host compositor compositor 0.0.0.0/0 trust"; } >> "$PGDATA/pg_hba.conf"
}

main "$@"