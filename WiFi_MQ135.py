import RPi.GPIO as GPIO
import bluetooth
import time
import http.server

host_name = '192.168.0.12'  # Dirección IP del Raspberry
host_port = 8000

# Configurar el modo de los pines
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # Para que no molesten las advertencias

# Definir los pines GPIO
rojo = 22
verde = 24
buzz = 26
sensor = 18

# Configurar los pines como salidas
GPIO.setup(rojo, GPIO.OUT)
GPIO.setup(verde, GPIO.OUT)
GPIO.setup(buzz, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

class MyServer(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        mensaje = medir_calidad()

        self.wfile.write(mensaje.encode("utf-8"))

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

    return mensaje

# # # # # Main # # # # #

if __name__ == '__main__':
    http_server = http.server.HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
        GPIO.cleanup()
    
        
        
    
