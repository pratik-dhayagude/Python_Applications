from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Embedding ,LSTM,Dense 

from tensorflow.keras.preprocessing.sequence import pad_sequences




# step2 : Configuration of values 


VOCAB_SIZE= 10000 # Consider Most frequent 10000 unique words

MAX_LENGTH = 200  # Consider maximum 200 words in review 


#Step 3 : Load the IMDB Data set 
print("-"*30)
print("Movi Review Sentiment analysis Using LSTM")
print("-"*30)

print("Loading The data set")

(X_train,Y_train),(X_test,Y_test) = imdb.load_data(num_words =VOCAB_SIZE)

print("="*40)

print("IMDB DataSet loaded successfully")


print("Number of traning review:",len(X_train))
print("Number of testing review:",len(X_test))

#################################################
#	X_train : review used for traning
#	Y_train : Actual sentiment of traning 
#	X_test  : Review use for testing 
# 	Y_test 	: Actual review for testing 

#	Sentiments :
# 	1 -> Positive Sentiment
#	0 -> Negative Sentiment 
#################################################


#Step 4: Laod the word dictionary 

word_index = imdb.get_word_index()

# Dictionary contains maping of word and its corresponding Number
# Drishum is Good Movie => (20 56 78 43)
# EX : 20 -> Drishum | 56 -> is | 78 -> Good | 43 -> movie

#Step 5 : Create Reverse Dictonary 

reverse_word_index = {}

# First 3 will be reserved so shifted with 3 
for word,index in word_index.items():
	reverse_word_index[index+3] = word
	
	
	
#Step 6 : Function tho decode the review 



def DecodeReview(encoded_review):
	words = []
	
	for num in encoded_review:
		if(num>=3): # Ignore first 3
			word = reverse_word_index.get(num,"?")
			words.append(word)
			
	return " ".join(words) # Joine the list of words 
	
	
# Step 7 : Display the Samples Review 

print("-"*40)
print("-------Sample Reviews------------")
print("-"*40)

for i in range(3,7):
	review = DecodeReview(X_train[i])
	
	
	print("Review Number:",i+1)
	print("review :")
	print(review)
	
	if(Y_train[i] == 1):
		print("Sentiment : Positive")
		
	else:print("Sentement : Negative")
	
	
# Step 8 : Padding 

X_train_padded = pad_sequences(
	X_train,
	maxlen = MAX_LENGTH	
)

X_test_padded = pad_sequences(
	X_test,
	maxlen= MAX_LENGTH

)
print("Traning Data Shape:",X_train_padded.shape)
print("Testing Data Shape:",X_test_padded.shape)


# Step 9 : Create LSTM Model 
model = Sequential()


model.add(
	Embedding(
		
		input_dim = VOCAB_SIZE,
		output_dim = 32 # Ecah word is repreasented in 32 Values 
		
	)


)
model.add(
	LSTM(
	
		units = 64 		# Size of LSTM Hiden state 
		
	
	)

)

model.add(
	Dense(
		units = 1,	#One Output
		activation = "sigmoid"	#Used to produce probability
	
	)

)

# Arcitecture 
# Review -> Embedding -> LSTM -> Dense -> Sigmoid -> Positive / Negative

#Step 10 : Compile The model 
model.compile(

	optimizer = "adam",	# Algorithum to updates weight 
	loss = "binary_crossentropy",	# Loss Function
	metrics = ["accuracy"]

)


print("Model Compiled successfully")

# step 11 -> Train the model 

print("Model Traning")

model.fit(

	X_train_padded,	# Input Traning Review 	
	Y_train,	# Actual Sentimental Label 
	epochs = 3,	# Complect data Ste get processed 3 time 
	batch_size = 64, # Process 64 review in one batch 
	validation_split = 0.2	# Use 20% traning for validation

)
print("Model traning gets complected")
# Step 12 : Evalute the model 

accuracy = model.evaluate(
	X_test_padded,	# Testing Review 
	Y_test,		# Actual Testing Label 
	verbose = 0	# Don't Display The Progress bar

)

print("Testing Accuracy :",accuracy)

# Step 13 : Predict the Review 

TEST_REVIEW_NUMBER = 0
original_review = X_test[TEST_REVIEW_NUMBER]

decoded_review = DecodeReview(original_review)


print("Riview Given by the model:")

print(decoded_review)


# Step 14 : Get The actual sentiment 

actual_value = Y_test[TEST_REVIEW_NUMBER]


if(actual_value == 1):
	actual_sentiment = "Positive"
else:
	actual_sentiment = "Negative"
	
print("Actual Centiment :",actual_sentiment)

# Step 15 : Predict the sentiment 


review_for_prediction = X_test_padded[TEST_REVIEW_NUMBER:TEST_REVIEW_NUMBER+1]


pred = model.predict(
	review_for_prediction,
	verbose = 0
)

probability = pred[0][0]


if(probability >= 0.5):
	predicted_sentiment = "POSITIVE"
else:	
	
	predicted_sentiment = "NEGATIVE"
	
	
print("-"*40)
print("Final Result:")
print("Prediction Probability :",probability)
print("Actual Sentiment :",actual_sentiment)
print("Predicted Sentiment:",predicted_sentiment)















	
			
	
	
	
	
	
	
	
	






