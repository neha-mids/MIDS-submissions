iimport numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message received")

face_cascade = cv.CascadeClassifier('/haarcascades/haarcascade_frontalface_default.xml')

broker_address = "mosquitto"
client = mqtt.Client("test")
# print(client)
client.on_message = on_message
client.connect(broker_address)

client.subscribe("imagelocal")
# client.publish("testtopic", str(time.time()))

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # We don't use the color information, so might as well save space
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # face detection and other logic goes here
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,t,w,h) in faces:
	# your logic goes here; for instance
	face = gray[y:y+h, x:x+w]
	print(gray.shape, x, y, h, w)
	rc,png = cv.imencode('.png', face)
        msg = png.tobytes()
	client.publish("imagelocal", msg, qos = 0, retain = False)

client.loop_forever()
