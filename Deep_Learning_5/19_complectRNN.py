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

tokenizer.fit_on_texts(train_sentances)
# Step 3 : Convert Traning data into sequence 

train_sequence = tokenizer.texts_to_sequences(train_sentances)


print("Traning sequences")
for sentance,sequance in zip(train_sentances,train_sequence ):
	print(sentance ,"->",sequance)
	
	
max_length = 4


x_train = pad_sequences (

	train_sequence,
	maxlen = max_length,
	padding = "pre"


)

y_train = np.array(train_label)


print("Padded Traning data:")
print(x_train)

print("Traning data:")
print(y_train)


# Step 5 : Calculate Voc size


voc_size = len(tokenizer.word_index)+1


print("Vocabuly size:",voc_size)


#Step 6 : Build RNN model

model = Sequential()

model.add(
	Embedding(
		input_dim = voc_size,
		output_dim = 8,
		input_length = max_length
	)

)
model.add(

	SimpleRNN(
		units = 8,
		activation = "tanh"
	
	
	)
	

)

model.add(
	Dense(
	units =1,
	activation = "sigmoid"
	
	)

)


model.compile(
	optimizer = "adam",
	loss = "binary_crossentropy",
	metrics = ["accuracy"]


)


#Step 8 : Display model 


model.build(
	input_shape=(None,max_length)
	

)

model.summary()


# Train the model


history = model.fit(x_train,y_train,epochs = 100,verbose = 1)

print("model traning complected")

# Create the unseen data 



test_sentance = [
	"service was amazing",
	"service was horrible",
	"experiance was excellent",
	"experiance was terrible"

]


# Convert text to sequence



test_sequences = tokenizer.texts_to_sequences(test_sentance)


x_test = pad_sequences(

	test_sequences,
	maxlen = max_length,
	padding = "pre"

)

# Step 12 : Predict the sentiments 


for text , sequences ,padded in zip(test_sentance ,test_sequences, x_test):
	input_data = np.array([padded])
	
	prediction = model.predict(input_data,verbose=0)
	
	probability = float(prediction[0][0])
	
	print("Sentance:",text)
	print("Sequence:",sequences)
	print("Padded sequences:",padded)
	print("Prediction:",probability)
	
	
	
	if probability >= 0.5:print("Positive")
	else:print("Negative")







  
