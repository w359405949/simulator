# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: itemtype.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='itemtype.proto',
  package='msg.item',
  serialized_pb='\n\x0eitemtype.proto\x12\x08msg.item\"O\n\rItemDirtyInfo\x12\x0e\n\x06\x65xtra1\x18\x01 \x01(\r\x12\x0e\n\x06\x65xtra2\x18\x02 \x01(\r\x12\x0e\n\x06\x65xtra3\x18\x03 \x01(\r\x12\x0e\n\x06\x65xtra4\x18\x04 \x01(\r\"\xbe\x02\n\x08ItemInfo\x12\x10\n\x08\x65ntityid\x18\x01 \x01(\t\x12\x0e\n\x06\x62\x61seid\x18\x02 \x01(\r\x12\r\n\x05\x63ount\x18\x03 \x01(\r\x12\x0f\n\x07quality\x18\x04 \x01(\r\x12\x0f\n\x07soldier\x18\x05 \x01(\r\x12\r\n\x05level\x18\x06 \x01(\r\x12\x0e\n\x06\x65xtra1\x18\x07 \x01(\r\x12\x0e\n\x06\x65xtra2\x18\x08 \x01(\r\x12\x0e\n\x06\x65xtra3\x18\t \x01(\r\x12\x0e\n\x06\x65xtra4\x18\n \x01(\r\x12\x0c\n\x04gem1\x18\x0b \x01(\r\x12\x0c\n\x04gem2\x18\x0c \x01(\r\x12\x0c\n\x04gem3\x18\r \x01(\r\x12\x0c\n\x04gem4\x18\x0e \x01(\r\x12\x0c\n\x04prob\x18\x0f \x01(\r\x12&\n\x05\x64irty\x18\x10 \x01(\x0b\x32\x17.msg.item.ItemDirtyInfo\x12\x10\n\x08\x64ressexp\x18\x11 \x01(\r\x12\x10\n\x08\x64ressres\x18\x12 \x01(\r\"/\n\x0cItemBaseUnit\x12\x10\n\x08\x65ntityid\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\r\".\n\rLockExtrainfo\x12\x0c\n\x04solt\x18\x01 \x01(\x05\x12\x0f\n\x07\x65xtraid\x18\x02 \x01(\x05\"@\n\x0fShopArticleUnit\x12\x11\n\tarticleid\x18\x01 \x02(\x05\x12\r\n\x05\x63ount\x18\x02 \x02(\r\x12\x0b\n\x03tag\x18\x03 \x02(\r')




_ITEMDIRTYINFO = _descriptor.Descriptor(
  name='ItemDirtyInfo',
  full_name='msg.item.ItemDirtyInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='extra1', full_name='msg.item.ItemDirtyInfo.extra1', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra2', full_name='msg.item.ItemDirtyInfo.extra2', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra3', full_name='msg.item.ItemDirtyInfo.extra3', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra4', full_name='msg.item.ItemDirtyInfo.extra4', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=28,
  serialized_end=107,
)


_ITEMINFO = _descriptor.Descriptor(
  name='ItemInfo',
  full_name='msg.item.ItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entityid', full_name='msg.item.ItemInfo.entityid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='baseid', full_name='msg.item.ItemInfo.baseid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='msg.item.ItemInfo.count', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quality', full_name='msg.item.ItemInfo.quality', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soldier', full_name='msg.item.ItemInfo.soldier', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='msg.item.ItemInfo.level', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra1', full_name='msg.item.ItemInfo.extra1', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra2', full_name='msg.item.ItemInfo.extra2', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra3', full_name='msg.item.ItemInfo.extra3', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra4', full_name='msg.item.ItemInfo.extra4', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gem1', full_name='msg.item.ItemInfo.gem1', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gem2', full_name='msg.item.ItemInfo.gem2', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gem3', full_name='msg.item.ItemInfo.gem3', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gem4', full_name='msg.item.ItemInfo.gem4', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prob', full_name='msg.item.ItemInfo.prob', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dirty', full_name='msg.item.ItemInfo.dirty', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dressexp', full_name='msg.item.ItemInfo.dressexp', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dressres', full_name='msg.item.ItemInfo.dressres', index=17,
      number=18, type=13, cpp_type=3, label=1,
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
  serialized_start=110,
  serialized_end=428,
)


_ITEMBASEUNIT = _descriptor.Descriptor(
  name='ItemBaseUnit',
  full_name='msg.item.ItemBaseUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entityid', full_name='msg.item.ItemBaseUnit.entityid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='msg.item.ItemBaseUnit.count', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=430,
  serialized_end=477,
)


_LOCKEXTRAINFO = _descriptor.Descriptor(
  name='LockExtrainfo',
  full_name='msg.item.LockExtrainfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='solt', full_name='msg.item.LockExtrainfo.solt', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extraid', full_name='msg.item.LockExtrainfo.extraid', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=479,
  serialized_end=525,
)


_SHOPARTICLEUNIT = _descriptor.Descriptor(
  name='ShopArticleUnit',
  full_name='msg.item.ShopArticleUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='articleid', full_name='msg.item.ShopArticleUnit.articleid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='msg.item.ShopArticleUnit.count', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='msg.item.ShopArticleUnit.tag', index=2,
      number=3, type=13, cpp_type=3, label=2,
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
  serialized_start=527,
  serialized_end=591,
)

_ITEMINFO.fields_by_name['dirty'].message_type = _ITEMDIRTYINFO
DESCRIPTOR.message_types_by_name['ItemDirtyInfo'] = _ITEMDIRTYINFO
DESCRIPTOR.message_types_by_name['ItemInfo'] = _ITEMINFO
DESCRIPTOR.message_types_by_name['ItemBaseUnit'] = _ITEMBASEUNIT
DESCRIPTOR.message_types_by_name['LockExtrainfo'] = _LOCKEXTRAINFO
DESCRIPTOR.message_types_by_name['ShopArticleUnit'] = _SHOPARTICLEUNIT

class ItemDirtyInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMDIRTYINFO

  # @@protoc_insertion_point(class_scope:msg.item.ItemDirtyInfo)

class ItemInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMINFO

  # @@protoc_insertion_point(class_scope:msg.item.ItemInfo)

class ItemBaseUnit(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMBASEUNIT

  # @@protoc_insertion_point(class_scope:msg.item.ItemBaseUnit)

class LockExtrainfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOCKEXTRAINFO

  # @@protoc_insertion_point(class_scope:msg.item.LockExtrainfo)

class ShopArticleUnit(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHOPARTICLEUNIT

  # @@protoc_insertion_point(class_scope:msg.item.ShopArticleUnit)


# @@protoc_insertion_point(module_scope)
