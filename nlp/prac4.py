from sklearn.feature_extraction.text import HashingVectorizer 
corpus = ["Sometimes life can get confusing and hard",
"In such times it can be useful to turn to the wisdom of poetry."]


vectorizer = HashingVectorizer(n_features = 3**5)


vector = vectorizer.fit_transform(corpus) 
print(vector.shape)
