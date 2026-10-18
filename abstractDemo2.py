from abc import ABC,abstractmethod

class base(ABC):

	@abstractmethod
	def Addition(self,No1,No2):
		pass
		
	
	
	
class derived(base):
	def Addition(self,No1,No2):
		return No1+No2
	
	
	
dobj = derived()	
Ret = dobj.Addition(11,21)
print("Addition is :",Ret)
