import paho.mqtt.client as mqtt
from constants import mqtt_broker
import os
def create_client(client_id: str, port: int = 18883, username: str = None):
    password = None
    client = mqtt.Client(client_id)
    if username is not None:
        password = os.environ.get(username)

        client.username_pw_set(username=username, password=password)
        print("username and password set")
    print(f"Connecting to {mqtt_broker} on port {port} ith username {username}- {password}")
    client.connect(mqtt_broker, port=port, keepalive = 60)
    return client
