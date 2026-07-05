def Factorial(No):
	Fact=1
	for i in range(1,No+1):
		Fact = Fact* i
		
	return Fact
			
		


def main():

	print("Enter the number:")
	No = int(input())
	
	Ret = Factorial(No)
	print("Factorial of the given number will bs :",Ret)
	

if __name__ == "__main__":
	main()
