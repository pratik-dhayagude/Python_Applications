sentences = [
	"Food was good",
	"food was bad",
	"Food was not good"
]

labels = [1,0,0]

for sentence ,label in zip(sentences,labels):
	
	
	print("Sentence:",sentence)
	print("Label:",label)

	if(label==1):
		print("Meanign : Positive Sentiment")
	else:
		print("Meaning : Neigative Semtiment")
	print("--------------------------------------")
