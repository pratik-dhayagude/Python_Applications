def main():
	try:
		open("Demo.txt","w")
		print("File get opend")
	except FileNotFoundError as fobj:
		print("There is no file in the folder")
		

if __name__ == "__main__":
	main()
