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
	
	
	
	
	
	
	
	






