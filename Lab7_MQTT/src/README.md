# Q1

## Q1.a

Complete the given `__init__(self)` method to instantiate an MQTT Client instance. 
1. The client instance should have an ID. Further, it should be configured for non-persistent connection mode. 
2. Connect the client to a message broker. Use freely available [Public MQTT brokers](https://mntolia.com/10-free-public-private-mqtt-brokers-for-testing-prototyping/) via unencrypted, unauthenticated mode OR a broker of your choice.

Complete the given `publish_message(self, topicName, data)` method and `get_e_number(self)` method.
1. It should publish on a specified topic. 
2. The data provided as an argument should be used as the payload of the MQTT message (Sample payload is available in the __main__ function).
3. Message broker should drop messages if there are no subscribers to the specified topic (**Hint:** Look at `retain` parameter of the publish method).
4. Deliver the messages with at least once delivery (**Hint:** Look at `qos` parameter of the publish method).

## Q1.b

Complete the given `addTask(self, description, topicName)` method that adds a task with given description.
1. Generate an unique ID for the task. This is essential because there is no server to maintain IDs and each subscriber will generate IDs. (**Hint:** Universally Unique IDentifier - [UUID](https://docs.python.org/3/library/uuid.html))
2. Create data to be published. Use format: "{'operation': 'ADD', 'idx': 123, 'state': 'OPEN', 'description': 'example task'}"
3. Call the publish method to publish to the specified topic

## Q1.c

Complete the given `deleteTask(self, idx, topicName)` method that deletes a task with given ID.
1. Create data to be published. Use format: "{'operation': 'DELETE', 'idx': 123}"
2. Call the publish method to publish to the specified topic
