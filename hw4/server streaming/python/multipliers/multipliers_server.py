from concurrent import futures
from math import gcd

import grpc
import multipliers_pb2
import multipliers_pb2_grpc


def factorization(n):
    factors = []

    def get_factor(m):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for count in range(cycle_size):
                if factor > 1:
                    break
                x = (x * x + 1) % m
                factor = gcd(x - x_fixed, m)

            cycle_size *= 2
            x_fixed = x

        return factor

    while n > 1:
        next_num = get_factor(n)
        factors.append(next_num)
        n //= next_num

    return factors


class MultipliersServicer(multipliers_pb2_grpc.MultipliersServicer):

    def ListFeatures(self, request, context):
        multipliers_values = factorization(request.value)
        for value in multipliers_values:
            yield multipliers_pb2.Number(value=value)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    multipliers_pb2_grpc.add_MultipliersServicer_to_server(
      MultipliersServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
