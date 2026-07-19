def main():
	try:
		fobj = open("Demo.txt","r")
		print("File get opend")
		data = fobj.read()
		print("File data :",data)
		fobj.close()
	except FileNotFoundError as fobj:
		print("There is no file in the folder")
		

if __name__ == "__main__":
	main()
