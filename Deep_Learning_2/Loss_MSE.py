def Marvellous_MSE(Y_True,Y_pred):
	n = len(Y_True)
	
	Total_Error = 0
	
	for i in range(n):
		Error = Y_True[i] - Y_pred[i]
		Total_Error = Total_Error + (Error**2)
		
	MSE = (Total_Error/n)
	return MSE
		


Y_True = [10,20,30]
Y_pred = [12,18,33]

loss =  Marvellous_MSE(Y_True,Y_pred)
print(loss)
