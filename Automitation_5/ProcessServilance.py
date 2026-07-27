import psutil
import sys
import os

def main():	
	
	Border = "-"*50
	print(Border)
	print(".....Marvellous Platform Servilance System.....")
	print(Border)
	
	if(len(sys.argv) == 2):
		if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
			print("This automitation script is use to perform")
			print("1:It fetch they information of running process")
			print("2:It fetch information about Primary Storage ram")
			print("3:It fetch Information about Secondary Storage HDD")
			print("4:It fetch information about CPU")
			print("5:It gets Auto schedule periodically")
			print("6:It mentaion all records into log file")
			print("7:It sends they log file through mail periodically")
		elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
			print("Use they Automitation script as :")
			print(f"python {sys.argv[0]} 	Time_Interval Folder_Name ")
			print("Time_Interval : Time in minutes for periodic excution")
			print("Folder_Name : Name of folder")
		else:
			print("Unable to proced as there is no matching arguments")
			print("Please use --h and --u flag for getting more details")
		
	elif(len(sys.argv) == 3):
		pass
	else:
		print("Invalid Arguments")
		print("Unable to proced as arguments are not matching")
		print("Please use --h and --u flag for getting more details")
		
		
	
	print(Border)
	print("Thanku For using Marvellous Servilance system")
	print(Border)

if __name__ == "__main__":
	main()
