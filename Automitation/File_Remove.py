import os

def main():
	try:
		
		os.remove("Demo.txt")
		
	except FileNotFoundError as fobj:
		print("There is no file in the folder")
		

if __name__ == "__main__":
	main()
