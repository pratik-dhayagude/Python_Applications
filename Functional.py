Addition = lambda No1,No2 : No1+No2

Substraction = lambda No1,No2:No1-No2


def main():
	No1 = int(input("Enter First Number:"))
	No2 = int(input("Enter Second Number:"))
	
	Ret = Addition(No1,No2)
	print("Addition:",Ret)
	
	Ret = Substraction(No1,No2)
	print("Substraction:",Ret)
	
if __name__ == "__main__":
	main()
