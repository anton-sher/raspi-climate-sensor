#!/usr/bin/env python3

import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import leds,hygrometer,display

PIN_RED = 26
PIN_YELLOW = 6
PIN_GREEN = 5

def initialize():
    leds.setup_pin_for_led(PIN_GREEN)
    leds.setup_pin_for_led(PIN_YELLOW)
    leds.setup_pin_for_led(PIN_RED)
    font = ImageFont.load_default()

def make_image(temperature, pressure, humidity):
    img = Image.new('RGB', (display.image_width, display.image_height))
    draw = ImageDraw.Draw(img)
    draw.text((5, 5),  f"Temperature : {temperature:5d} °C", font=font, fill=(255, 255, 255))
    draw.text((5, 25), f"Humidity    : {humidity:5d} %", font=font, fill=(255, 255, 255))
    draw.text((5, 45), f"Pressure    : {pressure:5d} hPa", font=font, fill=(255, 255, 255))
    return img

def main_cycle():
    temperature, pressure, humidity = hygrometer.read_temp_pressure_humidity()
    image = make_image(temperature, pressure, humidity)
    display.display_image(image)

if __name__ == "__main__":
    initialize()
    while True:
        main_cycle()
        time.sleep(30)
