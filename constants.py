import platform, os, json
env = os.environ


IS_ON_WINDOWS = 'win' in platform.system().lower()
mqtt_broker = env.get('BROKER_IP_ADDRESS') if IS_ON_WINDOWS else env.get('LOCALHOST') #"mqtt.eclipseprojects.io"#
inside_temperature = "INSIDE_TEMPERATURE"
outside_temperature = "OUTSIDE_TEMPERATURE"
topic_temperature = "TEMPERATURE"
topic_AllTOPICS = "#"
device_smart_phone = "Smartphone"
locations_samuel_nde = "locations_samuel_nde"
location_updates = "LOCATION_UPDATES"
conf_path = "/etc/mqtt_broker_api/mqtt_broker_data.json"
if not (os.path.isfile(conf_path)):
  conf_path = 'mqtt_broker_data.json'
with open(conf_path, 'rb') as f:
    ENV = json.load(f)
    f.close()

GOOGLE_APPLICATION_CREDENTIALS = (ENV["GOOGLE_APPLICATION_CREDENTIALS"])
GOOGLE_APPLICATION_CREDENTIALS = GOOGLE_APPLICATION_CREDENTIALS if os.path.isfile(GOOGLE_APPLICATION_CREDENTIALS) else GOOGLE_APPLICATION_CREDENTIALS.split('/')[-1]
GOOGLE_MAPS_API_KEY = ENV["GOOGLE_MAPS_API_KEY"]
DF_CHARACTERS = ENV["DF_CHARACTERS"]