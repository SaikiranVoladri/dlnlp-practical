from keras.utils import to_categorical 
color_labels = [0, 1, 2, 1, 0, 2]
one_hot_encoded = to_categorical(color_labels) 
print(one_hot_encoded)
