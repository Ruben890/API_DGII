# Utilizamos una imagen base más ligera, como alpine, en lugar de la imagen completa de Python
FROM python:3.10

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt
# Apply database migrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Comando para ejecutar tu aplicación de Django con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
