import time
import multiprocessing
import os
def Calculate_Power(No):
	print("Process is running with pid :",os.getpid())
	Pow = 0
	for i in range(1,No+1):
		Pow = Pow + i ** 3
		
	return Pow
		
def main():
	
	Data = [10000000,20000000,30000000,40000000,50000000]
	Result = []
	
	Start_Time = time.perf_counter()
	
	pobj = multiprocessing.Pool()
	Result = pobj.map(Calculate_Power,Data)
	pobj.close()
	pobj.join()
	End_Time = time.perf_counter()
		
		
	print("Result is :")
	print(Result)
	
	
	print(f"Time Riquired :{End_Time-Start_Time:.4f}")
	
		
	
	

if __name__ == "__main__":
	main()
