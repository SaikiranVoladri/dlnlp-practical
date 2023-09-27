from sklearn.feature_extraction.text import TfidfVectorizer 
corpus = ["Sometimes life can get confusing and hard",
"In such times it can be useful to turn to the wisdom of poetry."]


vectorizer = TfidfVectorizer()


vectorizer.fit(corpus)


mykeys = list(vectorizer.vocabulary_.keys())
mykeys.sort()
sorted_dict = {i : vectorizer.vocabulary_[i] for i in mykeys}
 

print("Vocabulary:" , sorted_dict)
print(vectorizer.idf_)

vector = vectorizer.transform([corpus[0]]) 
print()

print(vector.shape)
print()
print("Encoded corpus is:")
print(vector.toarray())
