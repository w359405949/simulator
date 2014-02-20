# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scenetype.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='scenetype.proto',
  package='msg.scene',
  serialized_pb='\n\x0fscenetype.proto\x12\tmsg.scene\"G\n\nUnitAvatar\x12\r\n\x05\x64ress\x18\x01 \x01(\x05\x12\x0c\n\x04wing\x18\x02 \x01(\x05\x12\r\n\x05trump\x18\x03 \x01(\x05\x12\r\n\x05title\x18\x04 \x01(\x05\"v\n\rSceneUnitInfo\x12\x0e\n\x06unitid\x18\x01 \x01(\t\x12\x10\n\x08rolename\x18\x02 \x01(\t\x12%\n\x06\x61vatar\x18\x03 \x01(\x0b\x32\x15.msg.scene.UnitAvatar\x12\r\n\x05pos_x\x18\x04 \x01(\x05\x12\r\n\x05pos_y\x18\x05 \x01(\x05\"K\n\nFightSpell\x12\r\n\x05spell\x18\x01 \x01(\x05\x12\r\n\x05power\x18\x02 \x01(\x05\x12\x0f\n\x07truedam\x18\x03 \x01(\x05\x12\x0e\n\x06\x62uffid\x18\x04 \x01(\x05\"M\n\nFightTrump\x12\x0f\n\x07trumpid\x18\x01 \x02(\x05\x12\r\n\x05power\x18\x02 \x02(\x05\x12\x0f\n\x07truedam\x18\x03 \x02(\x05\x12\x0e\n\x06\x62uffid\x18\x04 \x02(\x05\"\xb2\x02\n\x0b\x46ightFactor\x12\n\n\x02lv\x18\x01 \x01(\x05\x12\n\n\x02hp\x18\x02 \x01(\x05\x12\r\n\x05maxhp\x18\x03 \x01(\x05\x12\x0e\n\x06phyatk\x18\x04 \x01(\x05\x12\x0e\n\x06phydef\x18\x05 \x01(\x05\x12\x0e\n\x06magatk\x18\x06 \x01(\x05\x12\x0e\n\x06magdef\x18\x07 \x01(\x05\x12\x0c\n\x04\x63rit\x18\x08 \x01(\x05\x12\x0e\n\x06resist\x18\t \x01(\x05\x12\x14\n\x0c\x63ritmultiple\x18\n \x01(\x05\x12\x0f\n\x07truedef\x18\x0b \x01(\x05\x12\x0e\n\x06\x65leatk\x18\x0c \x01(\x05\x12\x0f\n\x07\x65letype\x18\r \x01(\x05\x12\x10\n\x08metaldef\x18\x0e \x01(\x05\x12\x0f\n\x07wooddef\x18\x0f \x01(\x05\x12\x10\n\x08waterdef\x18\x10 \x01(\x05\x12\x0f\n\x07\x66iredef\x18\x11 \x01(\x05\x12\x10\n\x08\x65\x61rthdef\x18\x12 \x01(\x05\"~\n\x0c\x46ightSoldier\x12\x0e\n\x06unitid\x18\x01 \x01(\t\x12\x0f\n\x07soldier\x18\x02 \x01(\x05\x12&\n\x06\x66\x61\x63tor\x18\x03 \x01(\x0b\x32\x16.msg.scene.FightFactor\x12%\n\x06spells\x18\x04 \x03(\x0b\x32\x15.msg.scene.FightSpell\"\x8d\x02\n\x0c\x43opyUnitInfo\x12\x0e\n\x06unitid\x18\x01 \x01(\t\x12\x10\n\x08rolename\x18\x02 \x01(\t\x12\x0f\n\x07soldier\x18\x03 \x01(\x05\x12\r\n\x05\x64ress\x18\x04 \x01(\x05\x12\r\n\x05title\x18\x05 \x01(\x05\x12\x0c\n\x04seed\x18\x06 \x01(\x05\x12&\n\x06\x66\x61\x63tor\x18\x07 \x01(\x0b\x32\x16.msg.scene.FightFactor\x12$\n\x05trump\x18\x08 \x01(\x0b\x32\x15.msg.scene.FightTrump\x12%\n\x06spells\x18\t \x03(\x0b\x32\x15.msg.scene.FightSpell\x12)\n\x08soldiers\x18\n \x03(\x0b\x32\x17.msg.scene.FightSoldier\"0\n\nSupplyInfo\x12\x10\n\x08supplyid\x18\x01 \x01(\x05\x12\x10\n\x08position\x18\x02 \x01(\x05\"p\n\x0ePkCopyUnitInfo\x12\x0e\n\x06unitid\x18\x01 \x01(\t\x12\x10\n\x08rolename\x18\x02 \x01(\t\x12\x0f\n\x07soldier\x18\x03 \x01(\x05\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x10\n\x08viplevel\x18\x05 \x01(\x05\x12\n\n\x02\x62p\x18\x06 \x01(\x05\"N\n\x10\x43opyProgressInfo\x12\x0e\n\x06\x63opyid\x18\x01 \x01(\x05\x12\x13\n\x0b\x66ightstatus\x18\x02 \x03(\x05\x12\x15\n\rhostingstatus\x18\x03 \x03(\x05\"`\n\x0e\x43opyStatusInfo\x12\x0e\n\x06\x63opyid\x18\x01 \x02(\x05\x12\x12\n\ndifficulty\x18\x02 \x02(\x05\x12\x13\n\x0b\x66ightstatus\x18\x03 \x02(\x05\x12\x15\n\rhostingstatus\x18\x04 \x02(\x05\"2\n\x0cTeamCopyInfo\x12\x0e\n\x06\x63opyid\x18\x01 \x01(\x05\x12\x12\n\ndifficulty\x18\x02 \x01(\x05\"D\n\x11\x43hallengeOpponent\x12\x0e\n\x06unitid\x18\x01 \x01(\t\x12\x10\n\x08rolename\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x05\"1\n\x11HostingItemReward\x12\x0e\n\x06itemid\x18\x01 \x02(\r\x12\x0c\n\x04nums\x18\x02 \x02(\r*B\n\tFightMode\x12\x15\n\x11\x65\x46ightMode_Single\x10\x01\x12\x1e\n\x1a\x65\x46ightMode_Synchronization\x10\x02*@\n\rChallengeType\x12\x15\n\x11\x65\x43hallengeType_PK\x10\x01\x12\x18\n\x14\x65\x43hallengeType_Arena\x10\x02')

