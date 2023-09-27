from sklearn.feature_extraction.text import CountVectorizer

corpus = ["What you do today is that you achieve tommorow",
"If you dont sacrifice for what you want then what you want is your sacrifice"]
vectorizer = CountVectorizer()
vectorizer.fit(corpus)

print("Vocabulary:" , vectorizer.vocabulary_)

vector = vectorizer.transform(corpus)

print("Encoded corpus is:")
print(vector.toarray())
