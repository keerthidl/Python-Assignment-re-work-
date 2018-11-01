#Implement a program to read a line in a file and print.

def main():
	file = open("read_file.txt")
	print(file.readline())

	file.close()

if __name__ == '__main__':
	main()