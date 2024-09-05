# Prueba de lectura y escritura en puertos seriales en MAC

## Configurar el ambiente virtual de Python

En primer lugar, es necesario crear el ambiente virtual, y en segundo, instalar las dependencias:

´´´bash
python3 -m venv venv
source venv/bin/activate
pip3 install pyserial
´´´

## Configuración de puertos seriales

´´´bash
socat -d -d pty,raw,echo=0 pty,raw,echo=0
´´´
