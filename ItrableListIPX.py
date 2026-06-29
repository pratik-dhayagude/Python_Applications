def SumList(Marks):
	Sum = 0
	for no in Marks:
		print(no)
		Sum = Sum + no
		
	return Sum
		
def main():

	Marks = []
	print("Enter they marks 5")
	no = int(input())
	Marks.append(no)
	no = int(input())
	Marks.append(no)
	no = int(input())
	Marks.append(no)
	no = int(input())
	Marks.append(no)
	
	
	
	
	
	
	Ret = SumList(Marks)
	print("Addition is :",Ret)
	
	
	
	

if __name__ == "__main__":

	main()
