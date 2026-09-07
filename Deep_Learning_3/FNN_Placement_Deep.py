##################################################################
#   -> Deep Learning PipeLine
#	1 :	Read the data from csv  
#	2 :	Data Analysis
#	3 :	Preprocessing
#	4 :	Train_TEst_Split
#	5 :	Feature Scaling
#	6 :	FNN Model Traning
#	7 :	Model Evalituion 	
#	8 :	model preserv
#	9 :	model loding and preserving
#	10 : 	Graphical Representation
# 	11 :	Test Unseen Data
##################################################################
border = "="*50

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

#	1 :	Read the data from csv

print(border)
print("1 :Read the data from csv") 
print(border)

data = pd.read_csv("placement_data.csv")

print("Complect Dataset")
print(data)
print(border)


#	2 :	Data Analysis

print("2 :Data Analysis")
print(border)

print("First Five Rows:")
print(data.head())

print("Colums Names:")
print(data.columns)

print("Shape of DataSet:")
print(data.shape)

print("Statical Summary :")
print(data.describe())

print(border)

print(border)
print("3 :Preprocessing")
print(border)

X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y = data["Placed"]

print("Input Feature:")
print(X.head())

print("Target")
print(Y.head())

print(border)
print("Shape of X:")
print(X.shape)
print("Shape of Y:")
print(Y.shape)
print(border)

print(border)
print("4 :Train_Test_Split")
print(border)


X_train,X_test,Y_train,Y_test = train_test_split(
			X,Y,test_size = 0.30,random_state = 42
	
)

print(border)
print("Shape of X_train:")
print(X_train.shape)
print("Shape of X_test:")
print(X_test.shape)
print("Shape of Y_train:")
print(Y_train.shape)
print("Shape of Y_test:")
print(Y_test.shape)
print(border)

#	5 :	Feature Scaling

print(border)
print("5 :Feature Scaling")
print(border)

Scaler = StandardScaler()


X_train_scaled = Scaler.fit_transform(X_train)
X_test_scaled =  Scaler.fit_transform(X_test) 


print("Scaled Traing Data:",X_train_scaled[:5])

#	6 :	FNN Model Traning
print(border)
print("6 :FNN Model Traning")
print(border)


model = MLPClassifier(
	
	hidden_layer_sizes = (8,4),
	activation = "relu",
	solver = "adam",
	max_iter = 1000,
	random_state = 42
)

print(model)
print(border)
print("Train the model")
model = model.fit(X_train_scaled,Y_train)
print("Model Traning complected")
print(border)

#	7 :	Model Evalituion 	
print("7 :	Model Evalituion ")
print(border)
print("Test the model")
y_pred = model.predict(X_test_scaled)
print("Testing model successfully")

accuracy = accuracy_score(Y_test,y_pred)
print("Accuracy:",accuracy)

cm = confusion_matrix(Y_test,y_pred)
print("Confusion Matrix:",cm)
print("Predict the probability:")
Y_prob = model.predict_proba(X_test_scaled)
print(Y_prob[:5])
print(border)
print("Thanku")

# 8 :	model preserv

print(border)
print("8 :model preserv")
print(border)

joblib.dump(model,"placemect_FNN_model.pkl")
joblib.dump(Scaler,"Placement_Scaler.pkl")

print("Model and Scaler Gets dump successfully")

# 10:model loding and preserving

print("Model Loading And prevising")
loaded_model = joblib.load("placemect_FNN_model.pkl")
loaded_scaler = joblib.load("Placement_Scaler.pkl")

print("Model Gest loaded successfully")

# 11 : 	Test Unseen Data
print(border)
print("11 :Test Unseen Data")
print(border)

new_Student = pd.DataFrame([[70,75,80,85,1]],columns = ['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaler = loaded_scaler.transform(new_Student)

new_pred = loaded_model.predict(new_student_scaler)
new_prob =  loaded_model.predict_proba(new_student_scaler)
print("New Student Data:",new_Student)
print("Prediction Probability:",new_prob)
if new_pred[0] == 1:
	print("Prediction place")
else:
	print("Prediction Unplace")








