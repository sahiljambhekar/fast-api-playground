# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
import warnings

from . import random_city_pb2 as pb_dot_random__city__pb2

GRPC_GENERATED_VERSION = "1.68.0"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in pb/random_city_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class RandomCityServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRandomCity = channel.unary_unary(
            "/randomcity.RandomCityService/GetRandomCity",
            request_serializer=pb_dot_random__city__pb2.RandomCityRequest.SerializeToString,
            response_deserializer=pb_dot_random__city__pb2.RandomCityResponse.FromString,
            _registered_method=True,
        )


class RandomCityServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetRandomCity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_RandomCityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetRandomCity": grpc.unary_unary_rpc_method_handler(
            servicer.GetRandomCity,
            request_deserializer=pb_dot_random__city__pb2.RandomCityRequest.FromString,
            response_serializer=pb_dot_random__city__pb2.RandomCityResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "randomcity.RandomCityService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers(
        "randomcity.RandomCityService", rpc_method_handlers
    )


# This class is part of an EXPERIMENTAL API.
class RandomCityService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetRandomCity(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/randomcity.RandomCityService/GetRandomCity",
            pb_dot_random__city__pb2.RandomCityRequest.SerializeToString,
            pb_dot_random__city__pb2.RandomCityResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )