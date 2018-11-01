#Implement a function to count the number of vowels present in the file. 

def vowel_count(string):
	vowel_count = 0
	vowel = ['a','e','i','o','u']
	for i in string:
		if i in vowel:
			vowel_count += 1


	return vowel_count


def main():
	file = open("vowel_count.txt")
	text =file.read()
	file.close()


	print(" vowel count in vowel_count.txt: ", vowel_count(text))

if __name__ == "__main__":
	main()