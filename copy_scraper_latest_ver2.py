#########################################################################################################
# This Python script is build by Gert Koolwijk after only 2 weeks of study on Python.                   #
# A 'thank you' is much appreciated @ gert.koolwijk@gmail.com                                           #
# Also any feedback with suggestions for improvements are much appreciated.                             #
# To run this script using Crontab you must have the file located in the home directory (e.g. /home/pi) #
# The user must be the @Datawattch registered e-mail address like "my.email@gmail.com" including quotes #
# The password must be the password used to login @ the Datawattch website or App like "secret123"      #
# broker must be the IP address of the system with the MQTT broker like '192.168.1.100'                 #
# If used fill in the MQTT username and password with quotes like "mqtt"                                #
#########################################################################################################
#
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import paho.mqtt.client as paho
import datetime
import signal
from locale import atof, setlocale, LC_NUMERIC
setlocale(LC_NUMERIC, '') 
now = datetime.datetime.now()

# specify the variables
url = 'https://app.datawattch.com/app'
broker = >broker IP Address<
port = 1883
user = >email address to login on the Datawatch website<
pwd = >password to login on the Datawatch website<
mqtt_usr = >MQTT username<
mqtt_pw = ">MQTT password<
rc = 1

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully with code %d." % (rc))
    else:
        print("Connection failed with code %d." % (rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")
	
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload)) 

def on_disconnect(client, userdata,rc):
    logging.debug("DisConnected result code "+str(rc))

client = paho.Client("Python",True)
client.on_subscribe = on_subscribe
client.on_publish = on_publish
client.on_message = on_message
client.on_connect = on_connect
	
client.username_pw_set(mqtt_usr, mqtt_pw)

client.connect(broker, port, keepalive=60)

client.subscribe("zigbee2mqtt/solar", qos=1)

def main():

    s = requests.session()

    site = s.get("https://app.datawattch.com/app")
    bs_content = BeautifulSoup(site.content, "html.parser")
    token = bs_content.find("input", {"name":"_token"})["value"]
    login_data = {"email": user,"password": pwd, "_token":token}
    s.post("https://app.datawattch.com/app_login",login_data)
    home_page = s.get("https://app.datawattch.com/app")

    soup = BeautifulSoup(home_page.content, 'html.parser')
    consumer_page = soup.find(class_='fill_currentCurrent counter text-success')
    current = consumer_page.text.strip()
    cur_num1 = current.split()
    cur_num2 = (cur_num1[0])
    total_today = atof(cur_num2)
    print("\nCurrent date and time using strftime: "+ now.strftime("%d-%m-%Y %H:%M"))
    print((current)+" - "+ str(cur_num1)+" - "+ str(total_today))
    (rc, mid) = client.publish("zigbee2mqtt/solar", total_today, qos=1, retain=False)

if __name__ == '__main__':
    main()

