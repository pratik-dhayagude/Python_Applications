CheakEvenOdd = lambda No :(No%2==0)
	
		
	

def main():
	print("Enter the Number")
	No = int(input())
	Ret = CheakEvenOdd(No) # No %2 ==0
	
	if(Ret):
		print("Number is even")
	else:
		print("Number is Odd")
	
if __name__ == "__main__":
	main()
