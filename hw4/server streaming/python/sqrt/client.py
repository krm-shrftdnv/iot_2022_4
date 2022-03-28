import grpc
import sqrt_pb2_grpc
import sqrt_pb2

if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    stub = sqrt_pb2_grpc.SqrtStub(channel)
    print(stub.Sqrt(sqrt_pb2.Number(value=9)))