_FIGHTMODE = _descriptor.EnumDescriptor(
  name='FightMode',
  full_name='msg.scene.FightMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='eFightMode_Single', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='eFightMode_Synchronization', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1603,
  serialized_end=1669,
)

FightMode = enum_type_wrapper.EnumTypeWrapper(_FIGHTMODE)
_CHALLENGETYPE = _descriptor.EnumDescriptor(
  name='ChallengeType',
  full_name='msg.scene.ChallengeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='eChallengeType_PK', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='eChallengeType_Arena', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1671,
  serialized_end=1735,
)

ChallengeType = enum_type_wrapper.EnumTypeWrapper(_CHALLENGETYPE)
eFightMode_Single = 1
eFightMode_Synchronization = 2
eChallengeType_PK = 1
eChallengeType_Arena = 2



_UNITAVATAR = _descriptor.Descriptor(
  name='UnitAvatar',
  full_name='msg.scene.UnitAvatar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dress', full_name='msg.scene.UnitAvatar.dress', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wing', full_name='msg.scene.UnitAvatar.wing', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trump', full_name='msg.scene.UnitAvatar.trump', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='msg.scene.UnitAvatar.title', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_end=101,
)


_SCENEUNITINFO = _descriptor.Descriptor(
  name='SceneUnitInfo',
  full_name='msg.scene.SceneUnitInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unitid', full_name='msg.scene.SceneUnitInfo.unitid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rolename', full_name='msg.scene.SceneUnitInfo.rolename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='msg.scene.SceneUnitInfo.avatar', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_x', full_name='msg.scene.SceneUnitInfo.pos_x', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_y', full_name='msg.scene.SceneUnitInfo.pos_y', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=103,
  serialized_end=221,
)


_FIGHTSPELL = _descriptor.Descriptor(
  name='FightSpell',
  full_name='msg.scene.FightSpell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spell', full_name='msg.scene.FightSpell.spell', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='msg.scene.FightSpell.power', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='truedam', full_name='msg.scene.FightSpell.truedam', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buffid', full_name='msg.scene.FightSpell.buffid', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=223,
  serialized_end=298,
)


_FIGHTTRUMP = _descriptor.Descriptor(
  name='FightTrump',
  full_name='msg.scene.FightTrump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trumpid', full_name='msg.scene.FightTrump.trumpid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='msg.scene.FightTrump.power', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='truedam', full_name='msg.scene.FightTrump.truedam', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buffid', full_name='msg.scene.FightTrump.buffid', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=300,
  serialized_end=377,
)


