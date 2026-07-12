def Addition(No1,No2):
	return No1+No2
	
def Substraction(No1,No2):
	return No1-No2
	
	
def main():
	print("Enter first Number")
	No1 = int(input())
	
	print("Enter first Number")
	No2 = int(input())
	
	Ret = Addition(No1,No2)
	print("Addition is :",Ret)
	
	Ret = Substraction(No1,No2)
	print("Substraction is :",Ret)
	
	
	
if __name__ == "__main__":
	main()
