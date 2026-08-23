import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt

def main():
	#Step1 -> Load the data
	
	df = pd.read_csv("Mall_Customers.csv")
	
	print("Some Values from the dataset ")
	print(df.head())
	
	print("Missing Values")
	print(df.isnull().sum())
	
	
	# Step2 -> Feature Selection
	
	X = df[["AnnualIncome","SpendingScore"]]
	
	print("Selected Fetures:")
	print(X.head())
	
	# Step3 -> Scale the Data
	
	scaler = StandardScaler()
	
	X_scaled = scaler.fit_transform(X)
	
	print("Scaled Data")
	print(X_scaled[:5])
	
	
	
	
	

if __name__ == "__main__":
	main()
