#Implement a program to find the euclidean distance of two points. 

import math

def distancebtwpoints(x1,x2,y1,y2):
	distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
	return distance
print distancebtwpoints(x1,y1,x2,y2)