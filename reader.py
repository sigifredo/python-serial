
import serial
import time

PORT_NAME = '/dev/'

port = serial.Serial(PORT_NAME, 9600, timeout=1)

time.sleep(2)

while True:
    if port.in_waiting > 0:
        message = port.readline().decode().strip()
        print(f'Mensaje recibido: {message}')
