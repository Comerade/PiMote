#
# Blink led connected to GPIO pin 17 for 1 minute.
# [PIN 17] -> RESISTOR(280ohm) -> LED -> GND
#

import RPi.GPIO as GPIO
import time

def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

for i in range(0,60):
        blink(11)

GPIO.cleanup()