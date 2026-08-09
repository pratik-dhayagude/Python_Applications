def MarvellousClassifier():
	
	border = "-"*30
	
	Data = [
	{"Point":"A","X":1,"Y":2,"Label":"Red"},
	{"Point":"B","X":2,"Y":3,"Label":"Red"},
	{"Point":"C","X":3,"Y":1,"Label":"Blue"},
	{"Point":"D","X":5,"Y":6,"Label":"Blue"}
	]
	
	print(border)
	print("Marvellous KNN Classifier")
	print(border)
	
	for i in Data:
		print(i)
	
	print(border)
	

def main():

	MarvellousClassifier()

	

	

if __name__ == "__main__":
	main()
