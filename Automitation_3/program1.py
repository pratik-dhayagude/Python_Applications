######################################################
#	
# 	Importing riquired libraries
#
######################################################	
import schedule
import os
import shutil
import sys
import time
######################################################
#	FunctionNmae : CheakExtensitation
#	Input :	       From main function 
#	Decription:    It can cheak the extentions of the file and then it 
#		       remove to they respective folder
#	Date :	       20/07/2026
#	Author :       Pratik Dhananjay Dhayagude
#
######################################################	


########################################################################
# New Module Lerned : shutil module 
#		      These module will be help to performing operations 
#		      like copying,moving,renaming 
########################################################################


def CheakExtensitation(DirectoryName):
	print("All Extentions of the file will be remove to they there destination folder")
	for FolderName, SubFolder, FileName in os.walk(DirectoryName):
		for fname in FileName:
		
			#name , extention = here name -> store filename and extention -> store .py 
			name, extension = os.path.splitext(fname)
			
			#here the dot will be removed .py -> py
			Folder = extension[1:]
			
			#they joine the path
			NewFolder = os.path.join(DirectoryName, Folder)
			
			#condition : if the path will be there then the file will be not created if the path is not there,
			# or there is no folder of that name then it will creating they folder
			if not os.path.exists(NewFolder):
				#Creating the new directory 
				os.mkdir(NewFolder)
				
			# Source 
			Source = os.path.join(FolderName, fname)
			
			#Destination
			Destination = os.path.join(NewFolder, fname)
			
			
			#inbuilt method in module shutil this will be move source file into destination 
			shutil.move(Source, Destination)
######################################################
#	FunctionNmae : main
#	Input :	       Command line arguments
#	Decription:    It control the script
#	Date :	       20/07/2026
#	Author :       Pratik Dhananjay Dhayagude
#
######################################################								
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
				
			schedule.every(10).seconds.do(CheakExtensitation,sys.argv[1])
			
			
			while(True):
				schedule.run_pending()
				time.sleep(1)
			
			
			
			
	print(Border)
	print("Thanku for using Marvellous Automitation Script")
	print(Border)
	
######################################################
#	
# 	Starter of the automitation script
#
######################################################	

if __name__ == "__main__":
	main()
