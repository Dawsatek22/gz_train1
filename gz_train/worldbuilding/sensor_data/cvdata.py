import cv2
import numpy as np
import os
import argparse
 
# Arg Parser to set the dataset path
parser = argparse.ArgumentParser()
parser.add_argument(' worldbuilding/sensor_data --path', type=str, required=True, help='Segmentation Dataset Path')
args = parser.parse_args()
 
# dataset path
path = args.path
 
# paths of images folders
imageDir = os.path.join(path, "images")
boxesDir = os.path.join(path, "boxes")
 
imagesPaths = sorted(os.listdir(imageDir))
boxesPaths = sorted(os.listdir(boxesDir))
 
imagesPaths = [os.path.join(imageDir, path) for path in imagesPaths]
boxesPaths = [os.path.join(boxesDir, path) for path in boxesPaths]
 
for imagePath, boxesPath in zip(imagesPaths, boxesPaths):
    boxesFile = open(boxesPath)
    boxesLines = boxesFile.readlines()
 
    image = cv2.imread(imagePath)
    width, height = image.shape[1], image.shape[0]
 
    del boxesLines[0]
    for box in boxesLines:
        box = box.split(',')
        label = float(box[0])
        x     = float(box[1])
        y     = float(box[2])
        w     = float(box[3])
        h     = float(box[4])
 
        cv2.rectangle(image, (int(x-w/2), int(y-h/2)), (int(x+w/2), int(y+h/2)), (0,255,0), 3)
 
    print("")
    cv2.imshow("image", image)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()
        break