import numpy as np


def ReLU(z):
	return max(0,z)
	
def Marvellous_neuron_Forward(inputs,weight,bias):
	
	print("Inputs Are(X):",inputs)
	print("Weigth are(W):",weight)
	print("Bias is(b):",bias)
	
	z = 0
	for i in range(len(inputs)):
		z += (inputs[i]*weight[i])
		
	z += bias
	#z = sum(w * x for w,x in zip(weight,inputs))+bias
	
	print("Weighted Sum (Z):",z)
	
	y = ReLU(z)
	
	return y
	
	
	
	
def main():

	print("---Marvellous Neural Network---")
	
	input = [1.0,2.0,3.0]
	
	weight = [0.6,0.4,-0.2]
	
	bias = 0.5
	
	iRet = Marvellous_neuron_Forward(input,weight,bias)
	print(iRet)
	
	
	
	
	

if __name__ == "__main__":
	main()
