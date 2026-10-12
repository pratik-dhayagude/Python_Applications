import threading
import time

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

	

	tobj1 = threading.Thread(target = Sum_Even,args=(100000000,))
	tobj2 = threading.Thread(target = Sum_Odd,args=(100000000,))
	start_Time = time.perf_counter()
	tobj1.start()
	tobj2.start()
	
	End_Time = time.perf_counter()
	
	print(f"Time Will be {End_Time-start_Time:.4f}")

	
	
	
	
	
if __name__ == "__main__":
	main()