_FIGHTFACTOR = _descriptor.Descriptor(
  name='FightFactor',
  full_name='msg.scene.FightFactor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lv', full_name='msg.scene.FightFactor.lv', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp', full_name='msg.scene.FightFactor.hp', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxhp', full_name='msg.scene.FightFactor.maxhp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phyatk', full_name='msg.scene.FightFactor.phyatk', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phydef', full_name='msg.scene.FightFactor.phydef', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magatk', full_name='msg.scene.FightFactor.magatk', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magdef', full_name='msg.scene.FightFactor.magdef', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crit', full_name='msg.scene.FightFactor.crit', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resist', full_name='msg.scene.FightFactor.resist', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='critmultiple', full_name='msg.scene.FightFactor.critmultiple', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='truedef', full_name='msg.scene.FightFactor.truedef', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eleatk', full_name='msg.scene.FightFactor.eleatk', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eletype', full_name='msg.scene.FightFactor.eletype', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metaldef', full_name='msg.scene.FightFactor.metaldef', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wooddef', full_name='msg.scene.FightFactor.wooddef', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='waterdef', full_name='msg.scene.FightFactor.waterdef', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firedef', full_name='msg.scene.FightFactor.firedef', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='earthdef', full_name='msg.scene.FightFactor.earthdef', index=17,
      number=18, type=5, cpp_type=1, label=1,
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
  serialized_start=380,
  serialized_end=686,
)


_FIGHTSOLDIER = _descriptor.Descriptor(
  name='FightSoldier',
  full_name='msg.scene.FightSoldier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unitid', full_name='msg.scene.FightSoldier.unitid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soldier', full_name='msg.scene.FightSoldier.soldier', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factor', full_name='msg.scene.FightSoldier.factor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spells', full_name='msg.scene.FightSoldier.spells', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=688,
  serialized_end=814,
)


_COPYUNITINFO = _descriptor.Descriptor(
  name='CopyUnitInfo',
  full_name='msg.scene.CopyUnitInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unitid', full_name='msg.scene.CopyUnitInfo.unitid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rolename', full_name='msg.scene.CopyUnitInfo.rolename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soldier', full_name='msg.scene.CopyUnitInfo.soldier', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dress', full_name='msg.scene.CopyUnitInfo.dress', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='msg.scene.CopyUnitInfo.title', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed', full_name='msg.scene.CopyUnitInfo.seed', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factor', full_name='msg.scene.CopyUnitInfo.factor', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trump', full_name='msg.scene.CopyUnitInfo.trump', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spells', full_name='msg.scene.CopyUnitInfo.spells', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soldiers', full_name='msg.scene.CopyUnitInfo.soldiers', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=817,
  serialized_end=1086,
)


_SUPPLYINFO = _descriptor.Descriptor(
  name='SupplyInfo',
  full_name='msg.scene.SupplyInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='supplyid', full_name='msg.scene.SupplyInfo.supplyid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='msg.scene.SupplyInfo.position', index=1,
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
  serialized_start=1088,
  serialized_end=1136,
)


_PKCOPYUNITINFO = _descriptor.Descriptor(
  name='PkCopyUnitInfo',
  full_name='msg.scene.PkCopyUnitInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unitid', full_name='msg.scene.PkCopyUnitInfo.unitid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rolename', full_name='msg.scene.PkCopyUnitInfo.rolename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soldier', full_name='msg.scene.PkCopyUnitInfo.soldier', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='msg.scene.PkCopyUnitInfo.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='viplevel', full_name='msg.scene.PkCopyUnitInfo.viplevel', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bp', full_name='msg.scene.PkCopyUnitInfo.bp', index=5,
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
  serialized_start=1138,
  serialized_end=1250,
)


_COPYPROGRESSINFO = _descriptor.Descriptor(
  name='CopyProgressInfo',
  full_name='msg.scene.CopyProgressInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='copyid', full_name='msg.scene.CopyProgressInfo.copyid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fightstatus', full_name='msg.scene.CopyProgressInfo.fightstatus', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hostingstatus', full_name='msg.scene.CopyProgressInfo.hostingstatus', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1252,
  serialized_end=1330,
)


_COPYSTATUSINFO = _descriptor.Descriptor(
  name='CopyStatusInfo',
  full_name='msg.scene.CopyStatusInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='copyid', full_name='msg.scene.CopyStatusInfo.copyid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='difficulty', full_name='msg.scene.CopyStatusInfo.difficulty', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fightstatus', full_name='msg.scene.CopyStatusInfo.fightstatus', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hostingstatus', full_name='msg.scene.CopyStatusInfo.hostingstatus', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=1332,
  serialized_end=1428,
)


_TEAMCOPYINFO = _descriptor.Descriptor(
  name='TeamCopyInfo',
  full_name='msg.scene.TeamCopyInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='copyid', full_name='msg.scene.TeamCopyInfo.copyid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='difficulty', full_name='msg.scene.TeamCopyInfo.difficulty', index=1,
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
  serialized_start=1430,
  serialized_end=1480,
)


