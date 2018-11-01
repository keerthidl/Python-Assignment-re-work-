#Create a list with 5 branches in SOIS. Try to do the following operations a) append b) insert c) sort d) reverse sort
def main():

	branches = ["EWT", "EMBEDDED SYSTEMS", "VIR", "IOT", "BIGDATA"]

	

	print(branches)

	print("\nAdding automotive embedded systems\n")
	branches.append("AUTOMOTIVE EMBEDDED SYSTEMS")
	print(branches)

	print("Adding inserting medical software  at the postion 3")
	branches.insert(2, "MEDICAL SOFTWARE")
	print(branches)


	print("Sort list ")
	branches.sort()
	print(branches)


	print("sort list descending")
	branches.sort(reverse = True)
	print(branches)


if __name__=="__main__":
	main()