#Implement a program to concatenate two strings.

def concat(string1, string2):
	return string1+string2


def main():

	string1 = input("Enter first string:")
	string2 = input("Enter second string:")

	print( "Result:", concat(string1, string2))

if __name__=="__main__":
	main()