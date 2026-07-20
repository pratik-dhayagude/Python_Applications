import sys

import os
def DirectoryScanner(DirectoryPath):
	print("Log file is created at they location")
	
	fobj = open("MarvellousLog.txt","w")
	fobj.write("Marvellous Automatation Script\n")
	fobj.write(" Files from the directory are\n:")
	
	for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
	
		for fname in FileName:
			fobj.write(fname+"\n")
			
	fobj.close()
			
	

def main():
	Border = "-"*40
	print(Border)
	print("Marvellous Automatation Script")
	print(Border)
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
			DirectoryScanner( sys.argv[1])
			
			
	print(Border)
	print("Thanku for using Marvellous Automitation Script")
	print(Border)

if __name__ == "__main__":
	main()
