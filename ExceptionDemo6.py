def main():
	
	Ans = 0
	try:
	
		print("Enter first Number")
		No1 = int(input())
	
		print("Enter Second Number")
		No2 = int(input())
	
		Ans = No1 / No2
		print("Division is successful")
	except ZeroDivisionError as zobj:
		print("Exception occur due to second operand is zero:",zobj)
		
	except ValueError as vobj:
		print("Exception is occur due to second operand is str:",vobj)
		
	except Exception as eobj:
		print("Exception ocuured",eobj)
		
	finally:
		print("Inside finally block:")
		
	
	print("Result is :",Ans)


if __name__ == "__main__":
	main()
