def Factorial(No):
	Fact=1
	for i in range(1,No+1):
		Fact = Fact* i
		
	return Fact
			
		


def main():

	print("Enter the number:")
	No = int(input())
	
	Ret = Factorial(No)
	print(f"Factorial of the {No}  will bs {Ret}")
	

if __name__ == "__main__":
	main()
