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
	
	
	
	
	
	
	
	


def main():
	MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
	main()
