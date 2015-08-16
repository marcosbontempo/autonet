from SimpleCV import *
import time
import sys
import numpy as np

camera_index=0
cam = Camera() 
time.sleep(1)
img = cam.getImage()
#img.show()
img.save("/home/marcos/workspace/parking_lot-0.0/img.png")
img.save("/home/marcos/workspace/parking_lot-0.0/original.png")
