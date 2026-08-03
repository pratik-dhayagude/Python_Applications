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










