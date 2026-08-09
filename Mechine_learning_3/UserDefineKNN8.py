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
		d["Distance"]=(MarvellousEucDistance(d,new_point))
		
		
	for d in Data:
		print(d)
		
		
	print(border)
	
	
	Sorted_Data = sorted(Data,key = lambda item : item["Distance"])
	
	print("Sorted Data :")
	
	for d in Sorted_Data:
		print(d)
		
	print(border)
	
	print(border)
	
	K = 3

	near = Sorted_Data[:K]
	print(border)
	print("Nearest 3 nabours are:")
	
	print(border)
	
	for d in near:
		print(d)
		
		
	print(border)
	
	# voting	
	
	Vot ={}
	
	for neg in near:
		label = neg["Label"]	
		
		Vot[label] = Vot.get(label,0)+1
		
	
	print(border)
	print("Votig Result is:")
	print(border)
	
	for d in Vot:
		print("Name:",d,"Number off vots:",Vot[d])
		
	print(border)
	

def main():

	MarvellousClassifier()

	

	

if __name__ == "__main__":
	main()
