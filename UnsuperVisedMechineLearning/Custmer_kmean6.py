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
	
	# Step4 -> Elbow method
	
	
	WCSS = []
	
	for k in range(1,11):
		model = KMeans(
			n_clusters = k,
			random_state = 42,
			n_init = 10
	
		
		)
		model.fit(X_scaled)
		WCSS.append(model.inertia_)
	print("Values of Wcss:")
	
	for i in range(len(WCSS)):
		print(f"{i+1}:{WCSS[i]}")
		
	# Step5 -> Visulation
	
	plt.plot(range(1,11),WCSS,marker = "o")
	plt.xlabel("Number of cluster:K")
	plt.ylabel("WCSS")
	plt.title("Marvellous Elbow analysis")
	plt.grid()
	plt.show()
	
	
	#Step6 -> Final Model
	
	
	model = KMeans(
			n_clusters = 4,
			random_state = 42,
			n_init = 10
	
		)
	clusters = model.fit_predict(X_scaled)
	df["Cluster"] = clusters
	
	print("Data Set with clusters")
	print(df.head(100))
	
		
		

if __name__ == "__main__":
	main()
