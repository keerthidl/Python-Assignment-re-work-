# Implment a program with arithmetic functions with  case statements.
def add(x, y):
   return x + y


def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y


def divide(x, y):
   return x / y

def show_choices(): 
	print(" 1 - add")      
	print(" 2 - subtract")       
	print(" 3 - multiply")
	print(" 4 - divide") 


def main():

	show_choices()

	choice = input("Enter choice: ")

	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))

	switch = {

	1: Calculator.add(num1, num2),
    2: Calculator.subtract(num1, num2),
    3: Calculator.multiply(num1, num2),
	4: Calculator.diivde(num1, num2),
		

	}

	print("Answer is", switch.get(choices))

	if __name__ == '__main__':
		main()

