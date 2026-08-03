import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
import seaborn as sns
from sklearn.model_selection import train_test_split

border = "-"*40
###############################################
##
## 	->Load They data set
##
###############################################

print(border)
print("Step1 -> Load They data set ")
print(border)

datapath = "iris.csv"

df = pd.read_csv(datapath)

print("Dataset loaded successfukky -_-")

print("Initial entry from dataset are ->")

print(df.head())


###############################################
##
## 	-> data analysis (EDA)
##
###############################################

print(border)
print("step2 -> data analysis")
print(border)

print("shape of the data set:",df.shape)

print("Coloum names:",list(df.columns))

print("Missing values per coloum :")
print(df.isnull().sum())

print("class distrubution->(species count)")
print(df["species"].value_counts())

print("Statical report of dataset:")
print(df.describe())


###############################################
##
## 	-> decide Independent Variable and dependent varaibles
##
###############################################

print(border)
print("step3-> decide Independent Variable and dependent varaibles")
print(border)
# X -> Independent variable(Features)
## Y -> Dependent Variable(Label) 

Feature_Cols = ["sepal length (cm)",
"sepal width (cm)",
"petal length (cm)",
"petal width (cm)"]

x = df[Feature_Cols]

y = df["species"]

print("X shape",x.shape)
print("Y shape",y.shape)

###############################################
##
## 	-> Visulation of data set
##
###############################################

#print(border)
#print("step4 -> Visulation of data set")
#print(border)


### Scatter Plot
#plt.figure(figsize = (7,5))#

#for sp in df["species"].unique():
	#temp = df[df["species"]==sp]
	#plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)
	
#plt.title("Marvellous Iris case study")

#plt.xlabel("petal length (cm)")
#plt.ylabel("petal weidth (cm)")

#plt.legend()
#plt.grid()
#plt.show()


###############################################
##
## 	-> traning testing
##
###############################################

print(border)
print("step5 ->traning testing")
print(border)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.5,random_state = 42)
print("dataset spliting activity done")

print("X :",x.shape) # (150,4)
print("Y :",y.shape) # (150,)
print("X_train",x_train.shape)
print("X_test",x_test.shape)
print("y_train",y_train.shape)
print("y_train",y_train.shape)

###############################################
##
## 	-> Built they model
##
###############################################

print(border)
print("Step6->Built they model")
print(border)

Model=DecisionTreeClassifier(max_depth = 5)

print("Model gets created sussfully")

###############################################
##
## 	-> Train the model
##
###############################################

print(border)
print("step7 -> Train the model")
print(border)

Model.fit(x_train,y_train)
print("Model traind sussfully")


###############################################
##
## 	-> Test the model
##
###############################################

print(border)
print("step8 ->  Test the model")
print(border)

y_pred = Model.predict(x_test)
print("Model testing done")

print("Expected answers :")
print(y_test)

print("Predicted answer")
print(y_pred)






























