from SimpleCV import *
import time
import sys
import numpy as np

# Variables
pixel_steps=5
vcy_range = 60
vcy_free = 0.7

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

print('Everything is ready. Starting to track!')

img = Image("/home/marcos/workspace/parking_lot-0.0/img.png")

# Drawn retangle vacancy area
retangle_layer = DrawingLayer((img.width, img.height))
retangle_dim = (width, height)
retangle_center = (left+(width/2), top+(height/2))	
retangle = retangle_layer.centeredRectangle(retangle_center, retangle_dim)
img.addDrawingLayer(retangle_layer)

vcy=0
points = []
cont = 0
for y in range(top, top+height, pixel_steps):
	for x in range(left, left+width, pixel_steps):
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
		cont = cont + 1
# Find out if the spot is free
print("")
print(str(cont)+" points")
print(str(vcy)+" free spots")

result = [(left,top), (left,top+height), (left+width,top+height), (left+width,top)]

if (vcy > 0.7*cont):
	print("Vacancy is free!")
	img.dl().polygon(result, filled=True, color=Color.GREEN)
	img.show()
	img.save("/home/marcos/workspace/parking_lot-0.0/img.png")
	sys.exit(0)
else:
	print("Vacancy is filled!")
	img.dl().polygon(result, filled=True, color=Color.RED)
	img.show()
	img.save("/home/marcos/workspace/parking_lot-0.0/img.png")
	sys.exit(1)

