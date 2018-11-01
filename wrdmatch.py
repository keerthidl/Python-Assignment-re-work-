#Implement a program to check the elements in the list has word "SOIS"

def word_exists(element, args):
	if element in args:
		return True
	else:
		return False


def main():
	n = 5
	print("Enter ", n, " list elements")
	word_list = list()
	for i in range(n):
		word_list.append(input("Enter " + str(i+1) + " list element: \t"))


	if word_exists("SOIS", word_list):
		print("\nSOIS found in list\n")
	else:
		print("\nSOIS not found in list\n")


if __name__=="__main__":
	main()