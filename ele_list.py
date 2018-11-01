#Implement a program to print the elements of a list.
def ele_length(my_list):
	count = 0
	for i in my_list:
		count += 1
	return count

def main():

	my_list =  ['ab', 'bc','ca', 'cd' , 'acd', 45.2]
	print(my_list)
	print("\nlist length is :",ele_length(my_list))


if __name__=="__main__":
	main()

	