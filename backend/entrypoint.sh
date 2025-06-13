#!/bin/bash
set -e

echo "Waiting for PostgreSQL to be available at $DB_HOST:$DB_PORT..."
until pg_isready -h "$DB_HOST" -p "$DB_PORT" > /dev/null 2>&1; do
  sleep 1
done

echo "PostgreSQL is ready!"

poetry run python migrate.py

exec "$@"
