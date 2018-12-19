# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpcFiles.database_pb2 as database__pb2


class DatabaseOperationStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/DatabaseOperation/Create',
        request_serializer=database__pb2.CrUpRequest.SerializeToString,
        response_deserializer=database__pb2.Reply.FromString,
        )
    self.Read = channel.unary_unary(
        '/DatabaseOperation/Read',
        request_serializer=database__pb2.RdDelRequest.SerializeToString,
        response_deserializer=database__pb2.Reply.FromString,
        )
    self.Update = channel.unary_unary(
        '/DatabaseOperation/Update',
        request_serializer=database__pb2.CrUpRequest.SerializeToString,
        response_deserializer=database__pb2.Reply.FromString,
        )
    self.Delete = channel.unary_unary(
        '/DatabaseOperation/Delete',
        request_serializer=database__pb2.RdDelRequest.SerializeToString,
        response_deserializer=database__pb2.Reply.FromString,
        )


class DatabaseOperationServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    """grpc database operations
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Read(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DatabaseOperationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=database__pb2.CrUpRequest.FromString,
          response_serializer=database__pb2.Reply.SerializeToString,
      ),
      'Read': grpc.unary_unary_rpc_method_handler(
          servicer.Read,
          request_deserializer=database__pb2.RdDelRequest.FromString,
          response_serializer=database__pb2.Reply.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=database__pb2.CrUpRequest.FromString,
          response_serializer=database__pb2.Reply.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=database__pb2.RdDelRequest.FromString,
          response_serializer=database__pb2.Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'DatabaseOperation', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
