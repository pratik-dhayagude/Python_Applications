from sklearn.datasets import load_iris

def main():
	print("-"*30)
	print("iris classification case stdy:")
	print("-"*30)
	
	dataset = load_iris()
	
	for i in range(len(dataset.target)):
		print("ID  %d, Feature %s, Label %s"%(i,dataset.data[i],dataset.target[i]))
	
	
	
	

if __name__ == "__main__":
	main()
