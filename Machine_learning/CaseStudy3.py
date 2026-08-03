import pandas as pd

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
## 	-> 
##
###############################################

















