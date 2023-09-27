import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer 
tokenizer = Tokenizer(num_words=1000)
texts = ["This is a text.", "This is another text."]
tokenizer.fit_on_texts(texts)
tokens = tokenizer.texts_to_sequences(texts)
print(tokens)
