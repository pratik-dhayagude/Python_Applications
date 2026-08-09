import numpy as np 
from sklearn.neighbors import KNeighborsClassifier



def main():
	# Independent
	X = np.array([
		[1,2],
		[2,3],
		[3,1],
		[5,6]
	])
	
	# Dependent
	Y = np.array([
		"Red",
		"Red",
		"Blue",
		"Blue"
	])
	
	# Model Creation
	
	new_point = np.array([[3,3]])
	
	model = KNeighborsClassifier(n_neighbors = 3)
	model = model.fit(X,Y)
	
	y_pred = model.predict(new_point)
	
	print("predict label:",y_pred)
	
	

	

	

if __name__ == "__main__":
	main()
