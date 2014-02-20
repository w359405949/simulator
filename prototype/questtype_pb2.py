# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: questtype.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='questtype.proto',
  package='msg.quest',
  serialized_pb='\n\x0fquesttype.proto\x12\tmsg.quest\"0\n\x0fQuestTargetBase\x12\x0e\n\x06target\x18\x01 \x02(\x05\x12\r\n\x05\x63ount\x18\x02 \x02(\x05\"=\n\rQuestInfoBase\x12\r\n\x05quest\x18\x01 \x02(\x05\x12\x0f\n\x07\x63ounter\x18\x02 \x02(\x05\x12\x0c\n\x04type\x18\x03 \x01(\x05\"-\n\x0eQuestTimesBase\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\r\n\x05\x63ount\x18\x02 \x02(\x05')




_QUESTTARGETBASE = _descriptor.Descriptor(
  name='QuestTargetBase',
  full_name='msg.quest.QuestTargetBase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='msg.quest.QuestTargetBase.target', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='msg.quest.QuestTargetBase.count', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=30,
  serialized_end=78,
)


_QUESTINFOBASE = _descriptor.Descriptor(
  name='QuestInfoBase',
  full_name='msg.quest.QuestInfoBase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quest', full_name='msg.quest.QuestInfoBase.quest', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counter', full_name='msg.quest.QuestInfoBase.counter', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='msg.quest.QuestInfoBase.type', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=80,
  serialized_end=141,
)


_QUESTTIMESBASE = _descriptor.Descriptor(
  name='QuestTimesBase',
  full_name='msg.quest.QuestTimesBase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='msg.quest.QuestTimesBase.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='msg.quest.QuestTimesBase.count', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=143,
  serialized_end=188,
)

DESCRIPTOR.message_types_by_name['QuestTargetBase'] = _QUESTTARGETBASE
DESCRIPTOR.message_types_by_name['QuestInfoBase'] = _QUESTINFOBASE
DESCRIPTOR.message_types_by_name['QuestTimesBase'] = _QUESTTIMESBASE

class QuestTargetBase(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUESTTARGETBASE

  # @@protoc_insertion_point(class_scope:msg.quest.QuestTargetBase)

class QuestInfoBase(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUESTINFOBASE

  # @@protoc_insertion_point(class_scope:msg.quest.QuestInfoBase)

class QuestTimesBase(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUESTTIMESBASE

  # @@protoc_insertion_point(class_scope:msg.quest.QuestTimesBase)


# @@protoc_insertion_point(module_scope)
