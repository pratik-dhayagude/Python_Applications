sentences = [
	"Food was good",
	"Food was bad",
	"Food was not good"
]

vocabulary = []

for sentance in sentences:
	words = sentance.split()
	for word in words:
		if word not in vocabulary:
			vocabulary.append(word)
			
for index , x in enumerate(vocabulary):
	# index +1 like 1,2,3,4
	print("Position ",index+1,":",x)


