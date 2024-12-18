# gnmi-pb

This project was created to provide an easily installable python package
of the GNMI protobuffer module (gnmi_pb).

This is **not** an official build. For the official GNMI sources, see:

https://github.com/openconfig/gnmi

## Installation & usage

Install from pypi, e.g.:

```
pip install gnmi_pb
```

Import the gnmi protobuf submodules from the `gnmi_pb` module:

```
>>> from gnmi_pb import gnmi_pb2, gnmi_pb2_grpc

>>> gnmi_pb2.GetRequest(...)
```

## Note about versions

Our release version numbers follow the official GNMI versions but add a 4th number that reflects build-related changes.

This project aims to build from .proto files as close as possible to the original ones, but some changes may be required to fix build issues.

When the official proto sources are modified, it is mentioned it in the Changelog below.

# Changelog

## 0.11.0.1 2024-12-18

### Added
- protos from official GNMI v0.11.0 . Modified imports ([50e1d47](https://github.com/iPronics/gnmi-pb/commit/50e1d473bc14a4fb218db51bb7dd1594987c61a9))
- project skeleton and metadata
- `build.sh` for automated generation of python and type files and distribution creation
- CI workflow for publishing python distribution in PyPI
