import platform, os
env = os.environ


IS_ON_WINDOWS = 'win' in platform.system().lower()
mqtt_broker = env.get('BROKER_IP_ADDRESS') if IS_ON_WINDOWS else env.get('LOCALHOST') #"mqtt.eclipseprojects.io"#
inside_temperature = "INSIDE_TEMPERATURE"
outside_temperature = "OUTSIDE_TEMPERATURE"
topic_temperature = "TEMPERATURE"
device_smart_phone = "Smartphone"
locations_samuel_nde = "locations_samuel_nde"
location_updates = "LOCATION_UPDATES"