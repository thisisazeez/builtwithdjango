#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate
# python manage.py djstripe_sync_models

python manage.py qcluster &

export DJANGO_SETTINGS_MODULE=builtwithdjango.settings
export OTEL_SERVICE_NAME=builtwithdjango
export OTEL_EXPORTER_OTLP_ENDPOINT=http://138.201.126.181:25418

opentelemetry-instrument \
  --traces_exporter otlp_proto_http \
  --metrics_exporter otlp_proto_http \
  gunicorn \
    -c deployment/gunicorn.config.py \
    --bind 0.0.0.0:80 \
    --workers 3 \
    --threads 2 \
    --reload \
    builtwithdjango.wsgi:application
