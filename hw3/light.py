import RPi.GPIO as GPIO, time
import paho.mqtt.client as mqtt
# Tell the GPIO library to use
# Broadcom GPIO references
GPIO.setmode(GPIO.BCM)

# Define function to measure charge time
def RCtime (PiPin):
    measurement = 0
    # Discharge capacitor
    GPIO.setup(PiPin, GPIO.OUT)
    GPIO.output(PiPin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(PiPin, GPIO.IN)
    # Count loops until voltage across
    # capacitor reads high on GPIO
    while (GPIO.input(PiPin) == GPIO.LOW):
        measurement += 1

        return measurement

broker = "broker.hivemq.com"
port = 1883
client = mqtt.Client("LS")
client.connect(broker, port)

# Main program loop
while True:
    signal = RCtime(4)
    if signal:
       message = "Light bright"
    else:
       message = "Light low"
    print("Sending message:", message)
    client.publish("itis/team_№4", message) # Publish resulting message
    time.sleep(2)
