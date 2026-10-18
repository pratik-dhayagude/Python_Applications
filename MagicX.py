class demo:
	def __init__(self,A):
		self.No = A
	def __add__(self,other):
		return self.No + other.No
		
	def __sub__(self,other):
		return self.No - other.No
		
	def __mul__(self,other):
		return self.No * other.No
	def __truediv__(self,other):
		return self.No / other.No
		
		
		
		
	
	
obj1 = demo(11)
obj2 = demo(21)
print(obj1+obj2) #obj1.__add__(obj2) -> __add__(obj1,obj2)
print(obj1-obj2)
print(obj1*obj2)
print(obj1/obj2)
		
