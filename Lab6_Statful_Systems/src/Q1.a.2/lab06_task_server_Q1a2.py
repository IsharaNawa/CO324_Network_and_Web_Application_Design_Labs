"""TODO:
    * Implement error handling in TaskapiImpl methods
    * Implement saveTasks, loadTasks
    * Implement TaskapiImpl.editTask (ignoring write conflicts)
    * Fix data race in TaskapiImpl.addTask
"""

#Reg No: E/17/219
#K.G.I.S. Nawarathna

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import logging
from pprint import pformat
from typing import Mapping, Sequence, Tuple

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
from grpc import server, StatusCode
import tasklist_pb2, tasklist_pb2_grpc
import threading #for synchronization in concurrency

class TaskapiImpl:
    def __init__(self, taskfile: str):
        self.taskfile = taskfile
        self.task_id = 1
        self.ExLock = threading.Lock()          #instantiating a lock for concurrency control

    def __enter__(self):
        """Load tasks from self.taskfile"""
        with open(self.taskfile, mode="rb") as t:
            tasklist = tasklist_pb2.Tasks()
            tasklist.ParseFromString(t.read())
            logging.info(f"Loaded data from {self.taskfile}")
            self.tasks: Mapping[int, tasklist_pb2.Task] = {item.id: item for item in tasklist.pending}
            print(self.tasks)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Save tasks to self.taskfile"""
        with open(self.taskfile, mode="wb") as t:
            tasks = tasklist_pb2.Tasks(pending=self.tasks.values())
            t.write(tasks.SerializeToString())
            logging.info(f"Saved data to {self.taskfile}")

    def addTask(self, request: wrappers_pb2.StringValue, context) -> tasklist_pb2.Task:
        #error handling
        if (len(request.value) > 1023):
            t = tasklist_pb2.Task()
            context.set_details('Please enter a description with length is less than 1024')
            context.set_code(StatusCode.INVALID_ARGUMENT)
            return t
        
        with self.ExLock:
            logging.debug(f"addTask parameters {pformat(request)}")
            t = tasklist_pb2.Task(id=self.task_id, description=request.value)
            #since we need to implement destructive method, only adding the task to the dictionary would be enough
            self.tasks[self.task_id] = t
            self.task_id += 1
            return t

    def delTask(self, request: wrappers_pb2.UInt64Value, context) -> tasklist_pb2.Task:
        logging.debug(f"delTask parameters {pformat(request)}")
        return self.tasks.pop(request.value)

    def listTasks(self, request: tasklist_pb2.TaskQuery, context) -> tasklist_pb2.Tasks:
        logging.debug(f"listTasks parameters {pformat(request)}")
        return tasklist_pb2.Tasks(pending=self.tasks.values())


    def destructive_editTask(self, request: tasklist_pb2.Task, context) -> tasklist_pb2.Task:
        """Returns the edited Task (destructive)"""
        #error handling
        if(len(request.description)>1023):              
            t = tasklist_pb2.Task()
            context.set_details('Please enter a description with length is less than 1024')
            context.set_code(StatusCode.INVALID_ARGUMENT)
            return t

        with self.ExLock:
            self.tasks[request.id] = request  #adding the new task to the list with the same id with overwitting the current value
            return request                         # returning the edited task


TASKFILE = "./src/Q1.a.2/tasklist.protobuf"
if __name__ == "__main__":
    Path(TASKFILE).touch()
    logging.basicConfig(level=logging.DEBUG)

    with ThreadPoolExecutor(max_workers=1) as pool, TaskapiImpl(TASKFILE) as taskapiImpl:
        taskserver = server(pool)
        tasklist_pb2_grpc.add_TaskapiServicer_to_server(taskapiImpl, taskserver)
        taskserver.add_insecure_port("[::]:50051")
        try:
            taskserver.start()
            logging.info("Taskapi ready to serve requests")
            taskserver.wait_for_termination()
        except:
            logging.info("Shutting down server")
            taskserver.stop(None)
