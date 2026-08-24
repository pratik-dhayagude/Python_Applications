import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

#Step1 -> Load the data Set 


df = pd.read_csv("breast_cancer.csv")

print("Shape of data set")
print(df.shape)

print("First 5 record")
print(df.head())

#Step2 -> Seperate Feature and label


print("The Independent variable will be:")
X = df.drop("target",axis = 1)

print("The Dependent variable are:")
Y = df["target"]


print("X shape:",X.shape)
print("Y shape:",Y.shape)

# Step3 -> train_test_spllit

X_train,X_test,Y_train,Y_test = train_test_split(
						X,
						Y,
						test_size = 0.2,
						random_state = 42)
						
						
print("Spliting Successfully done")

# Step4 -> Scale the feature


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)


# Step 5.1-> Create the Individule models 
model_log = LogisticRegression(max_iter = 1000)
model_D = DecisionTreeClassifier(random_state = 42)
model_KNN = KNeighborsClassifier(n_neighbors = 5)


#step5.2 -> Creating the model 


model = VotingClassifier(
	estimators = [("logistic",model_log),
		"decision_tree",model_D,
		"knn",model_KNN 
	],
	voting = "hard"


)



#Step 6 -> train the model

model = model.fit(X_train,Y_train)

print("Model train successfully")

# Step 7 -> test the model

y_pred = model.predict(X_test)


print("Testing succesfully")

#Step 8 -> Evalute the model 


print("Accuracy :",accuracy_score(Y_test,y_pred))
print("Confuision matrix:",confusion_matrix(Y_test,y_pred))

 



