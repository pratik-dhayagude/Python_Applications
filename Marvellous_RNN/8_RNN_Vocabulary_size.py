from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
	"Food was good",
	"Food was bad",
	"Food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentences)

word_index=tokenizer.word_index

vocab_size = len(word_index)+1

print("Number of unique words:",len(word_index))
print("Padding index:0")

print("Vocab Size :",vocab_size)
