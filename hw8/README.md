Neha Kumar  MIDS W251 Section 1

Part 1:  
1. I annotated 374 images
2. I annotated 295 instances of the Millennium Falcon and 216 instances of TIE fighters
3. The annotation of a large dataset should be split across multiple annotators if it should be done manually. Perhaps something like Mechanical Turk would be helpful. Once a subset of images have been annotated, we could train a model to aid with the annotation task. If the model returns an annotation with a confidence lower than a predetermined threshold, it goes to a human annotator to double check. This offloads some of the manual work.
4. Augmentations would also need to be applied to the annotation box in order to enhance the dataset


Part 2:
1. Flip: mirrors the image either horizontally or vertically
2. Rotation: spins the object about the center (rotates) by a certain number of degrees)
3. Scale: Zooms in and out of the image
4. Crop: Selects a subsection of the original image
5. Translate: shifts the image in a specified direction by a specified amount
6. Noise: adds random artifacts into the image


Part 3:
1. For Audio Annotations, we need the start and end times of the annotation and the classes of the annotations.
