sentance = "food was not good"
# Time Step: 1    2   3   4
# Token :    1    2   5   3


words = sentance.split()


print("Actual sentance:",sentance)


for index , word in enumerate(words):
	print("TimeStep:",index+1,":",word)
	


