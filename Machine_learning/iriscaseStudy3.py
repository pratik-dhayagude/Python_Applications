from sklearn.datasets import load_iris

def main():
	print("-"*30)
	print("iris classification case stdy:")
	print("-"*30)
	
	dataset = load_iris()
	
	#MetaData of they data set
	print("Independent varables are :")
	print(dataset.feature_names)
	print("length of independent variable:",len(dataset.feature_names))
	
	print("Dependent variable are:")
	print(dataset.target_names)
	print("length of dependent varables are :",len(dataset.target_names))
	

if __name__ == "__main__":
	main()
