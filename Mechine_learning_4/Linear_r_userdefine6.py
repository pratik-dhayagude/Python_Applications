import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def MarvellousPredictor():

	#
	# Step1 -> Load the data
	#
	X = [1,2,3,4,5]
	Y = [3,4,2,4,5]
	
	print("Values of independent variables are:",X)
	print("Values of dependent variables are:",Y)
	
	#
	# Step2 = Calculate X bar y Bar
	#
	Sum_X =0
	Sum_Y =0
	
	for i in range(len(X)):
		Sum_X += X[i]
		Sum_Y += Y[i]
		
	mean_x = Sum_X /len(X)
	mean_y = Sum_Y /len(Y)
	
	
	print("mean_x is:",mean_x)
	print("mean_y is:",mean_y)
	
	n = len(X) # 5
	
	
	num = 0
	deno = 0
	for i in range(n):
		num = num+((X[i] - mean_x)*(Y[i] - mean_y)) 
		deno = deno + ((X[i]-mean_x)**2)
		
		
		
	M = num / deno
	
	print("value of M is:",M)
	
	
	#
	# Step -> Calculating C
	# Y = M*X + C
	#
	
	
	C = mean_y - (M*mean_x)
	
	print("Value of C will be:",C) 
	
	
	x = np.linspace(1,6,n)
	y = M * x + C
	
	plt.plot(x,y,color = "g",label = "Regeression line")
	plt.scatter(x,y,color = "r",label = "Scatter plot")
	plt.xlabel("Independent variables")
	plt.ylabel("Dependent Variables")
	plt.legend()
	plt.show()
	
	
	
	
def main():
	MarvellousPredictor()

if __name__ == "__main__":
	main()
