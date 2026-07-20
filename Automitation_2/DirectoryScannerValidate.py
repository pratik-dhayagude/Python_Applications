import sys
import time
import os
import schedule
def DirectoryScanner(DirectoryPath = "Marvellous"):
	border = "-"*40
	
	print("Log file is created at they location")
	timeStamp = time.ctime()
	logFileName = "Marvellous%s.log"%(timeStamp )
	logFileName = logFileName.replace(" ","_")
	logFileName = logFileName.replace(":","_")
	
	##Cheaking
	Ret = False
	Ret = os.path.exists(DirectoryPath)
	if(Ret == False):
		print("Marvellous automatation error:There is no such directory with name",DirectoryPath)
		
		return
		
	Ret = os.path.isdir(DirectoryPath)
	if(Ret == False):
		print("Marvellous automitation Error:it is not directory with name:",DirectoryPath)
		return
	
	##Creating
	print("log file gets created with name:",logFileName)
	fobj = open(logFileName,"w")
	
	fobj.write(border+"\n")
	fobj.write("Marvellous Automatation Script\n")
	fobj.write(border+"\n\n")
	
	fobj.write(" Files from the directory are:\n\n")
	fobj.write(border+"\n")
	
	for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
	
		for fname in FileName:
			fobj.write(fname+"\n")
			
	fobj.write(border+"\n")
	fobj.write("Log file gets created as :"+timeStamp)
	fobj.write("\n"+border+"\n")
	
			
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
			
			schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
			while(True):
				schedule.run_pending()
				time.sleep(1)
			
			
			
	print(Border)
	print("Thanku for using Marvellous Automitation Script")
	print(Border)

if __name__ == "__main__":
	main()
