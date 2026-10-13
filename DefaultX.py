def Area(Radius=1,PI): # Error

	R = PI * Radius * Radius
	return R

def main():

	Ret = Area(3.14)
	print(Ret)
	
	Ret = Area(10.5,3.14)
	print(Ret)
	

if __name__ == "__main__":

	main()
