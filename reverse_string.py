#Implement a program to reverse a string (without standard librar function)

def reverse(string):
	return string[::-1]

def main():
	print(reverse(input("\nEnter the string: \n"))) 


if __name__ == "__main__":
	main()


