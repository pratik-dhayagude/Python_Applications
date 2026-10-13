def Largest(iNo1,iNo2,iNo3):
	iMax = iNo1

	if iNo2>iNo1 and iNo2 > iNo3 :
		iMax = iNo2
	elif iNo3 > iNo1 and iNo3 >iNo2 :
		iMax = iNo3
		
	return iMax


def main():

	print("Enter they first number")
	iNo1 = int(input())
	
	print("Enter they second number")
	iNo2 = int(input())
	
	print("Enter they second number")
	iNo3 = int(input())
	
	iRet = Largest(iNo1,iNo2,iNo3)
	
	print("Largest Number is ",iRet)
	 	
	
if __name__ =="__main__":
	main()

	
