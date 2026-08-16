import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def MarvellousPredictor():

	#
	# Step1 -> Load the data
	#
	x = [1,2,3,4,5]
	y = [3,4,2,4,5]
	
	print("Values of independent variables are:",x)
	print("Values of dependent variables are:",y)
	
	#
	# Step2 = Calculate X bar y Bar
	#
	Sum_X =0
	Sum_Y =0
	
	for i in range(len(x)):
		Sum_X += x[i]
		Sum_Y += y[i]
		
	mean_x = Sum_X /len(x)
	mean_y = Sum_Y /len(y)
	
	
	print("mean_x is:",mean_x)
	print("mean_y is:",mean_y)
	
	
	
def main():
	MarvellousPredictor()

if __name__ == "__main__":
	main()
