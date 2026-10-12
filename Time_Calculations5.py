import time

def Factorial(No):
	Fact=1
	for i in range(1,No+1):
		Fact = Fact* i
		
	return Fact
			
		


def main():

	print("Enter the number:")
	No = int(input())
	
	start_Time = time.perf_counter()
	Ret = Factorial(No)
	print(f"Factorial of the {No}  will bs {Ret}")
	end_Time = time.perf_counter()
	print(f"Time riquired :{end_Time - start_Time:5f} seconds")
	

if __name__ == "__main__":
	main()
