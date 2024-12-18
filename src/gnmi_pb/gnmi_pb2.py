"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'gnmi.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from . import gnmi_ext_pb2 as gnmi__ext__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngnmi.proto\x12\x04gnmi\x1a\x19google/protobuf/any.proto\x1a google/protobuf/descriptor.proto\x1a\x0egnmi_ext.proto"\x94\x01\n\x0cNotification\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x1a\n\x06prefix\x18\x02 \x01(\x0b2\n.gnmi.Path\x12\x1c\n\x06update\x18\x04 \x03(\x0b2\x0c.gnmi.Update\x12\x1a\n\x06delete\x18\x05 \x03(\x0b2\n.gnmi.Path\x12\x0e\n\x06atomic\x18\x06 \x01(\x08J\x04\x08\x03\x10\x04R\x05alias"u\n\x06Update\x12\x18\n\x04path\x18\x01 \x01(\x0b2\n.gnmi.Path\x12\x1e\n\x05value\x18\x02 \x01(\x0b2\x0b.gnmi.ValueB\x02\x18\x01\x12\x1d\n\x03val\x18\x03 \x01(\x0b2\x10.gnmi.TypedValue\x12\x12\n\nduplicates\x18\x04 \x01(\r"\x83\x03\n\nTypedValue\x12\x14\n\nstring_val\x18\x01 \x01(\tH\x00\x12\x11\n\x07int_val\x18\x02 \x01(\x03H\x00\x12\x12\n\x08uint_val\x18\x03 \x01(\x04H\x00\x12\x12\n\x08bool_val\x18\x04 \x01(\x08H\x00\x12\x13\n\tbytes_val\x18\x05 \x01(\x0cH\x00\x12\x17\n\tfloat_val\x18\x06 \x01(\x02B\x02\x18\x01H\x00\x12\x14\n\ndouble_val\x18\x0e \x01(\x01H\x00\x12*\n\x0bdecimal_val\x18\x07 \x01(\x0b2\x0f.gnmi.Decimal64B\x02\x18\x01H\x00\x12)\n\x0cleaflist_val\x18\x08 \x01(\x0b2\x11.gnmi.ScalarArrayH\x00\x12\'\n\x07any_val\x18\t \x01(\x0b2\x14.google.protobuf.AnyH\x00\x12\x12\n\x08json_val\x18\n \x01(\x0cH\x00\x12\x17\n\rjson_ietf_val\x18\x0b \x01(\x0cH\x00\x12\x13\n\tascii_val\x18\x0c \x01(\tH\x00\x12\x15\n\x0bproto_bytes\x18\r \x01(\x0cH\x00B\x07\n\x05value"Y\n\x04Path\x12\x13\n\x07element\x18\x01 \x03(\tB\x02\x18\x01\x12\x0e\n\x06origin\x18\x02 \x01(\t\x12\x1c\n\x04elem\x18\x03 \x03(\x0b2\x0e.gnmi.PathElem\x12\x0e\n\x06target\x18\x04 \x01(\t"j\n\x08PathElem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x03key\x18\x02 \x03(\x0b2\x17.gnmi.PathElem.KeyEntry\x1a*\n\x08KeyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"8\n\x05Value\x12\r\n\x05value\x18\x01 \x01(\x0c\x12\x1c\n\x04type\x18\x02 \x01(\x0e2\x0e.gnmi.Encoding:\x02\x18\x01"N\n\x05Error\x12\x0c\n\x04code\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\x12"\n\x04data\x18\x03 \x01(\x0b2\x14.google.protobuf.Any:\x02\x18\x01"2\n\tDecimal64\x12\x0e\n\x06digits\x18\x01 \x01(\x03\x12\x11\n\tprecision\x18\x02 \x01(\r:\x02\x18\x01"0\n\x0bScalarArray\x12!\n\x07element\x18\x01 \x03(\x0b2\x10.gnmi.TypedValue"\x9d\x01\n\x10SubscribeRequest\x12+\n\tsubscribe\x18\x01 \x01(\x0b2\x16.gnmi.SubscriptionListH\x00\x12\x1a\n\x04poll\x18\x03 \x01(\x0b2\n.gnmi.PollH\x00\x12&\n\textension\x18\x05 \x03(\x0b2\x13.gnmi_ext.ExtensionB\t\n\x07requestJ\x04\x08\x04\x10\x05R\x07aliases"\x06\n\x04Poll"\xa8\x01\n\x11SubscribeResponse\x12$\n\x06update\x18\x01 \x01(\x0b2\x12.gnmi.NotificationH\x00\x12\x17\n\rsync_response\x18\x03 \x01(\x08H\x00\x12 \n\x05error\x18\x04 \x01(\x0b2\x0b.gnmi.ErrorB\x02\x18\x01H\x00\x12&\n\textension\x18\x05 \x03(\x0b2\x13.gnmi_ext.ExtensionB\n\n\x08response"\xd5\x02\n\x10SubscriptionList\x12\x1a\n\x06prefix\x18\x01 \x01(\x0b2\n.gnmi.Path\x12(\n\x0csubscription\x18\x02 \x03(\x0b2\x12.gnmi.Subscription\x12\x1d\n\x03qos\x18\x04 \x01(\x0b2\x10.gnmi.QOSMarking\x12)\n\x04mode\x18\x05 \x01(\x0e2\x1b.gnmi.SubscriptionList.Mode\x12\x19\n\x11allow_aggregation\x18\x06 \x01(\x08\x12#\n\nuse_models\x18\x07 \x03(\x0b2\x0f.gnmi.ModelData\x12 \n\x08encoding\x18\x08 \x01(\x0e2\x0e.gnmi.Encoding\x12\x14\n\x0cupdates_only\x18\t \x01(\x08"&\n\x04Mode\x12\n\n\x06STREAM\x10\x00\x12\x08\n\x04ONCE\x10\x01\x12\x08\n\x04POLL\x10\x02J\x04\x08\x03\x10\x04R\x0buse_aliases"\x9f\x01\n\x0cSubscription\x12\x18\n\x04path\x18\x01 \x01(\x0b2\n.gnmi.Path\x12$\n\x04mode\x18\x02 \x01(\x0e2\x16.gnmi.SubscriptionMode\x12\x17\n\x0fsample_interval\x18\x03 \x01(\x04\x12\x1a\n\x12suppress_redundant\x18\x04 \x01(\x08\x12\x1a\n\x12heartbeat_interval\x18\x05 \x01(\x04"\x1d\n\nQOSMarking\x12\x0f\n\x07marking\x18\x01 \x01(\r"\xce\x01\n\nSetRequest\x12\x1a\n\x06prefix\x18\x01 \x01(\x0b2\n.gnmi.Path\x12\x1a\n\x06delete\x18\x02 \x03(\x0b2\n.gnmi.Path\x12\x1d\n\x07replace\x18\x03 \x03(\x0b2\x0c.gnmi.Update\x12\x1c\n\x06update\x18\x04 \x03(\x0b2\x0c.gnmi.Update\x12#\n\runion_replace\x18\x06 \x03(\x0b2\x0c.gnmi.Update\x12&\n\textension\x18\x05 \x03(\x0b2\x13.gnmi_ext.Extension"\xac\x01\n\x0bSetResponse\x12\x1a\n\x06prefix\x18\x01 \x01(\x0b2\n.gnmi.Path\x12$\n\x08response\x18\x02 \x03(\x0b2\x12.gnmi.UpdateResult\x12 \n\x07message\x18\x03 \x01(\x0b2\x0b.gnmi.ErrorB\x02\x18\x01\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x12&\n\textension\x18\x05 \x03(\x0b2\x13.gnmi_ext.Extension"\xdd\x01\n\x0cUpdateResult\x12\x15\n\ttimestamp\x18\x01 \x01(\x03B\x02\x18\x01\x12\x18\n\x04path\x18\x02 \x01(\x0b2\n.gnmi.Path\x12 \n\x07message\x18\x03 \x01(\x0b2\x0b.gnmi.ErrorB\x02\x18\x01\x12(\n\x02op\x18\x04 \x01(\x0e2\x1c.gnmi.UpdateResult.Operation"P\n\tOperation\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06DELETE\x10\x01\x12\x0b\n\x07REPLACE\x10\x02\x12\n\n\x06UPDATE\x10\x03\x12\x11\n\rUNION_REPLACE\x10\x04"\x97\x02\n\nGetRequest\x12\x1a\n\x06prefix\x18\x01 \x01(\x0b2\n.gnmi.Path\x12\x18\n\x04path\x18\x02 \x03(\x0b2\n.gnmi.Path\x12\'\n\x04type\x18\x03 \x01(\x0e2\x19.gnmi.GetRequest.DataType\x12 \n\x08encoding\x18\x05 \x01(\x0e2\x0e.gnmi.Encoding\x12#\n\nuse_models\x18\x06 \x03(\x0b2\x0f.gnmi.ModelData\x12&\n\textension\x18\x07 \x03(\x0b2\x13.gnmi_ext.Extension";\n\x08DataType\x12\x07\n\x03ALL\x10\x00\x12\n\n\x06CONFIG\x10\x01\x12\t\n\x05STATE\x10\x02\x12\x0f\n\x0bOPERATIONAL\x10\x03"\x7f\n\x0bGetResponse\x12(\n\x0cnotification\x18\x01 \x03(\x0b2\x12.gnmi.Notification\x12\x1e\n\x05error\x18\x02 \x01(\x0b2\x0b.gnmi.ErrorB\x02\x18\x01\x12&\n\textension\x18\x03 \x03(\x0b2\x13.gnmi_ext.Extension";\n\x11CapabilityRequest\x12&\n\textension\x18\x01 \x03(\x0b2\x13.gnmi_ext.Extension"\xaa\x01\n\x12CapabilityResponse\x12)\n\x10supported_models\x18\x01 \x03(\x0b2\x0f.gnmi.ModelData\x12+\n\x13supported_encodings\x18\x02 \x03(\x0e2\x0e.gnmi.Encoding\x12\x14\n\x0cgNMI_version\x18\x03 \x01(\t\x12&\n\textension\x18\x04 \x03(\x0b2\x13.gnmi_ext.Extension"@\n\tModelData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0corganization\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t*D\n\x08Encoding\x12\x08\n\x04JSON\x10\x00\x12\t\n\x05BYTES\x10\x01\x12\t\n\x05PROTO\x10\x02\x12\t\n\x05ASCII\x10\x03\x12\r\n\tJSON_IETF\x10\x04*A\n\x10SubscriptionMode\x12\x12\n\x0eTARGET_DEFINED\x10\x00\x12\r\n\tON_CHANGE\x10\x01\x12\n\n\x06SAMPLE\x10\x022\xe3\x01\n\x04gNMI\x12A\n\x0cCapabilities\x12\x17.gnmi.CapabilityRequest\x1a\x18.gnmi.CapabilityResponse\x12*\n\x03Get\x12\x10.gnmi.GetRequest\x1a\x11.gnmi.GetResponse\x12*\n\x03Set\x12\x10.gnmi.SetRequest\x1a\x11.gnmi.SetResponse\x12@\n\tSubscribe\x12\x16.gnmi.SubscribeRequest\x1a\x17.gnmi.SubscribeResponse(\x010\x01:3\n\x0cgnmi_service\x12\x1c.google.protobuf.FileOptions\x18\xe9\x07 \x01(\tBT\n\x15com.github.gnmi.protoB\tGnmiProtoP\x01Z%github.com/openconfig/gnmi/proto/gnmi\xca>\x060.10.0b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gnmi_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.github.gnmi.protoB\tGnmiProtoP\x01Z%github.com/openconfig/gnmi/proto/gnmi\xca>\x060.10.0'
    _globals['_UPDATE'].fields_by_name['value']._loaded_options = None
    _globals['_UPDATE'].fields_by_name['value']._serialized_options = b'\x18\x01'
    _globals['_TYPEDVALUE'].fields_by_name['float_val']._loaded_options = None
    _globals['_TYPEDVALUE'].fields_by_name['float_val']._serialized_options = b'\x18\x01'
    _globals['_TYPEDVALUE'].fields_by_name['decimal_val']._loaded_options = None
    _globals['_TYPEDVALUE'].fields_by_name['decimal_val']._serialized_options = b'\x18\x01'
    _globals['_PATH'].fields_by_name['element']._loaded_options = None
    _globals['_PATH'].fields_by_name['element']._serialized_options = b'\x18\x01'
    _globals['_PATHELEM_KEYENTRY']._loaded_options = None
    _globals['_PATHELEM_KEYENTRY']._serialized_options = b'8\x01'
    _globals['_VALUE']._loaded_options = None
    _globals['_VALUE']._serialized_options = b'\x18\x01'
    _globals['_ERROR']._loaded_options = None
    _globals['_ERROR']._serialized_options = b'\x18\x01'
    _globals['_DECIMAL64']._loaded_options = None
    _globals['_DECIMAL64']._serialized_options = b'\x18\x01'
    _globals['_SUBSCRIBERESPONSE'].fields_by_name['error']._loaded_options = None
    _globals['_SUBSCRIBERESPONSE'].fields_by_name['error']._serialized_options = b'\x18\x01'
    _globals['_SETRESPONSE'].fields_by_name['message']._loaded_options = None
    _globals['_SETRESPONSE'].fields_by_name['message']._serialized_options = b'\x18\x01'
    _globals['_UPDATERESULT'].fields_by_name['timestamp']._loaded_options = None
    _globals['_UPDATERESULT'].fields_by_name['timestamp']._serialized_options = b'\x18\x01'
    _globals['_UPDATERESULT'].fields_by_name['message']._loaded_options = None
    _globals['_UPDATERESULT'].fields_by_name['message']._serialized_options = b'\x18\x01'
    _globals['_GETRESPONSE'].fields_by_name['error']._loaded_options = None
    _globals['_GETRESPONSE'].fields_by_name['error']._serialized_options = b'\x18\x01'
    _globals['_ENCODING']._serialized_start = 3391
    _globals['_ENCODING']._serialized_end = 3459
    _globals['_SUBSCRIPTIONMODE']._serialized_start = 3461
    _globals['_SUBSCRIPTIONMODE']._serialized_end = 3526
    _globals['_NOTIFICATION']._serialized_start = 98
    _globals['_NOTIFICATION']._serialized_end = 246
    _globals['_UPDATE']._serialized_start = 248
    _globals['_UPDATE']._serialized_end = 365
    _globals['_TYPEDVALUE']._serialized_start = 368
    _globals['_TYPEDVALUE']._serialized_end = 755
    _globals['_PATH']._serialized_start = 757
    _globals['_PATH']._serialized_end = 846
    _globals['_PATHELEM']._serialized_start = 848
    _globals['_PATHELEM']._serialized_end = 954
    _globals['_PATHELEM_KEYENTRY']._serialized_start = 912
    _globals['_PATHELEM_KEYENTRY']._serialized_end = 954
    _globals['_VALUE']._serialized_start = 956
    _globals['_VALUE']._serialized_end = 1012
    _globals['_ERROR']._serialized_start = 1014
    _globals['_ERROR']._serialized_end = 1092
    _globals['_DECIMAL64']._serialized_start = 1094
    _globals['_DECIMAL64']._serialized_end = 1144
    _globals['_SCALARARRAY']._serialized_start = 1146
    _globals['_SCALARARRAY']._serialized_end = 1194
    _globals['_SUBSCRIBEREQUEST']._serialized_start = 1197
    _globals['_SUBSCRIBEREQUEST']._serialized_end = 1354
    _globals['_POLL']._serialized_start = 1356
    _globals['_POLL']._serialized_end = 1362
    _globals['_SUBSCRIBERESPONSE']._serialized_start = 1365
    _globals['_SUBSCRIBERESPONSE']._serialized_end = 1533
    _globals['_SUBSCRIPTIONLIST']._serialized_start = 1536
    _globals['_SUBSCRIPTIONLIST']._serialized_end = 1877
    _globals['_SUBSCRIPTIONLIST_MODE']._serialized_start = 1820
    _globals['_SUBSCRIPTIONLIST_MODE']._serialized_end = 1858
    _globals['_SUBSCRIPTION']._serialized_start = 1880
    _globals['_SUBSCRIPTION']._serialized_end = 2039
    _globals['_QOSMARKING']._serialized_start = 2041
    _globals['_QOSMARKING']._serialized_end = 2070
    _globals['_SETREQUEST']._serialized_start = 2073
    _globals['_SETREQUEST']._serialized_end = 2279
    _globals['_SETRESPONSE']._serialized_start = 2282
    _globals['_SETRESPONSE']._serialized_end = 2454
    _globals['_UPDATERESULT']._serialized_start = 2457
    _globals['_UPDATERESULT']._serialized_end = 2678
    _globals['_UPDATERESULT_OPERATION']._serialized_start = 2598
    _globals['_UPDATERESULT_OPERATION']._serialized_end = 2678
    _globals['_GETREQUEST']._serialized_start = 2681
    _globals['_GETREQUEST']._serialized_end = 2960
    _globals['_GETREQUEST_DATATYPE']._serialized_start = 2901
    _globals['_GETREQUEST_DATATYPE']._serialized_end = 2960
    _globals['_GETRESPONSE']._serialized_start = 2962
    _globals['_GETRESPONSE']._serialized_end = 3089
    _globals['_CAPABILITYREQUEST']._serialized_start = 3091
    _globals['_CAPABILITYREQUEST']._serialized_end = 3150
    _globals['_CAPABILITYRESPONSE']._serialized_start = 3153
    _globals['_CAPABILITYRESPONSE']._serialized_end = 3323
    _globals['_MODELDATA']._serialized_start = 3325
    _globals['_MODELDATA']._serialized_end = 3389
    _globals['_GNMI']._serialized_start = 3529
    _globals['_GNMI']._serialized_end = 3756