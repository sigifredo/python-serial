
import serial
import time

PORT_NAME = '/dev/ttys006'

port = serial.Serial(PORT_NAME, 9600, timeout=1)

time.sleep(2)

message = 'Hola desde python\n'

try:
    print('Inicia el script')

    sequence = 0

    while True:
        port.write(message.encode())
        print(f'Mensaje {sequence} enviado: {message.strip()}')

        sequence += 1

        time.sleep(1)

except KeyboardInterrupt:
    print('Script interrumpido')

finally:
    port.close()
