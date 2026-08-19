import pandas as pd

import joblib 

def LoadModel(FileName):
	model = joblib.load(FileName)
	print("Model Loaded Successfully")
	print(model.features_name_in_)
	
	
	
	  
def main():
	LoadModel()

if __name__ == "__main__":
	main()
