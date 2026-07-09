import multiprocessing
import time
import os


# 2 + 4 + 6 + 8 = 20
def Sum_Even(No):
	print(f"Pid :{os.pid()} PPID:{os.ppid()}")
	Sum=0
	for i in range(2,No,2):
		Sum += i
		
	print("Summation of even",Sum)
		
			
			
		
def Sum_Odd(No):
	print(f"Sum Odd Pid :{os.pid()} PPID:{os.ppid()}")
	Sum=0
	for i in range(1,No,2):
		Sum += i
		
	print("Summation of Odd",Sum)
		
	
	
	
	
	

def main():

	
	print(f"main Pid :{os.pid()} PPID:{os.ppid()}")
	start_Time = time.perf_counter()

	tobj1 = multiprocessing.Process(target = Sum_Even,args=(100,))
	tobj2 = multiprocessing.Process(target = Sum_Odd,args=(100,))
	
	tobj1.start()
	tobj2.start()
	
	End_Time = time.perf_counter()
	
	print(f"Time Will be {End_Time-start_Time:.4f}")

	
	
	
	
	
if __name__ == "__main__":
	main()
		

