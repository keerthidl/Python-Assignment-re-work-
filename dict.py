# Implement a program to create a dictionary of students with Registration number and names. 
#Perform the two operations, insert and delete.


def main():

	print(" enter 5 student details ")

	students=dict()


	for i in range(5):
		students[input("enter the Registration number: \n")]=input("enter the student name: \n")



	print(students)

	students.pop(input("enter the Registration number to delete the student details: ")) 

	print(students)


if __name__ == '__main__':
	main()
