import sys
sys.path.append('./src/Q1.b_c')
from lab06_task_server_Q1b_c import *

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
            assert response.state == tasklist_pb2.TaskState.OPEN, f"Initial task state should be OPEN"
            tasks[response.id] = response
        try:
            desc = random_string_generator(2000, string.ascii_letters)
            response = stub.addTask(wrappers_pb2.StringValue(value=desc))
            assert len(response.description) != 2000, f"Modify addTask to add only tasks with description < MAXLEN (=1024)"
        except grpc.RpcError as e:
            assert e.code() != grpc.StatusCode.OK
            assert e.code() == grpc.StatusCode.INVALID_ARGUMENT, f"Validate user input for length < MAXLEN(=1024)"
            assert e.details() != "", f"Set an appropriate error message"

def create_new_task(stub):
    desc = random_string_generator(99, string.ascii_letters)
    add_response = stub.addTask(wrappers_pb2.StringValue(value=desc))
    tasks[add_response.id] = add_response
    return add_response

def check_state_transition(stub, add_response, current_state, next_state):
    edit_response = stub.editTask(tasklist_pb2.Task(id=add_response.id, description=f"{current_state} to {next_state}", state=tasklist_pb2.TaskState.Value(next_state)))
    assert edit_response.id == add_response.id
    assert edit_response.description == f"{current_state} to {next_state}"
    assert edit_response.state == tasklist_pb2.TaskState.Value(next_state)

def test_editTask():
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tasklist_pb2_grpc.TaskapiStub(channel)
        existing_id = 0
        
        # OPEN -> ASSIGNED -> PROGRESSING -> DONE
        add_response = create_new_task(stub)
        check_state_transition(stub, add_response, "OPEN", "ASSIGNED")
        check_state_transition(stub, add_response, "ASSIGNED", "PROGRESSING")
        check_state_transition(stub, add_response, "PROGRESSING", "DONE")

        # OPEN -> ASSIGNED -> PROGRESSING -> CANCELLED
        add_response = create_new_task(stub)
        check_state_transition(stub, add_response, "OPEN", "ASSIGNED")
        check_state_transition(stub, add_response, "ASSIGNED", "PROGRESSING")
        check_state_transition(stub, add_response, "ASSIGNED", "CANCELLED")

        # OPEN -> CANCELLED
        add_response = create_new_task(stub)
        check_state_transition(stub, add_response, "OPEN", "CANCELLED")

        # OPEN
        add_response = create_new_task(stub)
        # OPEN -> DONE
        try:
            edit_response = stub.editTask(tasklist_pb2.Task(id=add_response.id, description="OPEN to DONE", state=tasklist_pb2.TaskState.DONE))
            assert edit_response.state != tasklist_pb2.TaskState.DONE
        except grpc.RpcError as e:
            assert e.code() != grpc.StatusCode.OK
            assert e.code() == grpc.StatusCode.INVALID_ARGUMENT
            assert e.details() != "", f"Set an appropriate error message"

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
                assert e.code() == grpc.StatusCode.INVALID_ARGUMENT, f"Validate user input for length < MAXLEN(=1024)"
                assert e.details() != "", f"Set an appropriate error message"


def test_listTasks():
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tasklist_pb2_grpc.TaskapiStub(channel)
        existing_id = 0
        
        # OPEN -> ASSIGNED
        add_response_1 = create_new_task(stub)
        stub.editTask(tasklist_pb2.Task(id=add_response_1.id, description="OPEN to ASSIGNED", state=tasklist_pb2.TaskState.ASSIGNED))

        # OPEN -> ASSIGNED -> PROGRESSING
        add_response_2 = create_new_task(stub)
        stub.editTask(tasklist_pb2.Task(id=add_response_2.id, description="OPEN to ASSIGNED", state=tasklist_pb2.TaskState.ASSIGNED))
        stub.editTask(tasklist_pb2.Task(id=add_response_2.id, description="ASSIGNED to PROGRESSING", state=tasklist_pb2.TaskState.PROGRESSING))

        list_response_1 = stub.listTasks(tasklist_pb2.TaskQuery(selected=[tasklist_pb2.TaskState.ASSIGNED, tasklist_pb2.TaskState.PROGRESSING]))
        tasks = list(list_response_1.pending)
        assert add_response_1.id in [task.id for task in tasks]
        assert add_response_2.id in [task.id for task in tasks]
        list_response_2 = stub.listTasks(tasklist_pb2.TaskQuery(selected=[]))
        assert len(list(list_response_1.pending)) != len(list(list_response_2.pending))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    
    # test_addTask()
    # test_listTasks()
    # test_editTask()
    test_listTasks()