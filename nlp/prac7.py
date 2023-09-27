# from keras.preprocessing.text import text_to_word_sequence
# text = "If you dont sacrifice for what you want then what yuou want is your sacrifice"
# result = text_to_word_sequence(text) 
# print(result)
# words = set(text_to_word_sequence(text)) 
# vocab_size = len(words)
# print(vocab_size)

# from keras.preprocessing.text import one_hot
# from keras.preprocessing.text import text_to_word_sequence
# text = "If you dont sacrifice for what you want then what yuou want is your sacrifice"
# words = set(text_to_word_sequence(text)) 
# vocab_size = len(words)
# print(vocab_size)
# result = one_hot(text, round(vocab_size*1.3)) 
# print(result)

from keras.preprocessing.text import hashing_trick
from keras.preprocessing.text import text_to_word_sequence
text = "If you don’t sacrifice for what you want then what you want is your sacrifice "
words = set(text_to_word_sequence(text))
vocab_size = len(words)
print(vocab_size)
result = hashing_trick(text, round(vocab_size*1.3), hash_function='md5')
print(result)

