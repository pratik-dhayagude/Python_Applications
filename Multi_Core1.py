def Calculate_Power(No):

	Pow = 0
	for i in range(1,No+1):
		Pow = Pow + i ** 3
		
	return Pow
		


def main():
	
	print("Enter the Number :")
	No = int(input())
	
	Ret = Calculate_Power(No)
	print("Calculated Power Will Be:",Ret)

if __name__ == "__main__":
	main()
