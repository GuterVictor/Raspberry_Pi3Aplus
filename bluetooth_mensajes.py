import RPi.GPIO as GPIO
import bluetooth
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 22
server_socket.bind(("",port))
server_socket.listen(1)

print("Esperando pacientemente una asquerosa conexion de Bluetooth...")

client_socket,address = server_socket.accept()
print("Conexion aceptada desde ", address)

while True:
    '''
    mensaje = input("Mensaje: ")
    mensaje += "\n"
    client_socket.send(mensaje.encode('utf-8'))
    '''
    mensaje = "Hola desde raspberry"
    mensaje += "\n"
    time.sleep(2)
    print(mensaje)
    client_socket.send(mensaje.encode('utf-8'))
client_socket.close()
server_socket.close()

