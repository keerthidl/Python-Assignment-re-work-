#. Implement a program to convert the input string to upper case (without using standard library

def main():

	string = input("Enter the string : ")

	for i in range (0,len(string)):

		x = ord(string[i])
		if x>=97 and x<=122:
			x=x-32

		y=chr (x)
		print(y)

if __name__ == '__main__':
	main()