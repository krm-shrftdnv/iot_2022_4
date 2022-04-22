import time
import threading
import schedule
from paho.mqtt import client as mqtt
import json, requests

BROKER_ADDRESS = 'broker.hivemq.com'
BROKER_PORT = 1883
COMMAND_TOPIC = 'itis_team_4/control'
INDICATIONS_TOPIC = 'itis_team_4/indications'
HARDWARE_SERVICE_ADDRESS = 'localhost'
HARDWARE_SERVICE_PORT = '5000'
STREAM = True
PUBLISH_INTERVAL = 2

client_streamer = mqtt.Client()
client_streamer.connect(BROKER_ADDRESS, BROKER_PORT, 60)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("$SYS/#")


def publish_indications():
    response = requests.get(f'http://{HARDWARE_SERVICE_ADDRESS}:{HARDWARE_SERVICE_PORT}/indications')
    if response.status_code == 200:
        indications = response.json()
        client_streamer.publish(INDICATIONS_TOPIC, json.dumps(response.json()))


def publish_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global client_streamer
    global STREAM
    message = msg.payload.decode()
    print(message)
    command = json.loads(message)['command']
    if command == 'get':
        publish_indications()
    elif command == 'alert':
        print(command)
        # requests.post(f'http://{HARDWARE_SERVICE_ADDRESS}:{HARDWARE_SERVICE_PORT}/command', data={'command': 'alert'})
    elif command == 'alert_off':
        requests.post(f'http://{HARDWARE_SERVICE_ADDRESS}:{HARDWARE_SERVICE_PORT}/command',
                      data={'command': 'alert_off'})
    elif command == 'start':
        STREAM = True
    elif command == 'stop':
        STREAM = False


client_subscriber = mqtt.Client()
client_subscriber.on_connect = on_connect
client_subscriber.on_message = on_message

client_subscriber.connect(BROKER_ADDRESS, BROKER_PORT, 60)
client_subscriber.subscribe(COMMAND_TOPIC)
client_subscriber.loop_start()

schedule.every(PUBLISH_INTERVAL).seconds.do(publish_threaded(publish_indications()))
while True:
    schedule.run_pending()
    time.sleep(1)