_CHALLENGEOPPONENT = _descriptor.Descriptor(
  name='ChallengeOpponent',
  full_name='msg.scene.ChallengeOpponent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unitid', full_name='msg.scene.ChallengeOpponent.unitid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rolename', full_name='msg.scene.ChallengeOpponent.rolename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='msg.scene.ChallengeOpponent.level', index=2,
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
  serialized_start=1482,
  serialized_end=1550,
)


_HOSTINGITEMREWARD = _descriptor.Descriptor(
  name='HostingItemReward',
  full_name='msg.scene.HostingItemReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='itemid', full_name='msg.scene.HostingItemReward.itemid', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nums', full_name='msg.scene.HostingItemReward.nums', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=1552,
  serialized_end=1601,
)

_SCENEUNITINFO.fields_by_name['avatar'].message_type = _UNITAVATAR
_FIGHTSOLDIER.fields_by_name['factor'].message_type = _FIGHTFACTOR
_FIGHTSOLDIER.fields_by_name['spells'].message_type = _FIGHTSPELL
_COPYUNITINFO.fields_by_name['factor'].message_type = _FIGHTFACTOR
_COPYUNITINFO.fields_by_name['trump'].message_type = _FIGHTTRUMP
_COPYUNITINFO.fields_by_name['spells'].message_type = _FIGHTSPELL
_COPYUNITINFO.fields_by_name['soldiers'].message_type = _FIGHTSOLDIER
DESCRIPTOR.message_types_by_name['UnitAvatar'] = _UNITAVATAR
DESCRIPTOR.message_types_by_name['SceneUnitInfo'] = _SCENEUNITINFO
DESCRIPTOR.message_types_by_name['FightSpell'] = _FIGHTSPELL
DESCRIPTOR.message_types_by_name['FightTrump'] = _FIGHTTRUMP
DESCRIPTOR.message_types_by_name['FightFactor'] = _FIGHTFACTOR
DESCRIPTOR.message_types_by_name['FightSoldier'] = _FIGHTSOLDIER
DESCRIPTOR.message_types_by_name['CopyUnitInfo'] = _COPYUNITINFO
DESCRIPTOR.message_types_by_name['SupplyInfo'] = _SUPPLYINFO
DESCRIPTOR.message_types_by_name['PkCopyUnitInfo'] = _PKCOPYUNITINFO
DESCRIPTOR.message_types_by_name['CopyProgressInfo'] = _COPYPROGRESSINFO
DESCRIPTOR.message_types_by_name['CopyStatusInfo'] = _COPYSTATUSINFO
DESCRIPTOR.message_types_by_name['TeamCopyInfo'] = _TEAMCOPYINFO
DESCRIPTOR.message_types_by_name['ChallengeOpponent'] = _CHALLENGEOPPONENT
DESCRIPTOR.message_types_by_name['HostingItemReward'] = _HOSTINGITEMREWARD

class UnitAvatar(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNITAVATAR

  # @@protoc_insertion_point(class_scope:msg.scene.UnitAvatar)

class SceneUnitInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SCENEUNITINFO

  # @@protoc_insertion_point(class_scope:msg.scene.SceneUnitInfo)

class FightSpell(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIGHTSPELL

  # @@protoc_insertion_point(class_scope:msg.scene.FightSpell)

class FightTrump(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIGHTTRUMP

  # @@protoc_insertion_point(class_scope:msg.scene.FightTrump)

class FightFactor(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIGHTFACTOR

  # @@protoc_insertion_point(class_scope:msg.scene.FightFactor)

class FightSoldier(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIGHTSOLDIER

  # @@protoc_insertion_point(class_scope:msg.scene.FightSoldier)

class CopyUnitInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COPYUNITINFO

  # @@protoc_insertion_point(class_scope:msg.scene.CopyUnitInfo)

class SupplyInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUPPLYINFO

  # @@protoc_insertion_point(class_scope:msg.scene.SupplyInfo)

class PkCopyUnitInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PKCOPYUNITINFO

  # @@protoc_insertion_point(class_scope:msg.scene.PkCopyUnitInfo)

class CopyProgressInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COPYPROGRESSINFO

  # @@protoc_insertion_point(class_scope:msg.scene.CopyProgressInfo)

class CopyStatusInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COPYSTATUSINFO

  # @@protoc_insertion_point(class_scope:msg.scene.CopyStatusInfo)

class TeamCopyInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TEAMCOPYINFO

  # @@protoc_insertion_point(class_scope:msg.scene.TeamCopyInfo)

class ChallengeOpponent(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHALLENGEOPPONENT

  # @@protoc_insertion_point(class_scope:msg.scene.ChallengeOpponent)

class HostingItemReward(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HOSTINGITEMREWARD

  # @@protoc_insertion_point(class_scope:msg.scene.HostingItemReward)


# @@protoc_insertion_point(module_scope)
