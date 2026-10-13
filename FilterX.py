def CheakEven(No):
	return(No%2==0)


def main():
	
	Data = [13,12,8,10,11,20]
	
	print("Input data is :",Data)
	
	fData = list(filter(CheakEven,Data))
	print("Data Afterfilter :",fData)
	
	
	
	
	

if __name__ == "__main__":
	main()
