# Q1

## Q1.a
Complete the given `editTask` functions to implement different API semantics covered in the class.
1. `nondestructive_editTask`: keeps a history of edits made to the task.
```python
def nondestructive_editTask(self, request, context):
        """Returns the edited Task (non-destructive)"""
```

2. `destructive_editTask`: deletes the task and creates a new task with the edits.
```python
def destructive_editTask(self, request, context):
        """Returns the edited Task (destructive)"""
```

## Q1.b
Suppose we modified the definition of Task to be able to track the current state of the task (similar to the Github issue tracker). Check the updated tasklist.proto file.

We would like to add the following rules governing the task lifecycle.
* New tasks are initially in OPEN state.
* OPEN tasks may be ASSIGNED or CANCELLED.
* Once someone begins work on an ASSIGNED task they set the status to PROGRESSING.
* A task that is PROGRESSING is either set to DONE once completed or CANCELLED.

1. Draw a state machine to illustrate all possible legal transitions between states. Save your answer as `src/taskstate-fsm.png`.
2. Implement task state update logic completing the `editTask` function. Your implementation must return a suitable error on illegal state transitions.
```python
def editTask(self, request, context):
        """Returns the edited Task based on states, return an appropriate error upon failure"""
```

## Q1.c
Modify your `listTasks` implementation to return a list of tasks that are in the specified states. If TaskQuery.selected is empty, return a list of all tasks. For example, `listTasks([DONE, CANCELLED])` should return tasks in either the DONE or CANCELLED state.
```python
def listTasks(self, request, context):
        logging.debug(f"listTasks parameters {pformat(request)}")
```

