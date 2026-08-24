import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error,r2_score


#Step1 -> Load the data

df = pd.read_csv("california_housing.csv")

print("Shape")
print(df.shape)
print("Some entry from the csv:")
print(df.head())


#Step2 -> Split the X and y 

X = df.drop("target",axis = 1)
Y = df["target"]


print("X Shape:",X.shape)
print("Y shape:",Y.shape)



#Step3 -> split the traning and testing


X_train,X_test,Y_train,Y_test =  train_test_split(X,Y,test_size = 0.2,random_state = 42)

print("Spliting successfully")




# Step4 -> creat the boosting model
model = GradientBoostingRegressor(
	
	n_estimators = 100,
	learning_rate = 0.1,
	max_depth = 3,
	random_state = 42

)


# Step5 -> train the model


model = model.fit(X_train,Y_train)


print("Train model successfully")

#Step 6 -> test the model'

y_pred = model.predict(X_test)

print("Testing the model sucessfully")


# Step7 -> Evalute the model


print("MSE : ",mean_squared_error(Y_test,y_pred))

print("R2 :",r2_score(Y_test,y_pred))

