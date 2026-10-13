def Arithematic(iNo1,iNo2):
	Mult = iNo1 * iNo2
	Div = iNo1 /iNo2
	
	return Mult,Div

	

	

def main():

	Value1 = int(input("Enter first number..."))
	
	Value2 = int(input("Enter second number...."))
	
	Ret1,Ret2 = Arithematic(Value1,Value2)
	
	print("Multiplication is :",Ret1,"Division is:",Ret2)

	
if __name__ == "__main__":

	main()
