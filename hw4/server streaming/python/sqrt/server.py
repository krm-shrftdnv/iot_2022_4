import grpc
from concurrent import futures
import sqrt_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sqrt_pb2_grpc.add_SqrtServicer_to_server(
        sqrt_pb2_grpc.SqrtServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
