#!/bin/bash

# Define the path to the proto folder
PROTO_DIR="$(pwd)/proto"

# Compile the gNMI proto file to .py and .pyi files
if ! uv run python -m grpc_tools.protoc -I$PROTO_DIR --python_out=$PROTO_DIR --pyi_out=$PROTO_DIR --grpc_python_out=$PROTO_DIR $PROTO_DIR/gnmi.proto;
    then echo "gNMI proto compilation failed"
        exit 1
fi

echo "Compilation completed successfully."