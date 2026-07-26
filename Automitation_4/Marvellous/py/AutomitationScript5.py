import sys


def main():
	print("-------------------------------------------------------------------------")
	print("------------------Marvellous Automatation Script-------------------------")
	print("-------------------------------------------------------------------------")
	if(len(sys.argv)!= 2):
		print("Invalid number of arguments")
		print("Please use --h or --u for more information")
	else:
		
		
		if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
			print("This automatation script is use to travel they directory")
			print("For better usage please cheak --u flag")
		elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
			print("Please execute the script as ")
			print("Python FileName.py DirectoryName")
			print("Directory name should be absoulte path")
		else:
			DirectoryName = sys.argv[1]
			print("Directory name is :",DirectoryName)
			
	print("-------------------------------------------------------------------------")
	print("-----------------Thanku for using Marvellous Automitation Script---------")
	print("-------------------------------------------------------------------------")

if __name__ == "__main__":
	main()
