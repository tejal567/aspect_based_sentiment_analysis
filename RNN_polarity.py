from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import SimpleRNN,LSTM
from keras.layers.core import Dense, Dropout
from keras.layers.wrappers import TimeDistributed
from keras.layers import Convolution1D
from keras.utils import np_utils
import pickle
import numpy as np

from prepareData import *

y = []
for i in range(len(train_label)):
    if train_label[i] == -1:
        y.append(2)
    else:
        y.append(int(train_label[i]))
y = np_utils.to_categorical(y)

MAX_SEQUENCE_LENGTH = maxi
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_x)
sequences = tokenizer.texts_to_sequences(train_x)

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

data = []

for vec in sequences:
    data.append(vec[:-1]+[0 for i in range(MAX_SEQUENCE_LENGTH-len(vec))]+[vec[-1]])

data = np.asarray(data)

# data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', y.shape)

# split the data into a training set and a validation set
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
y = y[indices]
nb_validation_samples = int(0.2 * data.shape[0])

x_train = data[:-nb_validation_samples]
y_train = y[:-nb_validation_samples]
x_val = data[-nb_validation_samples:]
y_val = y[-nb_validation_samples:]



embeddings_index = {}
f = open('glove.6B.200d.txt','r')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))


embedding_matrix = np.zeros((len(word_index) + 1, 200))
for word, i in word_index.items():
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        embedding_matrix[i] = embedding_vector


from keras.layers import Embedding,Input,Activation,Dense,Conv1D,MaxPooling1D,Flatten,Dropout,LSTM
from keras.models import Model
embedding_layer = Embedding(len(word_index) + 1,
                            200,
                            weights=[embedding_matrix],
                            input_length=MAX_SEQUENCE_LENGTH,
                            trainable=False)


sequence_input = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
embedded_sequences = embedding_layer(sequence_input)
# x = Conv1D(128, 5, activation='relu')(embedded_sequences)
# # x = Dropout(0.1)(x)
# x = MaxPooling1D(4)(x)
# x = Conv1D(128, 3, activation='relu')(x)
# # x = Dropout(0.1)(x)
# x = MaxPooling1D(5)(x)  # global max pooling
# x = Flatten()(x)
print embedded_sequences.shape
# x = LSTM(100, dropout=0.02, recurrent_dropout=0.02)(embedded_sequences)
x = LSTM(100)(embedded_sequences)
x = Dense(128, activation='relu')(x)
x = Dropout(0.02)(x)
preds = Dense(3, activation='softmax')(x)
# x = Dropout(0.02)(x)

model = Model(sequence_input, preds)
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['acc'])


model.fit(x_train, y_train, validation_data=(x_val, y_val),epochs=10, batch_size=10)