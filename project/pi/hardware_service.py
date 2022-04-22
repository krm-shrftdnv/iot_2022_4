from flask import Flask, request
from ccs811 import *
import RPi.GPIO as IO
import json

app = Flask(__name__)

ALERT = False
LED_PIN = 40


def turn_led_on():
    IO.setup(LED_PIN, IO.OUT)
    IO.output(LED_PIN, 1)


def turn_led_off():
    IO.setup(LED_PIN, IO.OUT)
    IO.output(LED_PIN, 0)


@app.route('/indications')
def get_indications():
    ccs811SetEnvironmentalData(21.102, 57.73)
    if ccs811CheckDataAndUpdate():
        CO2 = ccs811GetCO2()
        tVOC = ccs811GetTVOC()
        return json.dumps({'CO2': CO2, 'tVOC': tVOC})
    elif ccs811CheckForError():
        ccs811PrintError()
        return json.dumps({'error': 'ccs811_error'}), 500


@app.route('/command', methods=['POST'])
def command():
    global ALERT
    if request.method == 'POST':
        content = request.json
        command = content['command']
        if command == 'alert':
            if not ALERT:
                turn_led_on()
                ALERT = False
        elif command == 'alert_off':
            if not ALERT:
                turn_led_off()
                ALERT = True
        else:
            return json.dumps({'error': 'Unsupported command'}), 400
        return json.dumps({'result': 'OK'}), 200
    else:
        return 405


if __name__ == "__main__":
    ccs811Begin(CCS811_driveMode_1sec)
    app.run()
