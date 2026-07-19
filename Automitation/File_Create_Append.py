def main():
	try:
		fobj = open("Demo.txt","a")
		print("File get opend")
		fobj.write(" pune Maharashtra")
		fobj.close()
	except FileNotFoundError as fobj:
		print("There is no file in the folder")
		

if __name__ == "__main__":
	main()
