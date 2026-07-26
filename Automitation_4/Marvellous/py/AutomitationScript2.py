import sys


def main():
	if(len(sys.argv)!= 2):
		print("Invalid number of arguments")
	else:
		
		DirectoryName = sys.argv[1]
		print("Directory name is :",DirectoryName)
	

if __name__ == "__main__":
	main()
