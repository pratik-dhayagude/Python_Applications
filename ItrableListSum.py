def SumList(Marks):
	Sum = 0
	for no in Marks:
		print(no)
		Sum = Sum + no
		
	return Sum
		
def main():

	Marks = [78,90,56,98,77]
	
	Ret = SumList(Marks)
	print("Addition is :",Ret)
	print("-"*15)
	Marks[2] = 59
	Ret = SumList(Marks)
	print("Addition is :",Ret)
	
	
	

if __name__ == "__main__":

	main()
