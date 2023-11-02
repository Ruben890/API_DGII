# Define los argumentos ARG
ARG PYTHON_VERSION=3.10-slim-buster
ARG DEBIAN_FRONTEND=noninteractive
ARG PORT=8000

# Utiliza una imagen base de Python
FROM python:${PYTHON_VERSION}

# Configura variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crea el directorio de trabajo
WORKDIR /code

# Instala los paquetes de Linux necesarios
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    cron \
    wkhtmltopdf \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Actualiza pip y luego instala las dependencias de Python
RUN set -ex && \
    pip install --upgrade pip

RUN set -ex && \
    pip install -r requirements.txt


# Copia el contenido de la aplicación al directorio de trabajo
COPY . /code

# Ejecuta las migraciones de Django
RUN python manage.py migrate

# Inicia el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
