def SumList(Marks):
	Sum = 0
	for no in Marks:
		print(no)
		Sum = Sum + no
		
	return Sum
		
def main():

	Marks = []
	Marks.append(11)
	Marks.append(21)
	Marks.append(51)
	Marks.append(101)
	
	Ret = SumList(Marks)
	print("Addition is :",Ret)
	
	
	
	

if __name__ == "__main__":

	main()
