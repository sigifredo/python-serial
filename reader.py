
import serial
import time

PORT_NAME = '/dev/ttys007'

port = None

try:
    port = serial.Serial(PORT_NAME, 9600, timeout=1)

    time.sleep(2)

    print('Inicia script')

    sequence = 0

    while True:
        if port.in_waiting > 0:
            message = port.readline().decode().strip()
            print(f'Mensaje #{sequence} recibido: {message}')

            sequence += 1

except serial.SerialException as e:
    print(f'[ERROR] Error abriendo el puerto "{PORT_NAME}"')

except KeyboardInterrupt:
    print('Interrupción manual')
finally:

    if port:
        print('Cerrando puerto serial')
        port.close()
