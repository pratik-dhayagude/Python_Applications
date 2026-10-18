class Base1:	
	def Fun(self):
		print("Inside base1 Fun")
			
class Base2:
	
	def Gun(self):
		print("Inside base2 Gun")
			
	
class Derived(Base1,Base2):
	def Sun(self):
		print("Inside derived Sun")
		


dobj = Derived()
dobj.Fun()
dobj.Gun()
dobj.Sun()



