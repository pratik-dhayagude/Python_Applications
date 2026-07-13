from abc import ABC,abstractmethod

class base(ABC):

	@abstractmethod
	def Addition(self,No1,No2):
		pass
		
	
	
	
class derived(base):
	pass
	
	
dobj = derived()	#Error

