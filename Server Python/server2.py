import paho.mqtt.client as mqtt
import os, urlparse
import json
import time

mqttc = mqtt.Client()
# mqttc2 = mqtt.Client()
topic ='kirim1'
topicterima ="beli2"
topicsebar ='sebar'
topichp1='hp1'


jumlahkrupuk =50

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    # print(str(msg.payload))
    # jumlahbeli =  str(msg.payload)
    # mqttc.publish(topic,jumlahbeli)

    if  str(msg.topic) == topicterima :
        jumlahbeli =  str(msg.payload)
        print("Dibeli :"+str(msg.payload)+" Buah Kerupuk")
        mqttc.publish(topic,jumlahbeli)
    elif str(msg.topic) == topicsebar :
        global jumlahkrupuk
        jumlahkrupuk =  str(msg.payload)
        mqttc.publish(topichp1,jumlahkrupuk)
        

# def on_message2(client, obj, msg):
#     global jumlahkrupuk
#     print(str(msg.payload))
#     jumlahkrupuk =  str(msg.payload)
#     mqttc2.publish(topichp1,jumlahkrupuk)
    
    
          
# def on_publish(client, obj, mid):
#     print("mid: " + str(mid))

# def on_subscribe(client, obj, mid, granted_qos):
#     print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)


# Assign event callbacks
mqttc.on_message = on_message
# mqttc2.on_message = on_message2
mqttc.on_connect = on_connect




# Connect
mqttc.username_pw_set("oiftmfqd" , "N9ABDhE6_aMN" )
mqttc.connect( "m15.cloudmqtt.com", "17496" )

# mqttc2.username_pw_set("oiftmfqd" , "N9ABDhE6_aMN" )
# mqttc2.connect( "m15.cloudmqtt.com", "17496" )

# Start subscribe, with QoS level 0
mqttc.subscribe('#', 0)
# mqttc2.subscribe(topicsebar, 0)



# Publish a message
# mqttc.publish(topic,'{"Nama": "Simory","Bagian":"Sensor","Kebutuhan": "Actuator_Air"}')

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
    # mqttc2.loop()
    print("Jumlah Stok : " +str(jumlahkrupuk))