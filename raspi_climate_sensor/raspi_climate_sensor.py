#!/usr/bin/env python3

import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import hygrometer,display,co2meter

def initialize():
    font = ImageFont.truetype('/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf', 30)
    return font

def make_image(font, status_color, temperature, pressure, humidity, co2level):
    img = Image.new(mode='RGB', size=(display.image_width, display.image_height), color=status_color)
    draw = ImageDraw.Draw(img)
    draw.ellipse((80, 15, 110, 45), fill=status_color, outline = status_color)
    if temperature is not None:
        draw.text((5, 0),  f"{temperature:.0f}°", font=font, fill=(0, 0, 0))
        draw.text((5, 40), f"{humidity:.0f}%", font=font, fill=(0, 0, 0))
    else:
        draw.text((5, 0),  f"???°", font=font, fill=(0, 0, 0))
        draw.text((5, 40), f"???%", font=font, fill=(0, 0, 0))
    draw.text((5, 80), f"{co2level:.0f} ppm", font=font, fill=(0, 0, 0))
    draw.text((5, 120), f"{time.strftime('%H:%M:%S')}", font=font, fill=(0, 0, 0))
    return img

def main_cycle(font):
    temperature, pressure, humidity = None, None, None
    try:
        temperature, pressure, humidity = hygrometer.read_temp_pressure_humidity()
    except Exception as e:
        print("Could not read BME280 sensor:", repr(e), "\n")
    co2level = co2meter.get_co2_level()
    status_color = 'grey'
    if co2level <= 800:
        status_color = 'green'
    elif co2level <= 1200:
        status_color = 'yellow'
    else:
        status_color = 'red'
    for _ in range(10):
        image = make_image(font, status_color, temperature, pressure, humidity, co2level)
        display.display_image(image)
        time.sleep(1)

if __name__ == "__main__":
    font = initialize()
    while True:
        main_cycle(font)
