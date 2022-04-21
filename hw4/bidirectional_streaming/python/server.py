from concurrent import futures

import grpc
import number_pb2_grpc
import number_pb2


class CalculationService(number_pb2_grpc.CalculationServiceServicer):

    def streamingMax(self, request_iterator, context):
        # current_max = -1
        for number in request_iterator:
            yield number_pb2.StreamingMaxResponse(result=5)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    number_pb2_grpc.add_CalculationServiceServicer_to_server(CalculationService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
