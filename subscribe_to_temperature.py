import paho.mqtt.client as mqtt
import time
from constants import topic_temperature, device_smart_phone
from mqtt_helpers import create_client
from typing import Any
def on_message(client: mqtt.Client, userdata: Any, message: mqtt.MQTTMessage):
    print(f"userdata type is {type(userdata)}") #
    print("Received message: ", str(message.payload.decode("utf-8")))


client = create_client(device_smart_phone)

client.loop_start()
client.subscribe(topic_temperature)
client.on_message = on_message
time.sleep(30)
#if(number_of_messages >= 5):
client.loop_end()
