from __future__ import print_function

import grpc
import number_pb2_grpc
import number_pb2


def make_number(number):
    return number_pb2.StreamingMaxRequest(
        number=number
    )


def generate_numbers():
    numbers = [
        make_number(1),
        make_number(7),
        make_number(3),
        make_number(2),
        make_number(10),
    ]
    for n in numbers:
        print("Hello, Server, Sending you the %s" % n)
        yield n


def send_number(stub):
    responses = stub.streamingMax(generate_numbers())
    for response in responses:
        print("Hello from the server received your %s" % response)


def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = number_pb2_grpc.CalculationServiceStub(channel)
        send_number(stub)


if __name__ == '__main__':
    run()
