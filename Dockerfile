FROM python:3-slim-buster

RUN apt-get update && \
    apt-get -y --no-install-recommends install \
    build-essential python3-dev

RUN adduser --disabled-login --system --no-create-home --gecos 'App User' app

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY --chown=app:root ./shopify_test_project/ /app

USER app
