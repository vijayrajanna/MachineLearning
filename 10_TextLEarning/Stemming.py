from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")
print(stemmer.stem("respose"))
print(stemmer.stem("responsiveness"))
print (stemmer.stem("responsibility"))
print (stemmer.stem("respondent"))
print (stemmer.stem("responcsively"))
