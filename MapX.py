def CheakEven(No):
	return(No%2==0)

def Increament(No):
	return No + 1
def main():
	
	Data = [13,12,8,10,11,20]
	
	print("Input data is :",Data)
	
	fData = list(filter(CheakEven,Data))
	print("Data Afterfilter :",fData)
	
	mData = list(map(Increament,fData))
	print("Data After Mapping:",mData)
	
	
	
	
	

if __name__ == "__main__":
	main()
