#Implement a program with functions, for finding the area of circle, triangle, square.

import math

class Area:

	
	def circle(radius):
		pi = 3.1415
		return (pi * (radius * radius))

	
	def triangle(height, base):
		return ((height * base)/2)

	
	def square(side):
		return (side * side)

from area import Area

def main():

	print("\n1 - Area of Circle\n")
	print("2 - Area of Triangle\n")
	print("3 - Area of Square\n")
	

	choice = int(input("\nEnter your choice:\t"))
		
	if choice == 1:

			
		radius = float(input("\nEnter radius of the Circle:\t"))
		print("\nArea is : " + str(Area.circle(radius)))

			

	if choice == 2:

			
		base = float(input("\nEnter base of the Triangle:\t"))
		height = float(input("\nEnter height of the Triangle:\t"))
		print("\nArea is : " + str(Area.triangle(height, base)))

			

	if choice == 3:

			
		side = float(input("\nEnter a side of the Square:\t"))
		print("\nArea is : " + str(Area.square(side)))



if __name__=="__main__":
	main()