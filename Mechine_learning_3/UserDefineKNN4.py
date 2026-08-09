import math
import numpy as np


def MarvellousEucDistance(P1,P2):

	Ans = math.sqrt((P1["X"]-P2["X"])**2 + (P1["Y"]-P2["Y"])**2)
	
	return Ans
	


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
	
	new_point = {"X":3,"Y":3}
	
	print("Distances of all points")
	
	for d in Data:
		print(MarvellousEucDistance(d,new_point))
		
		
	print(border)
		
	
	
	

def main():

	MarvellousClassifier()

	

	

if __name__ == "__main__":
	main()
