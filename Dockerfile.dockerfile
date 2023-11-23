# Utiliza una imagen base con Python
FROM python:3.8-slim

# Instala las dependencias necesarias para Tkinter
RUN apt-get update && \
    apt-get install -y \
    python3-tk \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en la imagen
WORKDIR /app

# Copia tu script y los recursos necesarios al contenedor
COPY proyectito_PDI.py .
COPY txtimagen.png .

# Instala las dependencias de Python
RUN pip install openpyxl Pillow

# Comando para ejecutar tu script al iniciar el contenedor
CMD ["python", "proyectito_PDI.py"]