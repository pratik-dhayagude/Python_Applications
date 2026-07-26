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
	
	
	for Folder, SubFolder , FileName in os.walk(directoryName):
		for fname in FileName:
			fname = os.path.join(Folder,fname)
			CheakSum = CalculateCheakSum(fname)
			
			if CheakSum in Duplicate:
				
				
				Duplicate[CheakSum].append(fname)
			else:
				
				Duplicate[CheakSum] = [fname]
				
	return Duplicate
	
def DeleteDupliacte(DirectoryName):

	MyDict = FindDuplicate(DirectoryName)
	
	Count = 0
	TotalDeleted =0
	
	
	
	Result = list(filter(lambda X : len(X) > 1,MyDict.values()))
	
	for Value in Result:
		
		for SubValue in Value:
			
			Count += 1
			if(Count > 1):
				print("Duplicate Found:",SubValue)
				TotalDeleted +=1
				
		
		Count = 0
	print("Dleted Files:",TotalDeleted )	
				
			
				
			
	
	
	

				
	

	
	
		
def main():
	DeleteDupliacte("Test")
	
	

if __name__ == "__main__":
	main()
