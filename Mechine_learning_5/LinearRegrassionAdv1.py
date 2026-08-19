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
	## Step2 -> Analysis the data
	###
	
	
	


def main():
	MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
	main()
