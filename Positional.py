def Area(Radius , PI):
	R = PI * Radius * Radius
	return R
	

def main():

	Value = float(input("Enter they number"))
	Ret = Area(Value,3.14)
	print("Area is :",Ret)
	

if __name__=="__main__":
	main()
