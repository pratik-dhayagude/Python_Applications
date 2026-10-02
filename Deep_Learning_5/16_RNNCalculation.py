# ht = tanh(wx*xt + wh * ht-1 +b)

# Xt = Current Input
# Wx = Weight of current input
# Wh = weight of previous hidden state
# B =  bias
# ht-1 = previous hidden state 
# tanh = activation function 
# ht =  new hidden satte 
import numpy as np 



def Sigmoid(x):
	return 1 / (1+np.exe(-x))
	
def MarvellousRNNPrediction():
	print("Calculation of RNN")
	# food was not good
	inputs =[1,2,5,3]
	
	hidden_state = 0
	
	# RNN parameters 
	Wx = 0.5
	Wh = 0.8
	bias =  0.1
	
	
	# RNN Calculation
	for time_step,x in enumerate(inputs):
		previous_hidden_state = hidden_state
		weighted_input = Wx * x
		weighted_memory = Wh + previous_hidden_state 
		total = weighted_input + weighted_memory + bias
		
		hidden_state = np.tanh(total)
		
		print("TimeStamp : ",time_step+1)
		print("Input:",x)
		print("Hiden state:",hidden_state)
		print("-"*30)
		
	# Step No 2 : Finel hiden state 
	print("Final Hidden State :",hidden_state)
	
	#Step 3 -> Output Layer 
	
	# O/P = wy * finalHiddenstate + output bias
	
	
	Wy = 1.0
	output_bias = 0
	
	
	output = (Wy * hidden_state) + output_bias
	
	
	print("Row output :",output)
	
	
	
	# STep 4 : Apply the sigmoid 
	
	probability = Sigmoid(output)
	
	print("Probability is :",probability )
	
	
	
	
	
	
	
	
	
def main():

	MarvellousRNNPrediction()
if __name__ == "__main__":
	main()
