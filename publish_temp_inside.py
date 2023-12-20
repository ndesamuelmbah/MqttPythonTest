from random import uniform
import time, json, sys
from constants import inside_temperature, topic_temperature, location_updates
from mqtt_helpers import create_client
args = sys.argv
username = None
port = 18883
print(args)
if len(args) > 1:
    username = args[1]
    port = 8883
client = create_client(inside_temperature, username=username, port=port)
print(f"client is {client}")

#get the environment variable APP_DOMAIN and store it in a variable app_domain

published_attempts = 0
haspublished = False
while not haspublished and published_attempts < 6 :
    outside_temperature = uniform(20.0, 21.0)
    payload = json.dumps({'publishedAttempts':published_attempts, "outsideTemperature": outside_temperature})
    mqtt_message_info = client.publish(topic = location_updates, payload=f'''{payload}''', properties = {'publishedAttempts':published_attempts}, qos=0) #mqtt.MQTTMessageInfo
    haspublished = mqtt_message_info.rc == 0
    print(f" Was publish successful {haspublished}")
    # print(f"Published temperature inside of '{outside_temperature}' to topic '{topic_temperature}' with outcome [mid,rc] {[mqtt_message_info.mid, mqtt_message_info.rc]}")
    time.sleep(1)
    published_attempts += 1
