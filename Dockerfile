# Build stage
FROM node:16 AS build

WORKDIR /app
COPY . .

RUN npm install
RUN npm run build

# Production stage
FROM python:3.11

WORKDIR /app

COPY . .
COPY --from=build /app/frontend/build/ ./frontend/build/

RUN pip install --no-cache-dir -r requirements.txt
RUN opentelemetry-bootstrap -a install

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
# RUN python manage.py djstripe_sync_models

ENV DJANGO_SETTINGS_MODULE=builtwithdjango.settings
ENV OTEL_RESOURCE_ATTRIBUTES=bwd_workers_dev
ENV OTEL_EXPORTER_OTLP_ENDPOINT=https://signoz-otel-collector-proxy.cr.lvtd.dev
ENV OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf

EXPOSE 80

CMD ["opentelemetry-instrument", "uvicorn", "builtwithdjango.asgi:application", "--host", "0.0.0.0", "--port", "80"]
