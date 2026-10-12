import threading

# 2 + 4 + 6 + 8 = 20
def Sum_Even(No):
	Sum=0
	for i in range(2,No,2):
		Sum += i
		
	print("Summation of even",Sum)
		
			
			
		
def Sum_Odd(No):
	Sum=0
	for i in range(1,No,2):
		Sum += i
		
	print("Summation of Odd",Sum)
		
	
	
	
	
	

def main():

	Sum_Even(10000)
	Sum_Odd(10000)

	
	
	
	
	
if __name__ == "__main__":
	main()
