import matplotlib.pyplot as plt

def main():

	x = [1,2,3,4,5]

	y = [10,25,18,35,30]
	
	plt.plot(
		x, 
		y,
		marker = "X",
		linestyle = "--",
		linewidth = 2,
		markersize = 9,
		label = "Marks" 
	)
	plt.title("Marvellous Line Plot")
	plt.xlabel("Student Number")
	plt.ylabel("Marks")
	
	plt.grid(True)
	plt.legend()
	plt.show()
	

if __name__ == "__main__":
	main()
