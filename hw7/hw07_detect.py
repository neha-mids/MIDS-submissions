from PIL import Image
import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt
import time
import os
import tensorflow.contrib.tensorrt as trt
import tensorflow as tf
print("Finished Importing Libraries")

def on_message(client, userdata, message):
    print("message received")

#face_cascade = cv.CascadeClassifier('/haarcascades/haarcascade_frontalface_default.xml')
FROZEN_GRAPH_NAME = 'data/frozen_inference_graph_face.pb'
output_dir=''
frozen_graph = tf.GraphDef()
with open(os.path.join(output_dir, FROZEN_GRAPH_NAME), 'rb') as f:
  frozen_graph.ParseFromString(f.read())

print("Loaded Frozen Graph")

# Adding constants
INPUT_NAME='image_tensor'
BOXES_NAME='detection_boxes'
CLASSES_NAME='detection_classes'
SCORES_NAME='detection_scores'
MASKS_NAME='detection_masks'
NUM_DETECTIONS_NAME='num_detections'

input_names = [INPUT_NAME]
output_names = [BOXES_NAME, CLASSES_NAME, SCORES_NAME, NUM_DETECTIONS_NAME]

# Optimizing frozen graph with TensorRT
#trt_graph = trt.create_inference_graph(
#    input_graph_def=frozen_graph,
#    outputs=output_names,
#    max_batch_size=1,
#    max_workspace_size_bytes=1 << 25,
#    precision_mode='FP16',
#    minimum_segment_size=50
#)

#print("Optimized frozen graph with TensorRT")

# Creating session and loading graph
tf_config = tf.ConfigProto()
tf_config.gpu_options.allow_growth = True

tf_sess = tf.Session(config=tf_config)

tf.import_graph_def(frozen_graph, name='')

tf_input = tf_sess.graph.get_tensor_by_name(input_names[0] + ':0')
tf_scores = tf_sess.graph.get_tensor_by_name('detection_scores:0')
tf_boxes = tf_sess.graph.get_tensor_by_name('detection_boxes:0')
tf_classes = tf_sess.graph.get_tensor_by_name('detection_classes:0')
tf_num_detections = tf_sess.graph.get_tensor_by_name('num_detections:0')

broker_address = "mosquitto"
client = mqtt.Client("test")
# print(client)
client.on_message = on_message
client.connect(broker_address)

client.subscribe("imagelocal")
# client.publish("testtopic", str(time.time()))

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
i = 0
cap = cv.VideoCapture(0)

t0 = time.time()
while(True):
    # Capture frame-by-frame UNCOMMENT BELOW LINE
    ret, frame = cap.read()

    image = np.array(frame)

    # image_resized = frame[0:300, 0:300, :]
    # UNCOMMENT THIS ONE
    # image_resized = cv.resize(frame,(300,300))
    # cv.imshow("frame", frame)

    # TEST CODE
    # image = cv.imread('/neha_hd.jpg')
    # image_resized = cv.resize(image,(300,300))


    # face detection and other logic goes here
    scores, boxes, classes, num_detections = tf_sess.run([tf_scores, tf_boxes, tf_classes, tf_num_detections], feed_dict={
    tf_input: image[None,  ...]})
    boxes = boxes[0] # index by 0 to remove batch dimension
    scores = scores[0]
    classes = classes[0]
    num_detections = num_detections[0]
    # print("Max Score:", np.amax(scores))

    for i in range(int(num_detections)):
        if scores[i] < 0.5:
            continue

        
        print("Face Detected")
        i += 1
        t1 = time.time()
        total = t1 - t0
        print("Time to run {} frames: {}".format(int(i), total))
        
        box = boxes[i] * np.array([image.shape[0], image.shape[1], image.shape[0], image.shape[1]])
        box = box.astype(int)
        print("Score:", scores[i])
        print("Box:", box)
        y1 = box[0]
        x1 = box[1]
        y2 = box[2]
        x2 = box[3]

        face = image[y1:y2, x1:x2, :]

        # rcfull, pngfull = cv.imencode('.png',frame)
        cv.imwrite('/tmp/frame.png', image)
        
        rc,png = cv.imencode('.png', face)
        cv.imwrite('/tmp/face.png',face)
        # cv2.imshow("face", png)
        msg = png.tobytes()
        client.publish("imagelocal", msg, qos = 0, retain = False)

client.loop_forever()
