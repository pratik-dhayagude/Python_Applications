from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
	"Food was good",
	"Food was bad",
	"Food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

for sentance , sequence in zip(sentences,sequences):
	print("Sentence :",sentance)
	print("Sequence:",sequence)
	print("---------------------")
