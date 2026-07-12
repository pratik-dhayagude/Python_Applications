class Arithematic:
	def __init__(self,A,B):
		self.No1 = A
		self.No2 = B
		
	
	def Addition(self): 
		return self.No1+self.No2
	
	def Substraction(self):
		return self.No1-self.No2
		
		

print("Enter first Number")
No1 = int(input())

print("Enter first Number")
No2 = int(input())

aobj1 = Arithematic(No1,No2)

#Ret = Addition(aobj1,No1,No2)
Ret = aobj1.Addition()
print("Addition is :",Ret)

Ret = aobj1.Substraction()
print("Substraction is :",Ret)
	
