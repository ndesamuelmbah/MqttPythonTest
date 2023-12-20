import paho.mqtt.client as mqtt
import time, json
from constants import topic_AllTOPICS, device_smart_phone
from mqtt_helpers import create_client
from store_in_mysql_database import store_in_my_sql_database
from typing import Any

def on_message(client: mqtt.Client, userdata: Any, message: mqtt.MQTTMessage):
    #Print te client username
    print(f"topic type is {message.topic}") #
    print(f"timestamp is {message.timestamp}") #
    print(f"message_id is {message.mid}") #
    print(f"qos is {message.qos}")
    print(f"dup is {message.dup}")
    print(f"retain is {message.retain}")

    payload = message.payload.decode("utf-8")
    try:
        topic = message.topic
        data = json.loads(payload)
        store_in_my_sql_database(topic, payload)
    except Exception as e:
        print(f"Could not convert payload to json {e}")

    # try:
    #     topic = message.topic
    #     data = json.loads(payload)
    #     store_in_my_sql_database(topic, payload)
    # except Exception as e:
    #     print(f"Could not convert payload to json {e}")
    print("Received message: ", str(payload))


client = create_client(device_smart_phone)

client.loop_start()
client.subscribe(topic_AllTOPICS)
client.on_message = on_message
time.sleep(30)
#if(number_of_messages >= 5):
client.loop_end()
