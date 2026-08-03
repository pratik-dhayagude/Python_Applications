from sklearn.datasets import load_iris

def main():
	print("-"*30)
	print("iris classification case stdy:")
	print("-"*30)
	
	dataset = load_iris()
	print(dataset)
	

if __name__ == "__main__":
	main()
