import matplotlib.pyplot as plt

def main():

	Langauge = ["C","C++","Java","Pyrhon"]
	
	Students = [30,40,35,55]
	
	plt.bar(
		Langauge,
		Students,
		width = 0.2,
		edgecolor = "black",
		linewidth = 2,
		alpha = 0.8,
		label = "Students"
	
	)	
	plt.title("Marvellous Bar")
	plt.xlabel("Languages")
	plt.ylabel("student")
	
	plt.grid(True)
	plt.legend()
	plt.show()
	
	

if __name__ == "__main__":
	main()
