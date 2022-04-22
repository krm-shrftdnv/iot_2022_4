from kafka import KafkaConsumer
from json import loads


def serve():
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='iot4-2022',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
        print(f'message from kafka received: {message}')


if __name__ == '__main__':
    serve()
