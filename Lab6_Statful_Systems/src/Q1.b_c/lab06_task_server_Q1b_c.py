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
import threading

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
            t = tasklist_pb2.Task(id=self.task_id, description=request.value,state=tasklist_pb2.TaskState.OPEN)
            self.tasks[self.task_id] = t
            self.task_id += 1
            return t


    def delTask(self, request: wrappers_pb2.UInt64Value, context) -> tasklist_pb2.Task:
        logging.debug(f"delTask parameters {pformat(request)}")
        return self.tasks.pop(request.value)

    def listTasks(self, request: tasklist_pb2.TaskQuery, context) -> tasklist_pb2.Tasks:
        logging.debug(f"listTasks parameters {pformat(request)}")

        #when the task query is empty
        if(len(request.selected)==0):
            return tasklist_pb2.Tasks(pending=self.tasks.values())
        
        #when the select query is given
        myList = []
        for i in self.tasks.values():
            if i.state  in request.selected:
                myList.append(i)

        return tasklist_pb2.Tasks(pending=myList)


    def editTask(self, request: tasklist_pb2.Task, context) -> tasklist_pb2.Task:
        """
            Returns the edited Task based on states, return an appropriate error upon failure
            (Assume destructive edits happen)
        """
        #error handling
        if(len(request.description)>1023):              
            t = tasklist_pb2.Task()
            context.set_details('Please enter a description with length is less than 1024')
            context.set_code(StatusCode.INVALID_ARGUMENT)
            return t

        with self.ExLock:
            
            #dealing with the incorrect state transition
            if(self.tasks[request.id].state==0): #this is the OPEN state

                if(request.state==2 or request.state==3):   #next state can not be 2.PROSESSING or 3.DONE states
                    context.set_code(StatusCode.INVALID_ARGUMENT)
                    context.set_details("Please enter the correct state transition")
                    return request

            elif(self.tasks[request.id].state==1): #this is the ASSIGNED state

                if(request.state!=2):   #next state must be 2.PROGRESSING
                    context.set_code(StatusCode.INVALID_ARGUMENT)
                    context.set_details("Please enter the correct state transition")
                    return request

            elif(self.tasks[request.id].state==2): #this is the PROGRESSING state

                if(request.state==0 or request.state==1):   #next state can not be 0.OPEN or 1.ASSIGNED
                    context.set_code(StatusCode.INVALID_ARGUMENT)
                    context.set_details("Please enter the correct state transition")
                    return request

            elif(self.tasks[request.id].state==3): #this is the DONE state

                if(request.state!=3):   #next state can not be a state otherthan DONE
                    context.set_code(StatusCode.INVALID_ARGUMENT)
                    context.set_details("Please enter the correct state transition")
                    return request

            elif(self.tasks[request.id].state==4): #this is the CANCELLED state

                if(request.state!=4):   #next state can not be a state otherthan CANCELLED
                    context.set_code(StatusCode.INVALID_ARGUMENT)
                    context.set_details("Please enter the correct state transition")
                    return request

            self.tasks[request.id] = request
            return request        


TASKFILE = "./src/Q1.b_c/tasklist.protobuf"
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
