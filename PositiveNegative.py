def PositiveNegative(iNo):

	if iNo > 0:
		return 1
	elif iNo == 0:
		return 2
	else:
		return 3
		
	 	

def main():

	print("Enter they first number")
	iNo = int(input())
	
	iRet = PositiveNegative(iNo)
	if(iRet ==1 ):
		print("Number is positive")
	elif(iRet == 2):
		print("number is zero")
	else:
		print("Number is negative")
	
		
		
	
	
	

if __name__ == "__main__":
	main()

