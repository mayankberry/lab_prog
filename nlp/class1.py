# Task 1 - Import Nltk and test it 

import nltk
from nltk.tokenize import word_tokenize

a = "hello i am mayank"

token = word_tokenize(a)

print(token)



# Task 2 - Convert the tokens into Bigram Trigram

from nltk.util import bigrams, trigrams

a_bigrams = list(bigrams(token))

print("Bigrams = ",a_bigrams)

a_trigrams = list(trigrams(token))

print("Trigrams = ",a_trigrams)
