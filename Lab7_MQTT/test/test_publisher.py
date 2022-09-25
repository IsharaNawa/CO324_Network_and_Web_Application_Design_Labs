import sys
sys.path.append('./src/')

from lab07 import *
import paho.mqtt.client as mqtt
import time

class TestPublisher:
	def on_connect(self, mqttc, obj, flags, rc):
		assert rc == 0
		print("Connected")

	def on_message(self, mqttc, obj, msg):
	    self.message = msg
	    data = eval(msg.payload)
	    if data["operation"] == 'ADD':
	    	self.tasks[data['idx']] = {'state': data["state"], 'description': data["description"]}
	    elif data["operation"] == 'DELETE':
	    	key = int(data['idx'])
	    	if key in self.tasks:
	    		del self.tasks[key]
	    print(self.tasks)


	def on_publish(self, mqttc, obj, mid):
	    print("mid: " + str(mid))


	def on_subscribe(self, mqttc, obj, mid, granted_qos):
	    print("Subscribed: " + str(mid) + " " + str(granted_qos))
	    self.tasks = {}


	def on_log(self, mqttc, obj, level, string):
	    print(string)


	def test_publisher(self):
		client = mqtt.Client()
		client.on_message = self.on_message
		client.on_connect = self.on_connect
		client.on_publish = self.on_publish
		client.on_subscribe = self.on_subscribe

		client.connect("broker.hivemq.com", 1883, 60)

		mqtt_obj = MQTT()
		topic = "TaskApi" + mqtt_obj.get_e_number()
		client.subscribe(topic, qos=1)

		# time.sleep(30)

		data = "{'operation': 'ADD', 'idx': 123, 'state': 'OPEN', 'description': 'example task'}"
		client.loop_start()
		mqtt_obj = MQTT()
		mqtt_obj.publish_message(topic, data)
		time.sleep(30)
		assert self.message.payload.decode('UTF-8') == data, "Payload not matching"
		assert self.message.qos == 1, "QoS not matching"
		assert self.message.retain == 0, "Retain value is incorrect"
		assert self.message.topic == topic, "Topic is incorrect"
		client.loop_stop()


	def test_addTask(self):
		client = mqtt.Client()
		client.on_message = self.on_message
		client.on_connect = self.on_connect
		client.on_publish = self.on_publish
		client.on_subscribe = self.on_subscribe

		client.connect("broker.hivemq.com", 1883, 60)

		mqtt_obj = MQTT()
		topic = "TaskApi" + mqtt_obj.get_e_number()
		client.subscribe(topic, qos=1)
		client.loop_start()
		mqtt_obj = MQTT()
		mqtt_obj.addTask("dummy description", topic)
		time.sleep(30)
		assert "dummy description" in [x["description"] for x in self.tasks.values()], "Task not added properly, check addTask() method"
		client.loop_stop()


	def test_deleteTask(self):
		client = mqtt.Client()
		client.on_message = self.on_message
		client.on_connect = self.on_connect
		client.on_publish = self.on_publish
		client.on_subscribe = self.on_subscribe

		client.connect("broker.hivemq.com", 1883, 60)

		mqtt_obj = MQTT()
		topic = "TaskApi" + mqtt_obj.get_e_number()
		client.subscribe(topic, qos=1)
		client.loop_start()
		mqtt_obj = MQTT()
		mqtt_obj.addTask("new description", topic)
		time.sleep(30)
		idx_to_delete = 0
		for idx in self.tasks:
			idx_to_delete = idx
		assert idx_to_delete in self.tasks
		mqtt_obj = MQTT()
		mqtt_obj.deleteTask(idx_to_delete, topic)
		time.sleep(30)
		assert idx_to_delete not in self.tasks, "Task not deleted properly, check deleteTask() method"
		client.loop_stop()


if __name__ == "__main__":
	pt = TestPublisher()
	pt.test_publisher()
