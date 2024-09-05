#!/bin/env python

from argparse import ArgumentParser

import enum
import os
import random
import serial
import time


class AppType(enum.Enum):
    SENDER = 1
    READER = 2


def recive(port):
    if port.in_waiting > 0:
        message = port.readline().decode().strip()
        print(f'Mensaje recibido: "{message}"')


def send(port, message):
    port.write(message.encode())
    print(f'Mensaje enviado: {message.strip()}')


def main(file: str, type: AppType):
    try:
        print(f'Abriendo "{file}"')
        port = serial.Serial(args.file, 9600, timeout=1)

        time.sleep(2)

        print('Inicia script')

        while True:
            if type == AppType.READER:
                recive(port)
            elif type == AppType.SENDER:
                send(port, f'{random.randint(0, 100)}\n')

    except serial.SerialException as e:
        print(f'[ERROR] Error abriendo el puerto "{file}"')

    except KeyboardInterrupt:
        print('Interrupción manual')
    finally:

        if port:
            print('Cerrando puerto serial')
            port.close()


def get_app_type(type: str):
    app_type = None

    if type == 's':
        app_type = AppType.SENDER
    elif type == 'r':
        app_type = AppType.READER

    return app_type


if __name__ == '__main__':
    parser = ArgumentParser(
        description='Enviar o recibir mensajes usando el puerto serial'
    )

    parser.add_argument(
        '-t',
        '--type',
        choices=['s', 'r'],
        required=True,
        dest='type',
        help='Tipo de ejecución del script: "s" para enviar mensajes, "r" para recibir'
    )

    parser.add_argument(
        'file',
        type=str,
        help='Ruta al puerto serial'
    )

    args = parser.parse_args()

    if os.path.exists(args.file):
        app_type = get_app_type(args.type)

        if app_type == None:
            print(
                f'[ERROR] El tipo de ejecución del script es incorrecto: "{args.type}"'
            )
        else:
            main(args.file, app_type)
    else:
        print(f'[ERROR] El archivo "{args.file}", no existe')
