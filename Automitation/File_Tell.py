def main():
	try:
		fobj = open("Demo.txt","r")
		print("File get opend")
		
		print("File offset is :",fobj.tell())
		data = fobj.read(10)
		print("File data :",data)
		print("File offset is :",fobj.tell())
		
		print("File offset is :",fobj.tell())
		data = fobj.read(10)
		print("File data :",data)
		print("File offset is :",fobj.tell())
		
		fobj.close()
		
	except FileNotFoundError as fobj:
		print("There is no file in the folder")
		

if __name__ == "__main__":
	main()
