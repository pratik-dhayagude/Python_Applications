from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
	Data = load_iris()
	
	X = Data.data
	
	Y = Data.target
	
	X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)
	
	model = DecisionTreeClassifier()
	
	model = model.fit(X_train,Y_train)
	
	Y_pred = model.predict(X_test)
	
	Result = accuracy_score(Y_test,Y_pred)
		
	print(Result*100)
		
if __name__ == "__main__":
	main()
