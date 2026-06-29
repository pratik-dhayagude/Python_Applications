def BigBazar():

	print('Inside Big Bazar')
	def Amul():
		print('Inside Amul')

def main():
	BigBazar() #Allowed 
	Amul()#Error
	BigBazar.Amul() #Error
	
	

	
if __name__ == "__main__":

	main()
