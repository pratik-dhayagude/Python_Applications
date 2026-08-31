def Marvellous_MAE(Y_True,Y_pred):
	n = len(Y_True)
	
	Total_Error = 0
	
	for i in range(n):
		Error = abs(Y_True[i] - Y_pred[i])
		Total_Error = Total_Error + (Error)
		
	MAE = (Total_Error/n)
	return MAE
		


Y_True = [10,20,30]
Y_pred = [12,18,33]

loss =  Marvellous_MAE(Y_True,Y_pred)
print(loss)
