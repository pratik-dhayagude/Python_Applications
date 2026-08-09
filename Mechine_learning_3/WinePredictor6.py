import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifire(DataPath):
	Border = "-"*40
	
	
	###
	# Step1 -> Load the dataset from csv file
	###
	print(Border)
	print("Step1 -> Load the dataset from csv file")
	print(Border)
	
	df = pd.read_csv(DataPath)
	
	
	print(Border)
	print("Some Entry from data set")
	print(df.head())
	print(Border)
	
	###
	# Step2 -> Clean they data set
	###
	print(Border)
	print("Step2 -> Clean they data set")
	print(Border)
	
	df.dropna(inplace = True)
	
	print("Shape of data set:",df.shape)
	print("Total records:",df.shape[0])
	print("Total Coloum :",df.shape[1])

	print(Border)	
	
	###
	# Step3 -> Seperate independent and dependent variables
	###
	
	print(Border)
	print("Step3 -> Seperate independent and dependent variables")
	print(Border)
	
	X = df.drop(columns = "Class")
	Y = df["Class"]
	
	print("Shape of X:",X.shape)
	print("Shape of Y :",Y.shape)
	
	
	print(Border)
	print("Inputs Coloum :",X.columns.tolist())
	
	print("OutPut Columns: Class")
	
	print(Border)
	
	###
	# Step3 -> Split the dataset for traning and testing
	###
	
	print(Border)
	print("Step3 -> Split the dataset for traning and testing")
	print(Border)
	
	X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.5,random_state = 42,stratify = Y)
	
	print(Border)
	print("Detaisls of traning and testing data")
	print("Shape of X_train:",X_train.shape)
	print("Shape of X_test:",X_test.shape)
	print("Shape of Y_train:",Y_train.shape)
	print("Shape of Y_test:",X_test.shape)
	print(Border)
	
	###
	# Step5 -> Feature Scaling
	###
	
	print(Border)
	print("Step5 -> Feature Scaling")
	
	
	
	scalar = StandardScaler()
	
	X_train_scaled = scalar.fit_transform(X_train)
	X_test_scaled = scalar.fit_transform(X_test)
	
	print("Feature Scaling done")
	
	print(Border)
	
	###
	# Step6 -> Build the model
	###
	
	print(Border)
	print("Step6 -> Build the model")
	print(Border)
	
	model = KNeighborsClassifier(n_neighbors = 9)
	
	print("Classification model is created")
	
	### 
	# Step7 -> train the model
	###
	
	print(Border)
	print("Step7 -> train the model")
	print(Border)
	
	model = model.fit(X_train_scaled,Y_train)
	
	print("Model traning complited")
	
	
	### 
	# Step8 -> Testing the model
	###
	
	print(Border)
	print("Step8 -> Testing the model")
	print(Border)
	y_pred = model.predict(X_test_scaled)
	
	accuracy = accuracy_score(Y_test,y_pred)
	
	print("Model accuracy is :",accuracy*100)
def main():
	 MarvellousClassifire("WinePredictor.csv")
if __name__ == "__main__":
	main()
