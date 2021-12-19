#!/usr/bin/env python3

import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ST7735

disp = ST7735.ST7735(port=0, cs=0, dc=24, backlight=None, rst=25, width=128, height=160, rotation=0, invert=False)

WIDTH = disp.width
HEIGHT = disp.height

# Load default font.
font = ImageFont.load_default()

posx = 0
while True:
    posx = posx - 1 if posx > 0 else 64
    # Write some text
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    draw.text((posx, 5), "Hello World!", font=font, fill=(255, 255, 255))

    # Write buffer to display hardware, must be called to make things visible on the
    # display!
    disp.display(img)
    time.sleep(0.005)
