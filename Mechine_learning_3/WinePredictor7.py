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
	# step6 -> HyperParameter Tunning
	###
	
	
	print(Border)
	print("step6 -> HyperParameter Tunning")
	print(Border)
	
	accuracy_score =[]
	
	K_Values = range(1,21)
	 
	for K in K_Values:
		model = KNeighborsClassifier(n_neighbors = K)
		model = model.fit(X_train_scaled ,Y_train)
		Y_pred = model.predict(X_test_scaled)
		accuracy = accuracy_score(Y_test,Y_pred)
		accuracy_score.append(accuracy)
		
		
	print("Accuracy report")
	
	for No in accuracy_score:
		print(No)
		
	print(Border)
	
	
	print(Border)
	print("Graphical Representation")
	print(Border)
	
	
	plt.figure(figsize = (8,5))
	plt.plot(K_Values,accuracy_score,marker = "o")
	plt.title("K Values Vs Accuracy")
	plt.xlabel("Value of K")
	plt.ylabel("Accuracy")
	plt.grid(True)
	plt.xticks(list(K_Values))
	plt.show()
	
	
		
	
	
	
def main():
	 MarvellousClassifire("WinePredictor.csv")
if __name__ == "__main__":
	main()
