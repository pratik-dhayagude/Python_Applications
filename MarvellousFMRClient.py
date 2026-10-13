from MarvellousLibrary import *

CheakEven = lambda No:(No%2==0)

Increament = lambda No: No + 1
	
Sum = lambda No1,No2: No1+No2

		
			
def main():
	
	Data = [13,12,8,10,11,20]
	
	print("Input data is :",Data)
	
	fData = list(FilterX(CheakEven,Data))
	print("Data Afterfilter :",fData)
	
	mData = list(MapX(Increament,fData))
	print("Data After Mapping:",mData)
	
	rData = reduceX(Sum,mData)
	print("Data After Reducing:",rData)
	
if __name__ == "__main__":
	main()
