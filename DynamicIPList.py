from Arithematic import *
		
		
def main():
	
	size = 0
	
	print("Enter they number of elements:")
	size = int(input())
	
	marks = list()
	
	print("Enter the number of Elements")
	for i in range(size):
		i = int(input())
		marks.append(i)
	
	
	Ret = SumList(marks)
	print("Addition is :",Ret)
	
	print("-"*15)
	
	Ret = MulList(marks)
	print("Multiplication is :",Ret)
	
	
	
	
	
	

if __name__ == "__main__":

	main()
