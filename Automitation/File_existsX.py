import os

def main():
	
	if  os.path.exists("Demo.txt"):
		print("File is preasent")
	else:
		print("File is not preasent")

if __name__ == "__main__":
	main()
