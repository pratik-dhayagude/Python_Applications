from Marvellous import *

def main():
	
	print("Enter they first number")
	iNo1 = int(input())
	print("Enter they second number")
	iNo2 = int(input())
	
	iRet =Addition(iNo1,iNo2) 
	
	print("Ans is ", iRet)
	
	iRet =Substraction(iNo1,iNo2)
	
	print("Sub is ", iRet)
	
	iRet = Multiplication(iNo1,iNo2)
	
	print("Mul is ",iRet)
	
	
	iRet = Division(iNo1,iNo2)
	
	print("Div is ",iRet)	
	
	
	
	
	
	
if __name__ == "__main__":
	main()
	 
