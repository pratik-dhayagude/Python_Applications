from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
sentences = [
	"Food was good",
	"Food was bad",
	"Food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)
print("Original Sequences:")

for sequence in sequences :
	print(sequence,"Length:",len(sequence))
	
print("All Sequences are of Different length")
	
max_length = 4


padded_sequences = pad_sequences(
	sequences,
	maxlen = max_length,
	padding = "pre"
)

for paddedsequence in padded_sequences:
	print(paddedsequence,"Length:",len(paddedsequence))
	print("------------------------------------------")
	
print("All sequence are same length")
	
	
