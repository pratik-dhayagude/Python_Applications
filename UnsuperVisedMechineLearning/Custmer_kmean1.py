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
	
	
	

if __name__ == "__main__":
	main()
