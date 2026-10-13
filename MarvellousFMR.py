CheakEven = lambda No:(No%2==0)

Increament=lambda No: No + 1
	
Sum=lambda No1,No2: No1+No2

def FilterX(Task,Elements):
	Result = list()
	for no in Elements:
		Ret = Task(no)	#call to cheak Evevn
		if(Ret):
			Result.append(no)
			
	return Result
	
def mapX(Task,Elements):
	Result = list()
	
	for no in FilterData:
		Ret = Task(no)
		Result.append(Ret)
		
def ReduceX(Task,Elements):

	Sum = 0
	
	for no in Elements:
		
		Sum = Task(Sum,no)
		
	return Sum
		
			
def main():
	
	Data = [13,12,8,10,11,20]
	
	print("Input data is :",Data)
	
	fData = list(FilterX(CheakEven,Data))
	print("Data Afterfilter :",fData)
	
	mData = list(mapX(Increament,fData))
	print("Data After Mapping:",mData)
	
	rData = (reduceX(Sum,mData))
	print("Data After Reducing:",rData)
	
if __name__ == "__main__":
	main()
