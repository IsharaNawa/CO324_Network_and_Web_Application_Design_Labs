#E/17/219
#Nawarathna K.G.I.S.
import paho.mqtt.client as mqtt
import uuid

class MQTT:
    def __init__(self):
        #client id is assingned as 0
        #each time , the connection should be limited.(non presistent). That means each time, the connection should be
        #closed.Therefore cleas settion is set to True.
        self.client = mqtt.Client(client_id="0", clean_session=True, userdata=None, protocol=mqtt.MQTTv311,
                                  transport="tcp")

        # 'HiveMQ' is chosen as the public MQTT broker, the corresponding broker address is assigned
        # Since the message broker should have the unencrypted, unauthenticated mode, '1883' is assgned as the port
        self.client.connect(host="broker.hivemq.com", port=1883, keepalive=60, bind_address="")

    def get_e_number(self):
        """Return the string representation of E Number in format "E17xxx" (e.g.: E17000)"""
        return "E17219"

    def publish_message(self, topicName:str, data:str):
        """
            1) Publishes to a specified topic
            2) Should publish the data as the payload of the message
            3) Message broker should drop messages if no one subscribed to the specified topic
            4) Deliver messages with at least once delivery 

        """

        #message broker is configured to drop in case of no subscribers
        #to do this retain is set to Flase
        #messeges has to delivered at least once
        #to do this qos is set to 1
        self.client.publish(topic=topicName, payload=data, qos=1, retain=False)


    def subscribe_to_topic(self, topicName:str):
        self.client.subscribe(topic=topicName)


    def addTask(self, description:str, topicName:str) -> None:
        """
            1) Generate an unique ID for the task
            2) Create data to be published
            3) Call the publish method to publish to the specified topic
        """

        #id always need to be unique
        #to do this id is set using UUID
        #operation is set to ADD
        data = "{{'operation': 'ADD', 'idx': {id}, 'state': 'OPEN', 'description': '{desc}'}}".format(
            id=uuid.uuid1().int, desc=description)
        self.publish_message(topicName, data)


    def deleteTask(self, idx:int, topicName:str) -> None:
        """
            1) Create data to be published
            2) Call the publish method to publish to the specified topic
        """
        # operation is set to DELETE
        #id is set as the passed id
        data = "{{'operation': 'DELETE', 'idx': {id}}}".format(id=idx)
        self.publish_message(topicName, data)
        

if __name__ == "__main__":
    mqtt_obj = MQTT()

    #Q1.a
    data = "{'operation': 'ADD', 'idx': 123, 'state': 'OPEN', 'description': 'example task'}"
    mqtt_obj.publish_message(data)
