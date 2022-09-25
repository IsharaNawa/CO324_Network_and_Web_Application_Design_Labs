![Setup Environment and Autograde](../../actions/workflows/workflow.yml/badge.svg)
# CO324 Lab 4: RPC APIs using GRPC

## Objective
At the end of the lab you should be able to
* Define services and messages using the Protocol Buffers interface definition language.
* Implement gRPC clients and servers.


## Preparation
Install Python version 3.7 or newer on your computer. You may use whichever IDE or editor that you prefer.

1. Follow the instructions given in the [gRPC Python Quickstart](https://www.grpc.io/docs/languages/python/quickstart/) to set up your environment.   Alternatively, you can use the following command (don’t mix the two sets of instructions!)
```bash
pipenv install grpcio grpcio-tools
pipenv shell
```

2. To check your setup download the helloworld.proto file and try compiling it. If everything is properly set up you should see two generated named `helloworld_pb2.py` and `helloworld_pb2_grpc.py`
```bash
python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. helloworld.proto
```

3. Now  run the “hello world” demo following the instructions in the python quickstart.

4. (Optional) Install a [gRPC graphical client](https://github.com/uw-labs/bloomrpc), [VS-Code extension](https://github.com/oslabs-beta/tropicRPC), or the [command-line client](https://github.com/fullstorydev/grpcurl).

## Instructions
* Use **only grpcio and built-in modules** in Python 3 to complete these exercises.
* Put the solutions to coding exercises for the files in `src/` directory.
* **Put your E Number as a comment** in top of each source file.
* **DO NOT** change any code in `test/` directory.


## References
* [Introduction to gRPC](https://grpc.io/docs/what-is-grpc/introduction/)
* [gRPC core concepts](https://grpc.io/docs/what-is-grpc/core-concepts/)
* [Python gRPC generated code reference](https://developers.google.com/protocol-buffers/docs/reference/python-generated)
* [Protocol Buffer v3 User Guide](https://developers.google.com/protocol-buffers/docs/proto3)
* [Context Managers and "with" statement in python](https://dbader.org/blog/python-context-managers-and-with-statement)
* [gRPC python docs](https://grpc.io/docs/languages/python/)


## Exercises

Exercises can be found in the `src/` folder.
