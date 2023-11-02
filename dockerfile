# Imagen base de Python
FROM python:3.10

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt
# Apply database migrations
RUN python manage.py migrate
# Exponer el puerto que utiliza tu aplicación de Django (por ejemplo, 8000)
EXPOSE 8000

# Comando para ejecutar tu aplicación de Django
CMD ["python", "manage.py", "runserver"]