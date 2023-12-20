import paho.mqtt.client as mqtt
from random import randrange
import time
from constants import mqtt_broker, outside_temperature, topic_temperature

client = mqtt.Client(outside_temperature)
client.connect(mqtt_broker)

published_attempts = 0
while published_attempts < 6:
    inside_temperature = randrange(10)
    client.publish(topic_temperature, inside_temperature)
    print(f"Temperature outside of '{inside_temperature}' to topic '{topic_temperature}'")
    time.sleep(1)
    published_attempts += 1
