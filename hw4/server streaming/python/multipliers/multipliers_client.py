import random

import grpc
import multipliers_pb2
import multipliers_pb2_grpc


def multipliers_list_features(stub):
    number = multipliers_pb2.Number(
      value=random.randint(100, 1000)
    )
    print("Trying get multiplers of number ", number.value)

    features = stub.ListFeatures(number)

    print("multipliers:")

    for feature in features:
        print(feature.value)

    print("The End.")


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = multipliers_pb2_grpc.MultipliersStub(channel)
        print("-------------- ListFeatures --------------")
        multipliers_list_features(stub)


if __name__ == '__main__':
    run()
