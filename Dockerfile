# Usamos la imagen oficial de Python 3.14 versión slim (ligera)
FROM python:3.14-slim

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero el archivo de requerimientos para optimizar el caché de capas
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código fuente al contenedor
COPY . .

# Exponemos el puerto 8000
EXPOSE 8000

# Comando para ejecutar tu API
# Usamos 'api:app' como me indicaste anteriormente
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]