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
	
	
		
	mean_x = np.mean(x)
	mean_y = np.mean(y)
	
	
	print("mean_x is:",mean_x)
	print("mean_y is:",mean_y)
	
		
def main():
	MarvellousPredictor()

if __name__ == "__main__":
	main()
