# source: Simlog.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Simlog.proto',
  package='Ets2SdkClient.Demo',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0cSimlog.proto\x12\x12\x45ts2SdkClient.Demo\">\n\x06Simlog\x12\x34\n\x04info\x18\x01 \x03(\x0b\x32&.Ets2SdkClient.Demo.DrivingInformation\"\xf9\x01\n\x12\x44rivingInformation\x12\x11\n\ttimestamp\x18\x01 \x02(\t\x12\x12\n\ninGameTime\x18\x02 \x02(\r\x12\x32\n\ndrivetrain\x18\x03 \x02(\x0b\x32\x1e.Ets2SdkClient.Demo.Drivetrain\x12,\n\x07physics\x18\x04 \x02(\x0b\x32\x1b.Ets2SdkClient.Demo.Physics\x12.\n\x08\x63ontrols\x18\x05 \x02(\x0b\x32\x1c.Ets2SdkClient.Demo.Controls\x12*\n\x06lights\x18\x06 \x02(\x0b\x32\x1a.Ets2SdkClient.Demo.Lights\"w\n\nDrivetrain\x12\x15\n\rTruckOdometer\x18\x01 \x01(\x02\x12\x15\n\rGearDashboard\x18\x02 \x01(\x02\x12\x11\n\tEngineRpm\x18\x03 \x01(\x02\x12\x0c\n\x04\x46uel\x18\x04 \x01(\x02\x12\x1a\n\x12\x46uelAvgConsumption\x18\x05 \x01(\x02\"\xd8\x01\n\x07Physics\x12\x10\n\x08SpeedKmh\x18\x01 \x01(\x02\x12\x15\n\rAccelerationX\x18\x02 \x01(\x02\x12\x15\n\rAccelerationY\x18\x03 \x01(\x02\x12\x15\n\rAccelerationZ\x18\x04 \x01(\x02\x12\x13\n\x0b\x43oordinateX\x18\x05 \x01(\x02\x12\x13\n\x0b\x43oordinateY\x18\x06 \x01(\x02\x12\x13\n\x0b\x43oordinateZ\x18\x07 \x01(\x02\x12\x11\n\tRotationX\x18\x08 \x01(\x02\x12\x11\n\tRotationY\x18\t \x01(\x02\x12\x11\n\tRotationZ\x18\n \x01(\x02\"Z\n\x08\x43ontrols\x12\x11\n\tUserSteer\x18\x01 \x01(\x02\x12\x14\n\x0cUserThrottle\x18\x02 \x01(\x02\x12\x11\n\tUserBrake\x18\x03 \x01(\x02\x12\x12\n\nUserClutch\x18\x04 \x01(\x02\"7\n\x06Lights\x12\x15\n\rBlinkerLeftOn\x18\x01 \x01(\x02\x12\x16\n\x0e\x42linkerRightOn\x18\x02 \x01(\x02\"\x08\n\x06\x44\x61mage')
)




_SIMLOG = _descriptor.Descriptor(
  name='Simlog',
  full_name='Ets2SdkClient.Demo.Simlog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='Ets2SdkClient.Demo.Simlog.info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=98,
)


_DRIVINGINFORMATION = _descriptor.Descriptor(
  name='DrivingInformation',
  full_name='Ets2SdkClient.Demo.DrivingInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Ets2SdkClient.Demo.DrivingInformation.timestamp', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inGameTime', full_name='Ets2SdkClient.Demo.DrivingInformation.inGameTime', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drivetrain', full_name='Ets2SdkClient.Demo.DrivingInformation.drivetrain', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='physics', full_name='Ets2SdkClient.Demo.DrivingInformation.physics', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controls', full_name='Ets2SdkClient.Demo.DrivingInformation.controls', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lights', full_name='Ets2SdkClient.Demo.DrivingInformation.lights', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=350,
)


_DRIVETRAIN = _descriptor.Descriptor(
  name='Drivetrain',
  full_name='Ets2SdkClient.Demo.Drivetrain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TruckOdometer', full_name='Ets2SdkClient.Demo.Drivetrain.TruckOdometer', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='GearDashboard', full_name='Ets2SdkClient.Demo.Drivetrain.GearDashboard', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EngineRpm', full_name='Ets2SdkClient.Demo.Drivetrain.EngineRpm', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Fuel', full_name='Ets2SdkClient.Demo.Drivetrain.Fuel', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FuelAvgConsumption', full_name='Ets2SdkClient.Demo.Drivetrain.FuelAvgConsumption', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=471,
)


_PHYSICS = _descriptor.Descriptor(
  name='Physics',
  full_name='Ets2SdkClient.Demo.Physics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SpeedKmh', full_name='Ets2SdkClient.Demo.Physics.SpeedKmh', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='AccelerationX', full_name='Ets2SdkClient.Demo.Physics.AccelerationX', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='AccelerationY', full_name='Ets2SdkClient.Demo.Physics.AccelerationY', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='AccelerationZ', full_name='Ets2SdkClient.Demo.Physics.AccelerationZ', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CoordinateX', full_name='Ets2SdkClient.Demo.Physics.CoordinateX', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CoordinateY', full_name='Ets2SdkClient.Demo.Physics.CoordinateY', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CoordinateZ', full_name='Ets2SdkClient.Demo.Physics.CoordinateZ', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RotationX', full_name='Ets2SdkClient.Demo.Physics.RotationX', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RotationY', full_name='Ets2SdkClient.Demo.Physics.RotationY', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RotationZ', full_name='Ets2SdkClient.Demo.Physics.RotationZ', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=474,
  serialized_end=690,
)


