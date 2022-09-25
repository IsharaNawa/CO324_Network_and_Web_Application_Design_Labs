![Setup Environment and Autograde](../../actions/workflows/workflow.yml/badge.svg)
# CO324 Lab 5: Error Handling, Data Races, and Lost Updates

## Objective
At the end of the lab you should be able to
* Define services and messages using the Protocol Buffers interface definition language.
* Implement gRPC clients and servers.
* Proper input validation and error handling.
* Implement critical sections using mutual exclusion locks for concurrency control.

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
* [Data Races and Race Conditions - with C++ examples](https://www.modernescpp.com/index.php/race-condition-versus-data-race)
* [Data Races vs Race Conditions](https://blog.regehr.org/archives/490)
* [google/protobuf definitions - wrappers](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/wrappers.proto)

## Exercises

Exercises can be found in the `src/` folder.


