class Demo:
	# Class Variable
	Value1 = 10
	Value2 = 20
	
	def __init__(self):
		self.No1 = 11
		self.No2 = 21
		
		
	#Instamce Method
	def Fun(self):
		print("Inside Instance method Named as Fun")
		print(self.No1)
		print(self.No2)
		print(Demo.Value1)
		print(Demo.Value2)
		
	@classmethod
	def Gun(cls):
		print("Inside Instance method Named as Gun")
		#print(Demo.No1)  Not Allowed
		#print(Demo.No2)
		print(Demo.Value1)
		print(Demo.Value2)
		
	
#Call with object	
Demo.Gun()
dobj = Demo()
dobj.Gun


	
		
	
