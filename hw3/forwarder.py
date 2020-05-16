import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="testtopic"
print(LOCAL_MQTT_TOPIC)

def on_connect(client, userdata, flags, rc):
        print("connecting to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
    print(msg.topic + " " + str(msg.payload))
  # try:
    # print("message received!")	
    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    remote_mqttclient.publish("testtopic", payload=msg, qos=0, retain=False)
  # except:
    # print("Unexpected error:", sys.exc_info()[0])

print("Creating Local and Remote Client")
client = mqtt.Client()
print("Created Local Client")
remote_mqttclient = mqtt.Client()
print("Created Remote Client")

print("Assigning functions")
client.on_connect = on_connect
client.on_message = on_message
# local_mqttclient.on_connect = on_connect_local
# local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
# local_mqttclient.on_message = on_message
# print("Now connecting to the host")
# local_mqttclient.connect(LOCAL_MQTT_HOST)
# print("Host connected")
# local_mqttclient.subscribe(LOCAL_MQTT_TOPIC)

print("Connecting to local broker")
client.connect(LOCAL_MQTT_HOST, 1883, 60)
print("Connecting to remote broker")
remote_mqttclient.connect("169.62.239.30", 1883, 60)


# go into a loop
client.loop_forever()
