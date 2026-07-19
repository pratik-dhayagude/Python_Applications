import os

def main():
	ret = os.path.exists("Demo.txt")
	if ret:
		print("File is preasent")
	else:
		print("File is not preasent")

if __name__ == "__main__":
	main()
