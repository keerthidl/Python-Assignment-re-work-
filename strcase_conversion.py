# Implement a progam to convert the input string to inverse case(upper->lower, lower->upper) ( without using standard library)

def main():

	string = input("Enter the string : ")

	for i in range (0,len(string)):

		x = ord(string[i])
		if x>= 65 and x<=96:
			x=x+32
		elif x>=97 and x<=122:
			x=x-32
		else: 
			print('inavalid input')

		y=chr (x)
		print(y)

if __name__ == '__main__':
	main()