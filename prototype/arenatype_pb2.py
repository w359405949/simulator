# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arenatype.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='arenatype.proto',
  package='msg.arena',
  serialized_pb='\n\x0f\x61renatype.proto\x12\tmsg.arena\"n\n\x10\x41IPKFiveRankInfo\x12\x0c\n\x04rank\x18\x01 \x01(\x05\x12\x0e\n\x06unitid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05level\x18\x04 \x01(\x05\x12\r\n\x05\x66ight\x18\x05 \x01(\x05\x12\x10\n\x08in_fight\x18\x06 \x01(\x08\"h\n\x0e\x41IPKNoticeInfo\x12\x0e\n\x06unitid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x0e\n\x06result\x18\x04 \x01(\x05\x12\x0c\n\x04time\x18\x05 \x01(\x05\x12\x0c\n\x04rank\x18\x06 \x01(\x05')




_AIPKFIVERANKINFO = _descriptor.Descriptor(
  name='AIPKFiveRankInfo',
  full_name='msg.arena.AIPKFiveRankInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank', full_name='msg.arena.AIPKFiveRankInfo.rank', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unitid', full_name='msg.arena.AIPKFiveRankInfo.unitid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='msg.arena.AIPKFiveRankInfo.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='msg.arena.AIPKFiveRankInfo.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fight', full_name='msg.arena.AIPKFiveRankInfo.fight', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_fight', full_name='msg.arena.AIPKFiveRankInfo.in_fight', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=30,
  serialized_end=140,
)


_AIPKNOTICEINFO = _descriptor.Descriptor(
  name='AIPKNoticeInfo',
  full_name='msg.arena.AIPKNoticeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unitid', full_name='msg.arena.AIPKNoticeInfo.unitid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='msg.arena.AIPKNoticeInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='msg.arena.AIPKNoticeInfo.type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='msg.arena.AIPKNoticeInfo.result', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='msg.arena.AIPKNoticeInfo.time', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='msg.arena.AIPKNoticeInfo.rank', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=142,
  serialized_end=246,
)

DESCRIPTOR.message_types_by_name['AIPKFiveRankInfo'] = _AIPKFIVERANKINFO
DESCRIPTOR.message_types_by_name['AIPKNoticeInfo'] = _AIPKNOTICEINFO

class AIPKFiveRankInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AIPKFIVERANKINFO

  # @@protoc_insertion_point(class_scope:msg.arena.AIPKFiveRankInfo)

class AIPKNoticeInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AIPKNOTICEINFO

  # @@protoc_insertion_point(class_scope:msg.arena.AIPKNoticeInfo)


# @@protoc_insertion_point(module_scope)
