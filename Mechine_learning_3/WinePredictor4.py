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
	
	X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 42,stratify = Y)
	
	print(Border)
	print("Detaisls of traning and testing data")
	print("Shape of X_train:",X_train.shape)
	print("Shape of X_test:",X_test.shape)
	print("Shape of Y_train:",Y_train.shape)
	print("Shape of Y_test:",X_test.shape)
	
	
	print(Border)
	
	
	
	
	
	
	
	
	
	
	
		
	

def main():
	 MarvellousClassifire("WinePredictor.csv")
if __name__ == "__main__":
	main()
