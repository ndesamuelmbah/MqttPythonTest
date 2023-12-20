####################################################################################################################
##  Greate FastApi Documentation could be found at its documention linked below.                                  ##
##  https://fastapi.tiangolo.com/tutorial/path-params/                                                            ##
##  Additionally, the following medium article give greater insights into preventing access to /docs pages        ##
##  https://medium.com/data-rebels/fastapi-how-to-add-basic-and-cookie-authentication-a45c85ef47d3                ##
####################################################################################################################
##  Project tips                                                                                                  ##
## Requests tip Python - Notes: In get requests you can add params and in posts requests you can add json         ##
##                                                                                                                ##
## Path is used for parameters to be in the url, Query is used for url query parameters, Form is for body params  ##
## sudo systemctl restart nginx   sudo supervisorctl reload                                                       ##
####################################################################################################################
import json
from typing import Optional, List, Any, Dict, AnyStr
from constants import GOOGLE_APPLICATION_CREDENTIALS, GOOGLE_MAPS_API_KEY, DF_CHARACTERS
from datetime import datetime, timedelta
import paho.mqtt.client as mqtt

from geopy.geocoders import Nominatim
from geopy.geocoders.googlev3 import GoogleV3
import firebase_admin
from firebase_admin import credentials, messaging, storage, firestore
from database import store_in_mysql_database


geolocator = Nominatim(user_agent="dukaGas")
#gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
gv3  = GoogleV3(api_key = GOOGLE_MAPS_API_KEY)

serviceAccCreds = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS)
firebase_admin.initialize_app(credential = serviceAccCreds, name='saving_in_firestore')

firestoreDB = firestore.Client(credentials=serviceAccCreds.get_credential())
customersRef = firestoreDB.collection('customers')
publishedMessagesRef = firestoreDB.collection("publishedMessages")


def get_cameroon_time_now(in_milliseconds = False):
    time_now = datetime.utcnow() + timedelta(hours = 1)
    if in_milliseconds:
        return int(time_now.timestamp()*1000)
    return time_now

def get_timestamp_now():
    return int(datetime.now().timestamp()*1000)

def get_message_id(time):
    time_id = int(time)
    if (time_id < 62):
        return DF_CHARACTERS[time_id]
    res = ''
    remainder = 0
    while (time_id > 61):
        remainder = time_id % 62
        time_id //= 62
        res += DF_CHARACTERS[remainder]
    res += DF_CHARACTERS[remainder]
    return res

def store_message_in_firestore(message: mqtt.MQTTMessage):
    payload = message.payload.decode("utf-8")
    message_id = get_message_id(get_timestamp_now())
    topic = message.topic
    message_meta = {
        'timestamp': message.timestamp,
        'message_id': message_id,
        'qos': message.qos,
        'retain': message.retain,
        'dup': message.dup,
        'mid': message.mid,
        'topic': topic
    }
    data = json.loads(payload)
    data.update(message_meta)
    if('clientId' in data):
        data['temperature'] = data['outsideTemperature']
        publishedMessagesRef.document(data['clientId']).set(data)
        print(f"Message with message_id {message_id} from client {data['clientId']} has been stored in firestore")
    else:
        #publishedMessagesRef.document(message_id).set(data)
        print(f"Message with message_id {message_id} from client {data['clientId']} has not been stored in firestore")