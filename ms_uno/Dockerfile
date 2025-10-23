# Imagen base (elige la versión de Python que necesites)
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos antes (para aprovechar la caché de Docker)
COPY requirements.txt .
#Comando  Archivo y el donde se va a copiar el "." es la raiz del proyecto

# Copia el archivo main.py
COPY main.py .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY app/ .

# Documenta que la app corre en el puerto 8000
#EXPOSE 8000   Este es o
# Comando de inicio del contenedor
CMD ["python", "main.py"]
