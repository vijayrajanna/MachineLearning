from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
string1 = "Hello this is vijay rajanna"
string2 = "how are you Hello vijay renuka renuka"
string3 = "Hello Hello Hello"

stringlist = [string1,string2,string3]

vectorizer.fit(stringlist)

bagofwords = vectorizer.transform(stringlist)

print (bagofwords)
print (vectorizer.vocabulary_.get("hello"))