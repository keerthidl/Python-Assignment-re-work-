#Implement a program for finding a square of a number. (without using standard api)

def square(number):
	return number*number

def main():
	number=int(input("enter the number: "))
	print("square of ", "number is: ", square(number))


if __name__ == '__main__':
	main()

