import re 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import ngrams
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard. very poorly"

REGEX_TEXT = re.sub('[^a-zA-Z0-9 \n]', '', EXAMPLE_TEXT)
PS = PorterStemmer()

# print(sent_tokenize(REGEX_TEXT))
A=word_tokenize(REGEX_TEXT)
SW=set(stopwords.words("english"))
# print(A)

""" TG= ngrams(EXAMPLE_TEXT.split(),2)

for grams in TG:
  print(grams[0]+' '+grams[1]) """

for I in A:
    print(PS.stem(I))

