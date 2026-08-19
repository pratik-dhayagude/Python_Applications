from sklearn.linear_model import LinearRegression
import numpy as np

def main():
	X = np.array([[1],[2],[3],[4],[5]])
	Y = np.array([50,55,60,65,70])
	
	model = LinearRegression()
	
	model = model.fit(X,Y)
	
	print(model.predict([[6]]))

	

if __name__ == "__main__":
	main()
