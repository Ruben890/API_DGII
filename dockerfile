ARG PYTHON_VERSION=3.10-slim-buster
ARG DEBIAN_FRONTEND=noninteractive
ARG PORT=8000

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code

# Instalar los paquetes de Linux necesarios, ya que son dependencias de algunas bibliotecas de Python
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    cron \
    wkhtmltopdf \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . /code

# Aplicar migraciones de Django y ejecutar el servidor de desarrollo en el inicio del contenedor
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:${PORT}

EXPOSE ${PORT}
