import re 
from nltk.corpus import stopwords

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

REGEX_TEXT = re.sub('[^a-zA-Z0-9 \n]', '', EXAMPLE_TEXT)
SW=set(stopwords.words("english"))
print(REGEX_TEXT)

RESULTWORD  = [word for word in re.split(r"\W+",REGEX_TEXT) if word.lower() not in SW]
RESULT = ' '.join(RESULTWORD)
print(RESULT)