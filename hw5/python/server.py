from concurrent import futures
from json import dumps

import grpc
import message_pb2
import message_pb2_grpc
from kafka import KafkaProducer


def produce_kafka_message(message_string):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))
    data = {'message': message_string}
    producer.send('messages', value=data)


class MessageService(message_pb2_grpc.MessagingServiceServicer):

    def streamingMessage(self, request_iterator, context):
        for iterable in request_iterator:
            message = iterable.message
            print(f'message received on server: {message}')
            produce_kafka_message(message)
            response_message = 'message on server received'
            yield message_pb2.StreamingMessageResponse(message=response_message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_MessagingServiceServicer_to_server(MessageService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
