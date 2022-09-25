import sys
sys.path.append('./src/Q1.a.2/')
from lab06_task_server_Q1a2 import *

import logging
from pprint import pformat
from typing import Sequence, Mapping, Tuple
from google.protobuf import (
    any_pb2,
    api_pb2,
    duration_pb2,
    empty_pb2,
    field_mask_pb2,
    source_context_pb2,
    struct_pb2,
    timestamp_pb2,
    type_pb2,
    wrappers_pb2,
)
import random, string, logging
import grpc, tasklist_pb2, tasklist_pb2_grpc

tasks = {}

def random_string_generator(str_size, allowed_chars):
    return "".join(random.choice(allowed_chars) for x in range(str_size))


# Test that will be used to grade addTask
def test_addTask() -> None:
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tasklist_pb2_grpc.TaskapiStub(channel)
        for i in range(10):
            desc = random_string_generator(99, string.ascii_letters)
            response = stub.addTask(wrappers_pb2.StringValue(value=desc))
            assert response.description == desc
            tasks[response.id] = response
        try:
            desc = random_string_generator(2000, string.ascii_letters)
            response = stub.addTask(wrappers_pb2.StringValue(value=desc))
            assert len(response.description) != 2000, f"Modify addTask to add only tasks with description < MAXLEN (=1024)"
        except grpc.RpcError as e:
            assert e.code() != grpc.StatusCode.OK
            assert e.code() == grpc.StatusCode.INVALID_ARGUMENT, f"Validate user input for length < MAXLEN(=1024)"
            assert e.details() != "", f"Set an appropriate error message"


def test_editTask():
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tasklist_pb2_grpc.TaskapiStub(channel)
        existing_id = 0
        for i in range(5):
            desc = random_string_generator(99, string.ascii_letters)
            add_response = stub.addTask(wrappers_pb2.StringValue(value=desc))
            tasks[add_response.id] = add_response
            edit_response = stub.destructive_editTask(tasklist_pb2.Task(id=add_response.id, description="Edited task"))
            existing_id = add_response.id
            assert edit_response.id != 0
            assert edit_response.id == add_response.id
            assert edit_response.description == "Edited task"

        for i in range(1):
            desc = random_string_generator(99, string.ascii_letters)
            add_response = stub.addTask(wrappers_pb2.StringValue(value=desc))
            tasks[add_response.id] = add_response
            try:
                desc = random_string_generator(2000, string.ascii_letters)
                response = stub.destructive_editTask(tasklist_pb2.Task(id=existing_id, description=desc))
                assert len(response.description) != 2000
            except grpc.RpcError as e:
                assert e.code() != grpc.StatusCode.OK
                assert e.code() == grpc.StatusCode.INVALID_ARGUMENT, f"Validate user input for length < MAXLEN(=1024)"
                assert e.details() != "", f"Set an appropriate error message"



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    
    test_addTask()
    test_editTask()