# Implement a program to get three values from CLA and print the sum of them.

import sys

def add(a,b,c):
	return a+b+c

def main(argv):

	if (len(argv)>=3):
		print("sum is :", add(int(argv[0])+int(argv[1])+int(argv[2], '\n')))
	else:
		print("Usage: CLA_sum.py <number1> <number2> <number3>")
		

	return


if __name__ == '__main__':
	main(sys.argv[1:])
