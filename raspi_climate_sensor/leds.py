try:
    import RPi.GPIO as GPIO

    def setup_pin_for_led(gpio_pin: int):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(gpio_pin, GPIO.OUT)
        pass

    def set_led_status_on_pin(gpio_pin: int, status: int):
        GPIO.output(gpio_pin, GPIO.HIGH if status > 0 else GPIO.LOW)
        pass
except:
    def setup_pin_for_led(gpio_pin: int):
        print(f"Fallback: setup GPIO {gpio_pin} for LED")
    
    def set_led_status_on_pin(gpio_pin: int, status: int):
        print(f"Fallback: set LED on GPIO {gpio_pin} to {status}")
