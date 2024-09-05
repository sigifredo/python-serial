
import serial
import time

port = serial.Serial('/dev/tty.usbserial-XXXX', 9600, timeout=1)

time.sleep(2)

message = 'Hola desde python'

port.write(message.encode())

port.close()

print(f'Mensaje enviado: ${message}')
