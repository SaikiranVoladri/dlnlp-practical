
#TOKENIZATION
# # text = "This is Deep learning Practical 1 " 
# tokens = text.split()
# print(tokens)

# STEMMING
# import nltk
# from nltk.stem import PorterStemmer
# ps = PorterStemmer()
# sentence = "This is Deep learning Practical 1"
# for word in sentence.split():
#   print(ps.stem(word))

#LEMMATIZATION
# import nltk 
# nltk.download('wordnet')
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer() 
# print(lemmatizer.lemmatize("reading", pos= "v"))
# print(lemmatizer.lemmatize("teaching", pos= "v"))

#REMOVAL OF STOP WORDS
import nltk
from nltk.corpus import stopwords 
nltk.download('stopwords') 
print(stopwords.words('english'))

