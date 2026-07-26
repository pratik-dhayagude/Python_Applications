def main():
	try:
		fobj = open("Demo.txt","r")
		print("File get opend")
		
		fobj.seek(10,0)
		
		data = fobj.read()
		print(data)
		
	except FileNotFoundError as fobj:
		print("There is no file in the folder")
		

if __name__ == "__main__":
	main()
