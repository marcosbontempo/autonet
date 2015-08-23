from SimpleCV import *
import time
import sys
import numpy as np

# Variables
camera_index=0
pixel_steps=5
vcy_range = 20
vcy_free = 70

cam = Camera(camera_index)
if len(sys.argv) > 1:
	display = sys.argv[1]
	top = int(sys.argv[2])
	left = int(sys.argv[3])
	width = int(sys.argv[4])
	height = int(sys.argv[5])
	vcy_red = int(sys.argv[6])
	vcy_green = int(sys.argv[7])
	vcy_blue = int(sys.argv[8])
else:
	print ("usage: track.py display top left width height")
	sys.exit(1)
time.sleep(1)
background = cam.getImage()

print('Everything is ready. Starting to track!')

img = cam.getImage()

# Drawn retangle vacancy area
retangle_layer = DrawingLayer((img.width, img.height))
retangle_dim = (width, height)
retangle_center = (left+(width/2), top+(height/2))	
retangle = retangle_layer.centeredRectangle(retangle_center, retangle_dim)
img.addDrawingLayer(retangle_layer)

vcy=0
points = []
for y in range(top, top+height+pixel_steps, pixel_steps):
	for x in range(left, left+width+pixel_steps, pixel_steps):
		points.append((x, y))
		# color distances from cars
		(red, green, blue) = img.getPixel(x, y)
		print("R="+str(red)+" G="+str(green)+" B="+str(blue))

		if display:
			to_show = locals()[display]
			to_show.drawPoints(points)
			to_show.show()

		if (red > vcy_red-vcy_range) and (red < vcy_red+vcy_range) and (green > vcy_green-vcy_range) and (green < vcy_green+vcy_range) and (blue > vcy_blue-vcy_range) and (blue < vcy_blue+vcy_range):
			print("Vacancy spot: "+str(x)+"x"+str(y))
			vcy += 1
# Find out if the spot is free
print("")
print(str(vcy)+" free spots")
if (vcy > 70):
	print("Vacancy is free!")
	sys.exit(0)
else:
	print("Vacancy is filled!")
	sys.exit(1)

