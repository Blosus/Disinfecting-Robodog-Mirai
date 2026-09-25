# ------------ Imagen Base ------------
# version slim para evitar bajar imagenes de mas
FROM python:3.10-slim 

# ------------ Dependencias del Sistema ------------
# "apt-get update" refresca el indice de paquetes disponibles) y "apt-get install" instala los paquetes, la flag -y indica siempre SI a la instalacion de paquetes.
# La flag --no-install-recommends evita instalar paquetes adicionales que no son necesarios para el funcionamiento del contenedor.
# "build-essential" es un paquete que contiene herramientas de compilación necesarias para compilar software desde el código fuente.
# "cmake" es una herramienta de construcción de software que se utiliza para controlar el proceso de compilación.
# "git" es un sistema de control de versiones que permite clonar repositorios de código fuente.
# "iproute2" es un conjunto de utilidades para la gestión de redes en Linux.
# "libgl1" es una biblioteca de OpenGL que proporciona funciones gráficas para aplicaciones que requieren renderizado 3D.
# "libglib2.0-0" es una biblioteca de utilidades que proporciona funciones básicas para el desarrollo de aplicaciones en C.
# "rm -rf /var/lib/apt/lists/*" elimina los archivos temporales de la lista de paquetes descargados para reducir el tamaño de la imagen final del contenedor.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    iproute2 \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# ------------ Compilar CycloneDDS ------------
RUN git clone --branch releases/0.10.x https://github.com/eclipse-cyclonedds/cyclonedds.git /opt/cyclonedds \
    && mkdir /opt/cyclonedds/build \
    && cd /opt/cyclonedds/build \
    && cmake -DCMAKE_INSTALL_PREFIX=/opt/cyclonedds/install .. \
    && cmake --build . --target install

# ----------- Variables de entorno ------------
# Le dice a cualquier programa dentro del contenedor donde estan los binarios de Cyclone DDS, para que pueda encontrarlos y ejecutarlos correctamente.
ENV CYCLONEDDS_HOME=/opt/cyclonedds/install


# ------------ Directorio de Trabajo ------------
# Basicamente define nuestra carpeta actual como /app para todas las siguientes instrucciones.
WORKDIR /app

# ------------ SDK Vendored -------------
COPY setup.py .
COPY README.md .
COPY unitree_sdk2py/ ./unitree_sdk2py/
RUN pip install --no-cache-dir -e .

# ----------- Dependencias de la app web -----------
# Le dice a pip que instale TODOS los paquetes listados en el archivo requirements.txt, que se encuentra en la carpeta Iinu-Robot.
COPY Inu-Robot/requirements.txt ./Inu-Robot/requirements.txt
RUN pip install --no-cache-dir -r ./Inu-Robot/requirements.txt

# ----------- Paquete psutil -----------
RUN pip install --no-cache-dir psutil

# ----------- Copiar la app web -----------
COPY . .
WORKDIR /app/Inu-Robot
EXPOSE 8066
CMD ["python", "app.py"]