def Largest(iNo1,iNo2):
	if(iNo1>iNo2):
		return 1
	elif(iNo2>iNo1):
		return 2


def main():

	print("Enter they first number")
	iNo1 = int(input())
	
	print("Enter they second number")
	iNo2 = int(input())
	
	iRet = Largest(iNo1,iNo2)
	
	if(iRet == 1):
		print("The first number is large")
		
	else:
		print("The second number is large")
	
	 	
	
if __name__ =="__main__":
	main()

	
