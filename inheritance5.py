class Base:
	
		
	def Fun(self):
		print("Inside base Fun")
		
		
		
	
class Derived(Base):
	def Sun(self):
		print("Inside derived Sun")
		


dobj = Derived()
dobj.Fun()
dobj.Sun()



