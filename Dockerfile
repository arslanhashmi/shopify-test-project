FROM python:3-slim-buster

RUN apt-get update && \
    apt-get -y --no-install-recommends install \
    build-essential python3-dev

RUN adduser --disabled-login --system --no-create-home --gecos 'App User' app

WORKDIR /app

COPY --chown=app:root . /app
RUN pip install -r /app/requirements.txt

USER app
