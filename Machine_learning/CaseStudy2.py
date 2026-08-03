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











