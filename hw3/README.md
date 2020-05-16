Homework Questions:

- Link to binarized face images on the cloud: https://lab02-cos-standard-neha.s3.us-east.cloud-object-storage.appdomain.cloud
- The topic for the local mqtt was named imagelocal while the topic for the cloud mqtt was called imageremote. This describes what is being transmitted (images) and where (locally or to the remote)  were both named "testtopic."
- QoS of 0 (best attempt) was used as this was a streaming application. If one message was dropped, we want to continue with streaming subsquent messages without interruption

Commands run to spin up docker containers on the Jetson:
Local Broker:  `docker run --name mosquitto --network hw03 -p 1883:1883 -d broker`
Sensor (Camera component): `docker run --privileged --rm --network hw03 --name mysensor sensornew`
Forwarder: `docker run --rm --network hw03 --name subscriber forwarder`

On cloud:
Cloud Broker: `docker run --name mosquittocloud --network hw03 -p 1883:1883 -d brokercloud`
Image Processor / Saver: `docker run -v /mnt/mybucket/hw03:/hw03_faces  --network hw03 --name saver -it  --entrypoint sh saver`

Within the saver the following commands were run:
`Python saver.py`
Control c to exit out of the saver.py script

On the cloud outside the docker containers, sync the mounted directory with object storage
`s3cmd sync /mnt/mybucket/ s3://lab02-cos-standard-neha/hw03/`