_CONTROLS = _descriptor.Descriptor(
  name='Controls',
  full_name='Ets2SdkClient.Demo.Controls',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='UserSteer', full_name='Ets2SdkClient.Demo.Controls.UserSteer', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='UserThrottle', full_name='Ets2SdkClient.Demo.Controls.UserThrottle', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='UserBrake', full_name='Ets2SdkClient.Demo.Controls.UserBrake', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='UserClutch', full_name='Ets2SdkClient.Demo.Controls.UserClutch', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=692,
  serialized_end=782,
)


_LIGHTS = _descriptor.Descriptor(
  name='Lights',
  full_name='Ets2SdkClient.Demo.Lights',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='BlinkerLeftOn', full_name='Ets2SdkClient.Demo.Lights.BlinkerLeftOn', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BlinkerRightOn', full_name='Ets2SdkClient.Demo.Lights.BlinkerRightOn', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=784,
  serialized_end=839,
)


_DAMAGE = _descriptor.Descriptor(
  name='Damage',
  full_name='Ets2SdkClient.Demo.Damage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=841,
  serialized_end=849,
)

_SIMLOG.fields_by_name['info'].message_type = _DRIVINGINFORMATION
_DRIVINGINFORMATION.fields_by_name['drivetrain'].message_type = _DRIVETRAIN
_DRIVINGINFORMATION.fields_by_name['physics'].message_type = _PHYSICS
_DRIVINGINFORMATION.fields_by_name['controls'].message_type = _CONTROLS
_DRIVINGINFORMATION.fields_by_name['lights'].message_type = _LIGHTS
DESCRIPTOR.message_types_by_name['Simlog'] = _SIMLOG
DESCRIPTOR.message_types_by_name['DrivingInformation'] = _DRIVINGINFORMATION
DESCRIPTOR.message_types_by_name['Drivetrain'] = _DRIVETRAIN
DESCRIPTOR.message_types_by_name['Physics'] = _PHYSICS
DESCRIPTOR.message_types_by_name['Controls'] = _CONTROLS
DESCRIPTOR.message_types_by_name['Lights'] = _LIGHTS
DESCRIPTOR.message_types_by_name['Damage'] = _DAMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Simlog = _reflection.GeneratedProtocolMessageType('Simlog', (_message.Message,), dict(
  DESCRIPTOR = _SIMLOG,
  __module__ = 'Simlog_pb2'
  # @@protoc_insertion_point(class_scope:Ets2SdkClient.Demo.Simlog)
  ))
_sym_db.RegisterMessage(Simlog)

DrivingInformation = _reflection.GeneratedProtocolMessageType('DrivingInformation', (_message.Message,), dict(
  DESCRIPTOR = _DRIVINGINFORMATION,
  __module__ = 'Simlog_pb2'
  # @@protoc_insertion_point(class_scope:Ets2SdkClient.Demo.DrivingInformation)
  ))
_sym_db.RegisterMessage(DrivingInformation)

Drivetrain = _reflection.GeneratedProtocolMessageType('Drivetrain', (_message.Message,), dict(
  DESCRIPTOR = _DRIVETRAIN,
  __module__ = 'Simlog_pb2'
  # @@protoc_insertion_point(class_scope:Ets2SdkClient.Demo.Drivetrain)
  ))
_sym_db.RegisterMessage(Drivetrain)

Physics = _reflection.GeneratedProtocolMessageType('Physics', (_message.Message,), dict(
  DESCRIPTOR = _PHYSICS,
  __module__ = 'Simlog_pb2'
  # @@protoc_insertion_point(class_scope:Ets2SdkClient.Demo.Physics)
  ))
_sym_db.RegisterMessage(Physics)

Controls = _reflection.GeneratedProtocolMessageType('Controls', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLS,
  __module__ = 'Simlog_pb2'
  # @@protoc_insertion_point(class_scope:Ets2SdkClient.Demo.Controls)
  ))
_sym_db.RegisterMessage(Controls)

Lights = _reflection.GeneratedProtocolMessageType('Lights', (_message.Message,), dict(
  DESCRIPTOR = _LIGHTS,
  __module__ = 'Simlog_pb2'
  # @@protoc_insertion_point(class_scope:Ets2SdkClient.Demo.Lights)
  ))
_sym_db.RegisterMessage(Lights)

Damage = _reflection.GeneratedProtocolMessageType('Damage', (_message.Message,), dict(
  DESCRIPTOR = _DAMAGE,
  __module__ = 'Simlog_pb2'
  # @@protoc_insertion_point(class_scope:Ets2SdkClient.Demo.Damage)
  ))
_sym_db.RegisterMessage(Damage)


# @@protoc_insertion_point(module_scope)
