from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer


A = "ease of use , the fact that your company keeps current with the latest television hardware"
B="it works great but sometimes does not turn on everything at once"
C="I love the way you can customize the remote to a multitude of devices. Only issue is it is like a computer, not always what I apply will work."

print(sent_tokenize(A), end="\n")
print(sent_tokenize(B), end="\n")
print(sent_tokenize(C), end="\n")