# Q1

Create a task list application that tracks tasks that a user needs to complete. Implement a gRPC API with the RPCs that are defined in the given proto file. 

This application uses the client-server architecture. The server stores the task list. The server contains the functions (procedures) to manage the task list content. Then, the client sends request messages (i.e. Remote Procedure Calls - RPCs) to the server to initiate the specified tasks. This task list will contain the basic functionality listed below.
1. Adding a new task for a given description (Server should generate an ID to store the task - see the proto file definition)
2. Deleting an existing task with the given ID (see the proto file definition)
3. List all the tasks stored in the server (see the proto file definition)

## Q1.a
Complete the `addTask` function given to add a new task to the server.
```python
def addTask(self, request, context):
        """
        Returns the Task created
            1) Create a new Task
            2) Store in new Task in the server
            3) Return the created Task
        """
```

## Q1.b
Complete the `delTask` function to remove a task stored in the server.
```python
def delTask(self, request, context):
        """
        Returns the deleted Task
            1) Delete the Task with specified Id from the server
            2) Return the deleted Task
        """
```

## Q1.c
Complete the `listTasks` function to list tasks stored in the server.
```python
def listTasks(self, request, context):
        """Returns all the Tasks stored in the server"""
```