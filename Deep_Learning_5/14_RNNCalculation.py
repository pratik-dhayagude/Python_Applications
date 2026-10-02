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
	b =  0.1
	
	
	for time_step,x in enumerate(inputs):
		previous_hidden_state = hidden_state
		weighted_input = Wx * x
		weighted_memory = Wh + previous_hidden_state 
		total = weighted_input + weighted_memory + b
		
		hidden_state = np.tanh(total)
		
		print("TimeStamp : ",time_step+1)
		print("Input:",x)
		print("Hiden state:",hidden_state)
		print("-"*30)
		
	print("Final Hidden State :",hidden_state)
	
def main():

	MarvellousRNNPrediction()
if __name__ == "__main__":
	main()
