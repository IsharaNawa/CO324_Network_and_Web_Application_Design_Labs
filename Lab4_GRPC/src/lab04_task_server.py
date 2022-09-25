#E/17/219
#K.G.I.S. Nawarathna

import logging
from concurrent.futures import ThreadPoolExecutor
from google.protobuf import descriptor
from grpc import server
import tasklist_pb2, tasklist_pb2_grpc


class TaskapiImpl:
    """'Implementation of the Taskapi service"""

    def __init__(self):
        """Do required initializations to store tasks"""
        self.tasklist = []

        
    def addTask(self, request, context):
        """
        Returns the Task created
            1) Create a new Task
            2) Store in new Task in the server
            3) Return the created Task
        """
        logging.info(f"adding task {request.description}")

        task = {len(self.tasklist)+1 : request.description}
        self.tasklist.append(task)

        return tasklist_pb2.Task(id=len(self.tasklist),description=request.description)

    def delTask(self, request, context):
        """
        Returns the deleted Task
            1) Delete the Task with specified Id from the server
            2) Return the deleted Task
        """
        logging.info(f"deleting task {request.id}")

        desc =""

        for task in self.tasklist:
            if(	task.__contains__(request.id)):
                desc = task[request.id] 
                self.tasklist.remove(task)
                break

        return tasklist_pb2.Task(id=request.id,description=desc)



    def listTasks(self, request, context):
        """Returns all the Tasks stored in the server"""
        logging.info("returning task list")

        out = []

        for task in self.tasklist:
            key = list(task.keys())
            key=key[0]
            value = list(task.values())
            value=value[0]
            out.append(tasklist_pb2.Task(id=key,description=value))
            
        return tasklist_pb2.Tasks(tasks=out)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with ThreadPoolExecutor(max_workers=1) as pool:
        taskserver = server(pool)
        tasklist_pb2_grpc.add_TaskapiServicer_to_server(TaskapiImpl(), taskserver)
        taskserver.add_insecure_port("[::]:50051")
        try:
            taskserver.start()
            logging.info("Taskapi ready to serve requests")
            taskserver.wait_for_termination()
        except:
            logging.info("Shutting down server")
            taskserver.stop(None)
