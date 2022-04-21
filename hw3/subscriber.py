import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

broker = "broker.hivemq.com"
port = 1883
topic = "itis/team_№4"
client = mqtt.Client("LS_SUBCRIBER_1")
client.connect(broker, port)
client.subscribe(topic)
client.on_message = on_message
client.loop_forever()
