import sys
sys.path.append('./src/')
from lab05_task_server import *

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
            assert e.code() == grpc.StatusCode.INVALID_ARGUMENT, f"Read when to use INVALID_ARGUMENT status code in the given reference. Then, set the appropriate status code shown here."
            assert e.details() != "", f"Set an appropriate error message"


# Test that will be used to grade listTask
def test_listTasks() -> None:
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tasklist_pb2_grpc.TaskapiStub(channel)
        for i in range(10):
            desc = random_string_generator(99, string.ascii_letters)
            add_response = stub.addTask(wrappers_pb2.StringValue(value=desc))
            tasks[add_response.id] = add_response

        response = stub.listTasks(empty_pb2.Empty())
        
        # assert len([task for task in response.tasks]) == 20
        for _, task in tasks.items():
            # Is the proper task desc is returned for this id?
            descriptions = [task.description for task in response.pending]
            assert task.description in descriptions


# Test that will be used to grade delTask
def test_delTask() -> None:
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tasklist_pb2_grpc.TaskapiStub(channel)
        for i in range(10):
            desc = random_string_generator(99, string.ascii_letters)
            add_response = stub.addTask(wrappers_pb2.StringValue(value=desc))
            tasks[add_response.id] = add_response
        task_ids = list(tasks.keys())
        
        for i in task_ids:
            task = stub.delTask(wrappers_pb2.UInt64Value(value=i))
            assert task.id == i
            assert task.description == tasks[i].description
        try:
            response = stub.delTask(wrappers_pb2.UInt64Value(value=int(1e5)))
        except grpc.RpcError as e:
            assert e.details() != "Exception calling application: 100000", f"Return an empty Task upon failure with a customized message"
            assert e.code() != grpc.StatusCode.OK
            assert e.code() == grpc.StatusCode.FAILED_PRECONDITION, f"Read when to use FAILED_PRECODITION status code in the given reference. Then, set the appropriate status code shown here."
            assert e.details() != "", f"Set an appropriate error message"


def test__enter__():
    TASKFILE = "./test/test_enter.protobuf"
    Path(TASKFILE).touch()
    with TaskapiImpl(TASKFILE) as taskapiImpl:
        for ID, task in taskapiImpl.tasks.items():
            assert ID == task.id
            assert type(task) == tasklist_pb2.Task


def test_editTask():
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tasklist_pb2_grpc.TaskapiStub(channel)
        existing_id = 0
        for i in range(5):
            desc = random_string_generator(99, string.ascii_letters)
            add_response = stub.addTask(wrappers_pb2.StringValue(value=desc))
            tasks[add_response.id] = add_response
            edit_response = stub.editTask(tasklist_pb2.Task(id=add_response.id, description="Edited task"))
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
                response = stub.editTask(tasklist_pb2.Task(id=existing_id, description=desc))
                assert len(response.description) != 2000
            except grpc.RpcError as e:
                assert e.code() != grpc.StatusCode.OK
                assert e.code() == grpc.StatusCode.INVALID_ARGUMENT, f"Read when to use INVALID_ARGUMENT status code in the given reference. Then, set the appropriate status code shown here."
                assert e.details() != "", f"Set an appropriate error message"



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    
    test__enter__()
    test_addTask()
    test_listTasks()
    test_delTask()
    test_editTask()