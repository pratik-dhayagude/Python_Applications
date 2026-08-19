import numpy as np 

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

import pandas as pd
import matplotlib.pyplot as plt

def MarvellousRegression(DataPath):

	Border = "-"*40
	###
	## Step1 -> load the data
	###
	
	print(Border)
	print("Step1 -> load the data")
	print(Border)
	
	df = pd.read_csv(DataPath)
	
	print(df.head())
	
	###
	## Step2 -> Remove unwanted Coloum
	###
	
	print(Border)
	print("Step2 -> Remove unwanted Coloum")
	print(Border)
	
	if "Unnamed: 0" in df.columns:
		df = df.drop(columns = "Unnamed: 0")
		
	print(df.head())
	
	
	###
	## Step3 -> Cheak Missing Value
	###
	
	print(Border)
	print("Step3 -> Cheak Missing Value")
	print(Border)
	
	print("Total missing values:")
	print(df.isnull().sum())
	print(Border)
	
	###
	## Step4 -> Statical Summary
	###
	print(Border)
	print("tep4 -> Statical Summary")
	print(Border)


	print(df.describe())	
	
	
	###
	## Step5 -> Correletion
	###
	print(Border)
	print("Step5 -> Correletion")
	print(Border)

	print(df.corr())
	
	
	
	###
	## Step6 -> Seperate Independent and Dependent
	###
	print(Border)
	print("Step6 -> Seperate Independent and Dependent")
	print(Border)
	
	X = df[["TV","radio","newspaper"]]
	Y = df["sales"]
	
	
	print("Insependent variables:")
	print(X.head())
	
	print("Dependent variable:")
	print(Y.head())
	
	###
	## Step6 -> Split Independent and Dependent
	###
	
	print(Border)
	print("Step7 -> Split Independent and Dependent")
	print(Border)
	
	X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 42)
	
	print("Traning data",X_train.shape)
	print("Testing data:",X_test.shape)
	
	###
	## Step8 -> Create And train
	###
	
	print(Border)
	print("Step8 -> Create And train")
	print(Border)
	
	model = LinearRegression()
	
	
	model = model.fit(X_train,Y_train)
	
	print("Model train successfully -_-")
	
	print(Border)
	
	
	###
	## Step8 -> Test the model
	###
	
	print(Border)
	print("SStep8 -> Test the model")
	print(Border)
	
	
	y_pred= model.predict(X_test)
	
	print("Model testing successfull")
	print(Border)
	
	
	print("Expected answer")
	print(Y_test[:3])
	
	print("predicted Answer")
	print(y_pred[:3])
	
	
	###
	## Step10 -> Evalute the model
	###	
	
	print(Border)
	print("Step10 -> Evalute the model")
	print(Border)
	
	mse = mean_squared_error(Y_test,y_pred)
	
	RMSE = np.sqrt(mse)
	
	R2 = r2_score(Y_test,y_pred)
	
	print("MSE",mse)
	print("RMSE",RMSE)
	print("R2",R2)
	
	
	###
	## Step11 -> Display Coff
	###	
	
	print(Border)
	print("Step11 -> Display Coff")
	print(Border)
	
	print("TV Cofficient:",model.coef_[0])
	print("Radio Cofficient:",model.coef_[1])
	print("NewsPaper Cofficient:",model.coef_[2])
	
	print("Y Interceter",model.intercept_)
	
	
	
	
	
	
	
	
	
	
		
	
	
	
	


def main():
	MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
	main()
