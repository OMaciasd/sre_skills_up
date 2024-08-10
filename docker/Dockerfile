# Usa una imagen base oficial de Python
ARG PYTHON_VERSION=3.19
FROM python:alpine${PYTHON_VERSION}

# Configura el directorio de trabajo
WORKDIR /app

# Etiqueta de la imagen
LABEL Name="MiApp" \
      Version="1.0"

# Copia el código fuente de tu aplicación a la imagen
COPY myapp /app/myapp

# Configura variables de entorno para Flask
ENV PYTHONPATH=/app
ENV FLASK_ENV=development
ENV FLASK_APP=myapp.__init__:create_app

# Actualiza pip, instala dependencias y limpia cachés
RUN pip install --upgrade pip \
      && pip install --no-cache-dir --upgrade -r /app/myapp/requirements.txt \
      && apk add --no-cache gcc musl-dev \
      && apk add --no-cache libffi-dev \
      && apk add --no-cache libxml2-dev \
      && apk add --no-cache libxslt-dev \
      && apk add --no-cache postgresql-dev \
      && rm -rf /var/cache/apk/*

# Expone el puerto en el que tu aplicación Flask estará corriendo
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
