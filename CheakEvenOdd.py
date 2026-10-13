def CheakEvenOdd(No):
	if(No%2==0):
		return True
	else:
		return False

def main():
	print("Enter the Number")
	No = int(input())
	Ret = CheakEvenOdd(No)
	
	if(Ret):
		print("Number is even")
	else:
		print("Number is Odd")
	
if __name__ == "__main__":
	main()
