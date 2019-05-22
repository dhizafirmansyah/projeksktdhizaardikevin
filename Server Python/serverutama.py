import paho.mqtt.client as mqtt
import os, urlparse
import json
import time

mqttc = mqtt.Client()
jumlahkrupuk = 50
topic ='kirim1'
topicsebar ='sebar'

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    global jumlahkrupuk
    print(str(msg.payload))
    data = int(msg.payload)
    jumlahkrupuk = jumlahkrupuk - data
    mqttc.publish(topicsebar,jumlahkrupuk)
    
    
    
   
    
          
# def on_publish(client, obj, mid):
#     print("mid: " + str(mid))

# def on_subscribe(client, obj, mid, granted_qos):
#     print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)


# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
# mqttc.on_publish = on_publish
# mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# # Parse CLOUDMQTT_URL (or fallback to localhost)
# url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://localhost:1883')
# url = urlparse.urlparse(url_str)



# Connect
mqttc.username_pw_set("oiftmfqd" , "N9ABDhE6_aMN" )
mqttc.connect( "m15.cloudmqtt.com", "17496" )

# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)



# Publish a message
# mqttc.publish(topic,'{"Nama": "Simory","Bagian":"Sensor","Kebutuhan": "Actuator_Air"}')

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
    print("Jumlah Stok : " +str(jumlahkrupuk))
    
    # print("rc: " + str(rc))