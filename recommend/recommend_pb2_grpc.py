# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import recommend_pb2 as recommend__pb2


class RecommenderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recommned = channel.unary_unary(
                '/recommend.Recommender/Recommned',
                request_serializer=recommend__pb2.RecommnedRequest.SerializeToString,
                response_deserializer=recommend__pb2.RecommendResponseList.FromString,
                )


class RecommenderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Recommned(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecommenderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Recommned': grpc.unary_unary_rpc_method_handler(
                    servicer.Recommned,
                    request_deserializer=recommend__pb2.RecommnedRequest.FromString,
                    response_serializer=recommend__pb2.RecommendResponseList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'recommend.Recommender', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Recommender(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Recommned(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recommend.Recommender/Recommned',
            recommend__pb2.RecommnedRequest.SerializeToString,
            recommend__pb2.RecommendResponseList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)