import sys
sys.path.append('./src/')

from typing import Sequence, Mapping, Tuple
import random, string, logging, grpc
import tasklist_pb2, tasklist_pb2_grpc

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
            response = stub.addTask(tasklist_pb2.TaskDesc(description=desc))
            assert response.id == i + 1
            assert response.description == desc
            tasks[response.id] = response


# Test that will be used to grade listTask
def test_listTasks() -> None:
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tasklist_pb2_grpc.TaskapiStub(channel)
        for i in range(10):
            desc = random_string_generator(99, string.ascii_letters)
            add_response = stub.addTask(tasklist_pb2.TaskDesc(description=desc))
            tasks[add_response.id] = add_response

        response = stub.listTasks(tasklist_pb2.Empty())
        
        assert len([task for task in response.tasks]) == 20
        for task in response.tasks:
            # Is the proper task desc is returned for this id?
            assert task.description == tasks[task.id].description


# Test that will be used to grade delTask
def test_delTask() -> None:
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tasklist_pb2_grpc.TaskapiStub(channel)
        for i in range(10):
            desc = random_string_generator(99, string.ascii_letters)
            add_response = stub.addTask(tasklist_pb2.TaskDesc(description=desc))
            tasks[add_response.id] = add_response
        task_ids = list(tasks.keys())
        
        for i in task_ids:
            task = stub.delTask(tasklist_pb2.Id(id=i))
            assert task.id == i
            assert task.description == tasks[i].description


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tasklist_pb2_grpc.TaskapiStub(channel)

        # tasks = test_add(stub, 10)
        # logging.info(f"added tasks {tasks}")
        test_addTask()
        test_listTasks()
        test_delTask()
