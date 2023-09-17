import RPi.GPIO as GPIO
import time

#Configurar el modo de los pines
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Definir los pines GPIO
led1 = 22
led2 = 24
buzz = 26

# Configurar los pines como salidas
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(buzz, GPIO.OUT)
time.sleep(2)

# Encender y apagar leds
for i in range(1):
    GPIO.output(led1, GPIO.HIGH)        
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(buzz, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(led1, GPIO.LOW)        
    GPIO.output(led2, GPIO.HIGH)
    GPIO.output(buzz, GPIO.LOW)
    time.sleep(2)
    GPIO.output(led1, GPIO.HIGH)        
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(buzz, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(led1, GPIO.LOW)        
    GPIO.output(led2, GPIO.HIGH)
    GPIO.output(buzz, GPIO.LOW)
    time.sleep(2)

GPIO.cleanup() # Limpia y libera los recursos GPIO 
