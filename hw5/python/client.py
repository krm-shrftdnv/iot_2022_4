import grpc
import message_pb2
import message_pb2_grpc


def generate_messages():
    messages = [
        message_pb2.StreamingMessageRequest(message='test1'),
        message_pb2.StreamingMessageRequest(message='test2'),
        message_pb2.StreamingMessageRequest(message='test3'),
    ]
    for m in messages:
        print(f'sending to server: {m}')
        yield m


def send_message(stub):
    responses = stub.streamingMessage(generate_messages())
    for response in responses:
        print(f'{response}')


def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = message_pb2_grpc.MessagingServiceStub(channel)
        send_message(stub)


if __name__ == '__main__':
    run()
