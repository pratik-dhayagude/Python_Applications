from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
	"Food was good",
	"Food was bad",
	"Food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentences)

word_index=tokenizer.word_index

for word , index in word_index.items():
	print("Position ",index,":",word)
	
	
