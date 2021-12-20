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
    font = ImageFont.truetype('/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf', 24)
    return font

def make_image(font, temperature, pressure, humidity):
    img = Image.new('RGB', (display.image_width, display.image_height))
    draw = ImageDraw.Draw(img)
    draw.text((10, 5),  f"{temperature:.1f} °C", font=font, fill=(255, 255, 255))
    draw.text((10, 45), f"{humidity:.0f} %", font=font, fill=(255, 255, 255))
    draw.text((10, 85), f"{pressure:.0f} hPa", font=font, fill=(255, 255, 255))
    return img

def main_cycle(font):
    temperature, pressure, humidity = hygrometer.read_temp_pressure_humidity()
    image = make_image(font, temperature, pressure, humidity)
    display.display_image(image)

if __name__ == "__main__":
    font = initialize()
    while True:
        main_cycle(font)
        time.sleep(30)
