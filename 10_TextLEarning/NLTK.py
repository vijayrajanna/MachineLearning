import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

listofstopwords = stopwords.words("english")

print len(listofstopwords)
print listofstopwords
