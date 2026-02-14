Plataforma de Comercio Electrónico con EC2 y S3

Descripción del proyecto

Esta aplicación es una plataforma básica para pequeños negocios que desean publicar productos en línea. Permite registrar productos mediante un formulario web donde se capturan datos como nombre, precio, cantidad en inventario, descripción e imagen del producto.

La aplicación está desplegada en la nube utilizando Amazon EC2 para el procesamiento y Amazon S3 para el almacenamiento de imágenes.

Funcionamiento

El usuario accede desde un navegador a la IP pública de la instancia EC2.

Llena el formulario con la información del producto.

El formulario envía los datos al servidor mediante una solicitud POST.

El backend desarrollado en Python con Flask procesa la información.

La imagen se sube a un bucket de Amazon S3 utilizando boto3.

El servidor responde confirmando que el producto fue guardado correctamente.

Tecnologías utilizadas

Frontend:

HTML

CSS

JavaScript

Backend:

Python

Flask

boto3

Servicios en la nube:

Amazon EC2

Amazon S3

Estructura del proyecto

code/
backend/
app.py
requirements.txt
frontend/
index.html
style.css
script.js

Instalación y ejecución en EC2

Conectarse por SSH a la instancia.

Entrar a la carpeta backend.

Crear entorno virtual con:
python3 -m venv venv

Activar entorno:
source venv/bin/activate

Instalar dependencias:
pip install -r requirements.txt

Ejecutar servidor:
python app.py

Abrir en navegador:
http://IP_PUBLICA:8080

Requisitos en AWS

Instancia EC2 activa.

Puerto 8080 habilitado en el Security Group.

Bucket S3 creado.

Credenciales configuradas en ~/.aws/credentials.

