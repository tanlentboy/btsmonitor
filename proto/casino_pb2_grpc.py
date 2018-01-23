# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import casino_pb2 as casino__pb2


class CasinoStub(object):
  """定义赌场服务
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SentNotice = channel.unary_unary(
        '/casinoserver.Casino/SentNotice',
        request_serializer=casino__pb2.SentNoticeRequest.SerializeToString,
        response_deserializer=casino__pb2.SentNoticeReply.FromString,
        )
    self.ReceiveNotice = channel.unary_unary(
        '/casinoserver.Casino/ReceiveNotice',
        request_serializer=casino__pb2.ReceiveNoticeRequest.SerializeToString,
        response_deserializer=casino__pb2.ReceiveNoticeReply.FromString,
        )


class CasinoServicer(object):
  """定义赌场服务
  """

  def SentNotice(self, request, context):
    """SentNotice 转款通知
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReceiveNotice(self, request, context):
    """ReceiveNotice 收款通知
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CasinoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SentNotice': grpc.unary_unary_rpc_method_handler(
          servicer.SentNotice,
          request_deserializer=casino__pb2.SentNoticeRequest.FromString,
          response_serializer=casino__pb2.SentNoticeReply.SerializeToString,
      ),
      'ReceiveNotice': grpc.unary_unary_rpc_method_handler(
          servicer.ReceiveNotice,
          request_deserializer=casino__pb2.ReceiveNoticeRequest.FromString,
          response_serializer=casino__pb2.ReceiveNoticeReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'casinoserver.Casino', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
