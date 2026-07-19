import os

def main():
	for FolderName,SubFolder,FileName in os.walk("/"):
		print("Folder name :",FolderName)
		
		for fldName in SubFolder:
			print(fldName)

		for FileName in FileName:
			print(FileName)	
if __name__ == "__main__":
	main()
