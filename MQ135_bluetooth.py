import RPi.GPIO as GPIO
import bluetooth
import time

#Configurar el modo de los pines
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # Para que no molesten las advertencias

# Definir los pines GPIO
sensor = 23
rojo = 22
verde = 24
buzz = 26

# Configurar los pines como salidas
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(rojo, GPIO.OUT)
GPIO.setup(verde, GPIO.OUT)
GPIO.setup(buzz, GPIO.OUT)

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 22
server_socket.bind(("",port))
server_socket.listen(1)
print("Esperando conexion...")
client_socket,address = server_socket.accept()
print("Conexion aceptada desde ",address)

def medir_calidad():
    lectura = GPIO.input(sensor)
    
    if lectura == GPIO.HIGH:
        mensaje = "Concentracion de gas alta"
        GPIO.output(rojo, GPIO.HIGH)
        GPIO.output(buzz, GPIO.HIGH)
        GPIO.output(verde, GPIO.LOW)
        time.sleep(2)
    else:
        mensaje = "Concentracion de gas normal"
        GPIO.output(rojo, GPIO.LOW)
        GPIO.output(verde, GPIO.HIGH)
        GPIO.output(buzz, GPIO.LOW)
        time.sleep(2)
    mensaje += "\n"
    print(mensaje)
    client_socket.send(mensaje.encode('utf-8'))


try:
    print("Leyendo sensor...")
    while True:
        medir_calidad()
        time.sleep(2)

except KeyboardInterrupt:
    client_socket.close()
    server_socket.close()
    GPIO.cleanup()

    