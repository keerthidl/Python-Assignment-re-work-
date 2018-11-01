#Implement function to find the string length without using standard library.

def str_length(string):
	count=0
	for i in string:
		count +=1

	return count


def main():
	
	string = input("Enter the string: \t")

	print("length is :", str_length(string))

if __name__ == '__main__':
	main()