import RPi.GPIO as GPIO

import time


GPIO.setmode(GPIO.BCM)

# led colors connection
RED = 20
BLUE = 21
GREEN = 22

# setup GPIO channels
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


red_power = 0
green_power = 1
blue_power = 0

while True:
    try:
        input_state = GPIO.input(18)
        GPIO.output(RED, red_power)
        GPIO.output(BLUE, blue_power)
        GPIO.output(GREEN, green_power)

        # if button is pressed
        if not input_state:
            print('Button Pressed')

            # change led color by specified order: g -> r -> b -> g
            if green_power:
                green_power = 0
                red_power = 1
            elif red_power:
                red_power = 0
                blue_power = 1
            else:
                green_power = 1
                blue_power = 0
            time.sleep(0.2)
    except KeyboardInterrupt:
        GPIO.cleanup()
