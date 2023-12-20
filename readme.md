Playing around with Python MQTT client Paho-MQTT and Mosquitto MQTT broker.
To use this, first set your broker ip address in `constants.py`
In my case, I was testing on windows and my broker was running on linux-ubuntu at a different ip address.
So I had saved my ip address in an environment variable called
`BROKER_IP_ADDRESS`
And when I needed to test on the broker itself, I used the locahost saved in environment variables as
`LOCALHOST`

I have also saved my test usernames and passwords in environment in `username password pairs` such that when I run a script, if I pass a username, it will get the password for that username and use it for authentication.

Thank you.
