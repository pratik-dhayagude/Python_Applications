def LeepYear(Year):
	if Year % 400 == 0:
		print("It is a leep year")
	elif Year % 4 == 0 and Year %100 != 0:
		print("It is a leep year")
		
	else:
		print("It is not a leep year")
		 


def main():
	print("Enter they year")
	Year = int(input())
	
	LeepYear(Year)
	
	
	
if __name__ == "__main__":
	main()
