import RPi.GPIO as GPIO

import time


GPIO.setmode(GPIO.BCM)

red = 20
blue = 21
green = 22

GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


red_power = 0
green_power = 1
blue_power = 0

while True:

    input_state = GPIO.input(18)
    GPIO.output(red, red_power)
    GPIO.output(blue, blue_power)
    GPIO.output(green, green_power)

    if input_state == False:

        print('Button Pressed')
        if green_power:
            green_power = 0
            red_power = 1
            blue_power = 0
        elif red_power:
            green_power = 0
            red_power = 0
            blue_power = 1
        else:
            green_power = 1
            red_power = 0
            blue_power = 0
        time.sleep(0.2)
