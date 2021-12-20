try:
    import ST7735

    display = ST7735.ST7735(port=0, cs=0, dc=24, backlight=None, rst=25, width=128, height=160, rotation=0, invert=False)

    image_width = display.width
    image_height = display.height

    def display_image(img):
        display.display(img)
except:
    image_width = 128
    image_height = 160

    def display_image(img):
        print("Would display image here")
