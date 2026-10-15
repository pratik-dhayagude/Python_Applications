class Demo:
	def __init__(self):
		print("Inside constructur")
		
	def __del__(self):
		print("Inside Destructor")
		
		
		
obj1 = Demo()
obj2 = Demo()

print("End of application")
