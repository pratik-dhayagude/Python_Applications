import numpy as np 

from tensorflow.keras.preprocessing.text import Tokenizer 

from tensorflow.keras.preprocessing.sequence import pad_sequences 

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Embedding ,SimpleRNN,Dense



#Step 1
train_sentances = [

	"food was good",
	"food was bad",
	"food was excellent",
	"food was terrible",
	"service was good",
	"service was bad",
	"service was excellent",
	"service was terrible",
	"ambience was good",
	"ambience  was bad",
	"ambience  was excellent",
	"ambience  was terrible"
	

]

# step 2
train_label = [
	1,
	0,
	1,
	0,
	1,
	0,
	1,
	0,
	1,
	0,
	1,
	0
]

# Step2 : tocknizetion

tokenizer = Tokenizer(oov_token = "<oov>")

tokenizer.fit_on_text(train_sentances)
# Step 3 : Convert Traning data into sequence 

train_sequence = tokenizer.texts_to_sequences(train_sentances)


print("Traning sequences")
for sentance,sequance in zip(train_sentances,train_sequence ):
	print(sentance ,"->",sequance)






  
