import numpy as np 

import math


#=============================
#  Step 1 -> Input Layer
#=============================
border = "="*40
print(border)
X1 = 2.0
X2 = 3.0

print("Step 1 -> Input Layer")
print("Input Feature(X):Feature")
print(f"X1 = {X1}")
print(f"X2 = {X2}")


#=============================
#  Step 2 -> Hidden Layer
#=============================


print(border)
print(" Step 2 -> Hidden Layer")
print("Hidden Neuron 1")
print(border)
W11 = 0.5
W12 = -0.2

B1 = 0.1

print(border)
print("Weight:")
print(f"W11:{W11}")
print(f"W12:{W12}")

print(border)
print("Bias:")
print(f"b1:{B1}")
print(border)

print("Weighted Sum:")
print("z1 = (x1*w11+x2*w12)+b1")

z1 = (X1*W11)+(X2*W12)+B1
print("Weigthed Sum:(Z1)",z1)

h1 = max(0,z1)

print("O/P of hidden nueron1 (h1)",h1)
print(border)

#-------------------------------------
print("For H2")
print(border)
print(" Step 2 -> Hidden Layer")
print("Hidden Neuron 2")
print(border)
W21 = 0.8
W22 = 0.4

B2 = -0.1

print(border)
print("Weight:")
print(f"W21:{W21}")
print(f"W22:{W22}")

print(border)
print("Bias:")
print(f"b2:{B2}")
print(border)

print("Weighted Sum:")
print("z2 = (x1*w21+x2*w22)+b2")

z2 = (X1*W21)+(X2*W22)+B2
print("Weigthed Sum:(Z1)",z2)

h2 = max(0,z2)

print("O/P of hidden nueron1 (h2)",h2)
print(border)

#---------------------------------------

print(border)
print("Step 3 -> Output Layer")
print(border)


Wx = 1.0
Wy = -1.5
b_out = 0.2


print(border)
print("Weight:")
print(f"W_out1:{Wx}")
print(f"W_out2:{Wy}")
print(border)

print(border)
print("Bias:")
print(f"b_out :{b_out}")
print(border)

print("Weighted Sum:")
print("z = (h1*w_out1+h2*w_out2)+b_out")

z = (h1*Wx)+(h2*Wy)+b_out
print("Weighted Sum:",z)

h = 1 /(1+math.exp(-z))

print(border)
print("== Neural Network_Summary ==")
print(border)

print("Input layer")
print(f"X1:{X1}")
print(f"X2:{X2}")

print("Hidden Layer:")
print(f"h1:{h1}")
print(f"h2:{h2}")

print("O/P layer:")
print(f"z:{h}")

print("Prediction of Neural Network")
if(h>=0.5):
	print("Predicted as positive Class")
	
else:
	print("Negative Class")
print(border)













