#!/bin/bash

# Exit the script on any error
set -e

# Wait for PostgreSQL service to be ready
while ! nc -z $PG_HOST $PG_PORT; do
  sleep 1
done

# Apply database migrations for all apps
echo "Applying database migrations..."
python manage.py migrate

# Collect static files (if needed)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Django's built-in development server for local environment
echo "Starting Django development server..."
python manage.py runserver 0.0.0.0:8000
