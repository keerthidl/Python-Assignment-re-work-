# Implement a program to create a list with two tuple of fruits and vegetables. Access fruits separately and vegetables separately. 
'''
def main():
	fruit_veggies_list = list()

	fruits = tuple(("apple", "banana", "cherry"))
	veggies = tuple(("chilly", "capcium", "carrot"))

	fruit_veggies_list.append(fruits)
	fruit_veggies_list.append(veggies)

	print(fruit_veggies_list)

	print("\n-----Veggies-----\n")
	for veggie in fruit_veggies_list[1]:
		print(veggie)

	print("\n-----Fruits-----\n")
	for fruit in fruit_veggies_list[0]:
		print(fruit)


if __name__=="__main__":
	main()
'''


def main():
	fruit_vegetables = list()

	fruits = tuple(("apple","watermelon","orange"))
	vegetables = tuple(("carrot","beans","potato"))

	fruit_vegetables.append(fruits)
	fruit_vegetables.append(vegetables)

	print(fruit_vegetables)


	print("\n fruits \n")
	for fruits in fruit_vegetables[0]:
		print(fruits)

	print("\n vegetables\n")
	for vegetables in fruit_vegetables[1]:
		print(vegetables)

if __name__ == '__main__':
	main()