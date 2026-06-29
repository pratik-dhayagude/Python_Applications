from functools import reduce

CheakEven = lambda No:(No%2==0)

Increament=lambda No: No + 1
	
Sum=lambda No1,No2: No1+No2
	
def main():
	
	Data = [13,12,8,10,11,20]
	
	print("Input data is :",Data)
	
	fData = list(filter(CheakEven,Data))
	print("Data Afterfilter :",fData)
	
	mData = list(map(Increament,fData))
	print("Data After Mapping:",mData)
	
	rData = (reduce(Sum,mData))
	print("Data After Reducing:",rData)
	
if __name__ == "__main__":
	main()
