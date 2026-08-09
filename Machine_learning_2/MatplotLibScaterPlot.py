import matplotlib.pyplot as plt

def main():

	studyHours = [1,2,3,4,5,6]
	Marks = [35,42,50,62,72,85]
	
	plt.scatter(
				
		studyHours,
		Marks,
		s = 100,
		marker = "X",
		alpha = 0.8,
		edgecolours = "black",
		linewidths = 1,
		label = "Students"		
	)
	plt.title("Marvellous Scatter Plot")
	plt.xlabel("StudyHours")
	plt.ylabel("Marks")
	
	plt.grid(True)
	plt.legend()
	plt.show()
	

if __name__ == "__main__":
	main()
