# from keras.preprocessing.text import text_to_word_sequence
# txt = "todays hardwork is tomorrows life"
# result = text_to_word_sequence(txt)
# print(result)

from keras.preprocessing.text import text_to_word_sequence
txt = "todays hardwork is tomorrows life"
words = set(text_to_word_sequence(txt))
vocab_size = len(words) 
print(vocab_size)
