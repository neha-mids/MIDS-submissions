Link to binarized face images on the cloud: https://lab02-cos-standard-neha.s3.us-east.cloud-object-storage.appdomain.cloud
The topics for the cloud and local brokers were both named "testtopic." As the pipeline becomes increasingly complex, different names will be given for each topic to describe the messages being transmitted, ex: imageslocal and imagescloud
QoS of 0 (best attempt) was used as this was a streaming application. If one message was dropped, we want to continue with streaming subsquent messages without interruption

Commands run to spin up docker containers on the Jetson:
Local Broker: docker run --name mosquitto --network hw03 -p 1883:1883 -d broker
Sensor (Camera component): docker run --privileged --rm --network hw03 --name mysensor sensornew
Forwarder: docker run --rm --network hw03 --name subscriber forwarder

On cloud:
Cloud Broker: docker run --name mosquittocloud --network hw03 -p 1883:1883 -d brokercloud
Image Processor / Saver: docker run -v /mnt/mybucket/hw03:/hw03_faces  --network hw03 --name saver -it  --entrypoint sh saver

Within the saver the following commands were run:
Python saver.py
Control c to exit out of the saver.py script

On the cloud outside the docker containers, sync the mounted directory with object storage
s3cmd sync /mnt/mybucket/ s3://lab02-cos-standard-neha/hw03/

