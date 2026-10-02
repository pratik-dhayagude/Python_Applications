sentences = [
	"Food was good",
	"food was bad",
	"Food was not good"
]

labels = [1,0,0]

for sentence ,label in zip(sentences,labels):
	sentement = "Positive"if label == 1 else "Negative"
	
	print("Sentence:",sentence)
	print("Label:",label)

	print("Meaning:",sentement)	
	print("---------------------------")
