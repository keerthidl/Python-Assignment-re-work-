#Implement a program to write a line from the console to a file.

def main():
	file = open("write_file.txt","w")
	file.write("Be aware of humans!!!!!....")



	file.close()

if __name__ == '__main__':
	main()
