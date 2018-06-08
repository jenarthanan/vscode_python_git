import re
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
LMTZ = WordNetLemmatizer()

# NLTK's default English stopwords
DSTOPWORDS = stopwords.words()

# print(DSTOPWORDS)

# convert to list to String
DSTOPWORDS = " ".join(str(W) for W in DSTOPWORDS)

# Adding Custom Stopwords
stopwords_file = r'D:\Programing\python\vscode_python_git\NLP\stopwords.txt'
CSTOPWORDS = open(stopwords_file, 'r',encoding="utf8").read()

# Concatenate both stopwords
STOPWORDS = DSTOPWORDS + CSTOPWORDS

# Getting the Verbatim file 
VERBATIMFILE = r'D:\Programing\python\vscode_python_git\NLP\VerbatimJune1to5.txt'
FP = open(VERBATIMFILE, 'rt',encoding="utf8")

# Remove Special characters
REGEX_TEXT = re.sub('[^''a-zA-Z0-9 \n]', '', FP.read().lower())

WORDS = word_tokenize(REGEX_TEXT)

# Remove numbers
WORDS = [WORD for WORD in WORDS if not WORD.isnumeric()]

""" # Lowercase all words (default_stopwords are lowercase too)
WORDS = [WORD.lower() for WORD in WORDS] """

# Remove stopwords
WORDS = [WORD for WORD in WORDS if WORD not in STOPWORDS]

# Need to look  for Str to List Conversion



# Lemmatizer 
LEMWORDS = [LMTZ.lemmatize(WORD) for  WORD in WORDS ]


# print(LEMWORDS)

# Calculate frequency distribution
FREQ = FreqDist(LEMWORDS)

# Print(type(FREQ))


# FREQ1 = FreqDist(WORDS)

# Output top 50 words
for word, frequency in FREQ.most_common(200):
    print(u'{};{}'.format(word, frequency))

""" # Output top 50 words
for word, frequency in FREQ1.most_common(50):
    print(u'{};{}'.format(word, frequency)) """
