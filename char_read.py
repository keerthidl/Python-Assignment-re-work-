#Implement a program to read alternative characters in the file. 
def main():

	file = open("char_read.txt")
	text = file.read()

	print(text[::3])

	#important
	file.close()

if __name__=="__main__":
	main()