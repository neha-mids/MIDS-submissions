Neha Kumar  
Section 1 MIDS W251


Link to an example of a detected face in S3: https://lab02-cos-standard-neha.s3.us-east.cloud-object-storage.appdomain.cloud/hw07/hw07/face_15919310501500268

1. I used the mobilenet SSD detector, trained on the WIDERFACE dataset and has an AUC of 0.8487 (100% MobileNet SSD) [source](https://arxiv.org/pdf/1811.11582.pdf)
2. The neural network produced decent results, however I did experience difficultly when I had a very low-res camera. In that situation, the neural network was not confident that it saw a face (the maximum score in a frame with my face was under 0.05). Updating to a higher resolution webcam finally produced confidence intervals that cleared the 0.5 threshold. Moreover, I noticed that by not resizing the image to 300 by 300 I saw a further increase in score, over 0.85 and reaching close to 1.0. Provided a production grade system had higher resolution cameras, this detector can possibly be used, however it will likely not pick up any blurry or background faces. Depending on the application, this may not suit our use case (for example, detecting faces in a crowd or faces at a distance would be a poor application for this network).
3. I get a frame rate of 8-10 FPS (without using TensorRT). The bottleneck is the step where the network actually does the inference on the image to find faces. I expect on TensorRT the frame rate would be much higher (though it may take longer for the video stream to get up and running as optimizing the model on TensorRT takes time)
4. While MobileNet may be a more sophisticated technology, OpenCV was able to detect blurry face images much better.  
