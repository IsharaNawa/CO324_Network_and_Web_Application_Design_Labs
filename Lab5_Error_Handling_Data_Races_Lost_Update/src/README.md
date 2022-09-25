# Q1

## Q1.a

Context managers help manage resources efficiently. We can use the `with` statement to manage resources. We can even customize our classes to support these types of resource handling when using the `with` statement. Read more about [context managers](https://dbader.org/blog/python-context-managers-and-with-statement) here.

1. Implement the `__enter__(self): ` method to Load tasks to the server from a saved list of tasks in a specified file.
```python
def __enter__(self):
        """Load tasks from self.taskfile"""
```

2. Implement the `__exit__(self):` method to Save existing tasks in the server back to the specified file.

```python
def __exit__(self, exc_type, exc_val, exc_tb):
        """Save tasks to self.taskfile"""
```

## Q1.b

The internet is a dangerous place! You should always take the necessary precautions to ensure the [security of your web applications](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Website_security). We can implement user input validation as one such action. There are mainly two types of user input validation considered in client-server web applications.
* [Client-side validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation) (Done on the Browser - Frontend)
* [Server-side validation](https://owasp.org/www-project-proactive-controls/v3/en/c5-validate-inputs) (Done on the Server - Backend)

You can read more about them in the above references. Your task is to implement server-side validation in this question.

1. Modify the `addTask` method so that task descriptions must be less than MAXLEN=1024 characters.

2. Modify the `deleteTask` method so that task IDs must be valid.

If above methods fail, You should return an empty Task along with appropriate [gRPC status codes](https://developers.google.com/maps-booking/reference/grpc-api/status_codes) and error messages.

## Q1.c

Implement the `editTask(self, request, context)` to edit a specified Task. Return the edited Task. Include MAXLEN=1024 restriction here as well.
```python
def editTask(self, request, context):
        """Returns the edited Task"""
```

## Q1.d

In simple terms,

**Race condition:** "is a situation, in which the result of an operation depends on the interleaving of certain individual operations."

**Data race:** "is a situation, in which at least two threads access a shared variable at the same time. At least one thread tries to modify the variable."

In the above task-list applications, concurrency issues such as data races and race conditions can happen. We can avoid data races by synchronizing access to mutable data that is can be shared between threads (different users in our case). 

We can use [mutual exclusion locks](https://www.geeksforgeeks.org/python-how-to-lock-critical-sections/) to deal with these critical sections in our code.

Implement proper mutual exclusion using the [`threading.Lock` class](https://docs.python.org/3/library/threading.html#lock-objects) available in python to ensure that `addTask` and `editTask` methods are free from data races.
