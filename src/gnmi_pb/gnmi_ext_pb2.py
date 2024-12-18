"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'gnmi_ext.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egnmi_ext.proto\x12\x08gnmi_ext\x1a\x1egoogle/protobuf/duration.proto"\xf2\x01\n\tExtension\x127\n\x0eregistered_ext\x18\x01 \x01(\x0b2\x1d.gnmi_ext.RegisteredExtensionH\x00\x129\n\x12master_arbitration\x18\x02 \x01(\x0b2\x1b.gnmi_ext.MasterArbitrationH\x00\x12$\n\x07history\x18\x03 \x01(\x0b2\x11.gnmi_ext.HistoryH\x00\x12"\n\x06commit\x18\x04 \x01(\x0b2\x10.gnmi_ext.CommitH\x00\x12 \n\x05depth\x18\x05 \x01(\x0b2\x0f.gnmi_ext.DepthH\x00B\x05\n\x03ext"E\n\x13RegisteredExtension\x12!\n\x02id\x18\x01 \x01(\x0e2\x15.gnmi_ext.ExtensionID\x12\x0b\n\x03msg\x18\x02 \x01(\x0c"Y\n\x11MasterArbitration\x12\x1c\n\x04role\x18\x01 \x01(\x0b2\x0e.gnmi_ext.Role\x12&\n\x0belection_id\x18\x02 \x01(\x0b2\x11.gnmi_ext.Uint128"$\n\x07Uint128\x12\x0c\n\x04high\x18\x01 \x01(\x04\x12\x0b\n\x03low\x18\x02 \x01(\x04"\x12\n\x04Role\x12\n\n\x02id\x18\x01 \x01(\t"S\n\x07History\x12\x17\n\rsnapshot_time\x18\x01 \x01(\x03H\x00\x12$\n\x05range\x18\x02 \x01(\x0b2\x13.gnmi_ext.TimeRangeH\x00B\t\n\x07request"\'\n\tTimeRange\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03end\x18\x02 \x01(\x03"\xe5\x01\n\x06Commit\x12\n\n\x02id\x18\x01 \x01(\t\x12)\n\x06commit\x18\x02 \x01(\x0b2\x17.gnmi_ext.CommitRequestH\x00\x12*\n\x07confirm\x18\x03 \x01(\x0b2\x17.gnmi_ext.CommitConfirmH\x00\x12(\n\x06cancel\x18\x04 \x01(\x0b2\x16.gnmi_ext.CommitCancelH\x00\x12D\n\x15set_rollback_duration\x18\x05 \x01(\x0b2#.gnmi_ext.CommitSetRollbackDurationH\x00B\x08\n\x06action"E\n\rCommitRequest\x124\n\x11rollback_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration"\x0f\n\rCommitConfirm"\x0e\n\x0cCommitCancel"Q\n\x19CommitSetRollbackDuration\x124\n\x11rollback_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration"\x16\n\x05Depth\x12\r\n\x05level\x18\x01 \x01(\r*3\n\x0bExtensionID\x12\r\n\tEID_UNSET\x10\x00\x12\x15\n\x10EID_EXPERIMENTAL\x10\xe7\x07B+Z)github.com/openconfig/gnmi/proto/gnmi_extb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gnmi_ext_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/openconfig/gnmi/proto/gnmi_ext'
    _globals['_EXTENSIONID']._serialized_start = 1094
    _globals['_EXTENSIONID']._serialized_end = 1145
    _globals['_EXTENSION']._serialized_start = 61
    _globals['_EXTENSION']._serialized_end = 303
    _globals['_REGISTEREDEXTENSION']._serialized_start = 305
    _globals['_REGISTEREDEXTENSION']._serialized_end = 374
    _globals['_MASTERARBITRATION']._serialized_start = 376
    _globals['_MASTERARBITRATION']._serialized_end = 465
    _globals['_UINT128']._serialized_start = 467
    _globals['_UINT128']._serialized_end = 503
    _globals['_ROLE']._serialized_start = 505
    _globals['_ROLE']._serialized_end = 523
    _globals['_HISTORY']._serialized_start = 525
    _globals['_HISTORY']._serialized_end = 608
    _globals['_TIMERANGE']._serialized_start = 610
    _globals['_TIMERANGE']._serialized_end = 649
    _globals['_COMMIT']._serialized_start = 652
    _globals['_COMMIT']._serialized_end = 881
    _globals['_COMMITREQUEST']._serialized_start = 883
    _globals['_COMMITREQUEST']._serialized_end = 952
    _globals['_COMMITCONFIRM']._serialized_start = 954
    _globals['_COMMITCONFIRM']._serialized_end = 969
    _globals['_COMMITCANCEL']._serialized_start = 971
    _globals['_COMMITCANCEL']._serialized_end = 985
    _globals['_COMMITSETROLLBACKDURATION']._serialized_start = 987
    _globals['_COMMITSETROLLBACKDURATION']._serialized_end = 1068
    _globals['_DEPTH']._serialized_start = 1070
    _globals['_DEPTH']._serialized_end = 1092