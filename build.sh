#!/bin/bash

# Define the path to the proto folder
ROOT_DIR="$(dirname $0)"
PROTO_DIR="$ROOT_DIR/proto"
SRC_DIR="$ROOT_DIR/src/gnmi_pb"

# Compile the gNMI proto file to .py and .pyi files
uv run python -m grpc_tools.protoc -I$PROTO_DIR --python_out=$SRC_DIR --pyi_out=$SRC_DIR --grpc_python_out=$SRC_DIR gnmi_ext.proto gnmi.proto;
