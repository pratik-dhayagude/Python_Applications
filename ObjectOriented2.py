class Arithematic:
	
	def Addition(self,No1,No2): 
		return No1+No2
	
	def Substraction(self,No1,No2):
		return No1-No2
		
		
aobj1 = Arithematic()
print("Enter first Number")
No1 = int(input())

print("Enter first Number")
No2 = int(input())

#Ret = Addition(aobj1,No1,No2)
Ret = aobj1.Addition(No1,No2)
print("Addition is :",Ret)

Ret = aobj1.Substraction(No1,No2)
print("Substraction is :",Ret)
	
