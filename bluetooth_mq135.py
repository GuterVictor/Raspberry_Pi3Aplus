import RPi.GPIO as GPIO
import bluetooth
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

rojo = 22
verde = 24
buzz = 26

GPIO.setup(verde, GPIO.OUT)
GPIO.setup(rojo, GPIO.OUT)
GPIO.setup(buzz, GPIO.OUT)

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 22
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print("Conexion aceptada desde ", address)

while True:
    data = client_socket.recv(1024)
    data = data.decode('utf-8')
    print("Recibido:", data)

    if data == "0":
        GPIO.output(verde, GPIO.LOW)
        GPIO.output(rojo, GPIO.LOW)
        GPIO.output(buzz, GPIO.LOW)
    elif data == "1":
        GPIO.output(verde, GPIO.HIGH)
        GPIO.output(rojo, GPIO.HIGH)
        GPIO.output(buzz, GPIO.HIGH)
    else:
        print("Salir")
        break

client_socket.close()
server_socket.close()
