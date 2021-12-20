#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

while True:
    for color, pin in [('red', 26), ('yellow', 6), ('green', 5)]:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin,GPIO.OUT)
        print(f"{color} LED on (pin {pin})")
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        print(f"{color} LED off")
        GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
