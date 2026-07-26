import sys
import os 
import hashlib

def CalculateCheakSum(FileName):
	fobj = open(FileName,"rb")
	hobj = hashlib.md5()
	
	Buffer = fobj.read(1024)
	while(len(Buffer) > 0):
		hobj.update(Buffer)
		Buffer = fobj.read(1024)
		
	fobj.close()
	
	return 	hobj.hexdigest()
	
def FindDuplicate(directoryName):
	
	
	Ret = False
	
	Ret = os.path.exists(directoryName)
	
	if Ret == False:
		print("Path is invalid")
		return 
	
	Ret = os.path.isdir(directoryName)
	
	if Ret == False:
		print("There is no such directory")
		return
	
	Duplicate = {}
	Unique = 0
	Same = 0
	
	for Folder, SubFolder , FileName in os.walk(directoryName):
		for fname in FileName:
			fname = os.path.join(Folder,fname)
			CheakSum = CalculateCheakSum(fname)
			print(f"{fname}:{CheakSum}")
			if CheakSum in Duplicate:
				
				Same += 1
				Duplicate[CheakSum].append(fname)
			else:
				Unique += 1
				Duplicate[CheakSum] = [fname]
				
	print("Unique Files found:",Unique)
	print("Same Variable:",Same)
	
	
		
def main():
	FindDuplicate("Test")
	

if __name__ == "__main__":
	main()
