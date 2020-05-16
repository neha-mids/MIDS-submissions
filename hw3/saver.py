import paho.mqtt.client as mqtt
import time
import os

if not os.path.exists('hw03_faces'):
    os.makedirs('hw03_faces')

LOCAL_MQTT_HOST="mosquittocloud"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="imageremote"
print(LOCAL_MQTT_TOPIC)

def on_connect(client, userdata, flags, rc):
        print("connecting to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client,userdata, msg):
    print(msg.topic + " Received On " + str(time.time()))
    f = open('hw03_faces/face_'+str(time.time()).replace('.',''), 'w+b')
    f.write(msg.payload)
    f.close()
  # try:
    # print("message received!")        
    # if we wanted to re-publish this message, something like this should work
    # msg = msg.payload
    # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  # except:
    # print("Unexpected error:", sys.exc_info()[0])

print("Creating Client")
client = mqtt.Client()
print("Created Client")

print("Assigning functions")
client.on_connect = on_connect
client.on_message = on_message

print("Connecting")
# client.loop_start()
client.connect(LOCAL_MQTT_HOST, 1883, 60)

# go into a loop
# time.sleep(60) # wait
# client.loop_stop() #stop the loop
client.loop_forever()
