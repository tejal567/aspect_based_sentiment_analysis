from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import pickle
import a
import os.path

obj = pickle.load(open('aspect_dump_new.p'))

if os.path.isfile('SVM_polarity_model.p'):
	classifier = pickle.load(open('SVM_polarity_model.p','r'))

	res = dict()

	def stringval(x):
		if x==1:
			return 'positive'
		if x==-1:
			return 'negative'
		return 'neutral'

	pit = dict()
	for key, value in obj.iteritems():
		temp = dict()
		for aspect in value:
			pred = classifier.predict([a.sentence[key]+" "+aspect])
			temp[aspect] = stringval(pred)
		pit[key] = temp

	print pit
	pickle.dump(pit,open('polarities.p','wb'))
else:
	from keras.models import Sequential
	from keras.layers.embeddings import Embedding
	from keras.layers.recurrent import SimpleRNN,LSTM
	from keras.layers.core import Dense, Dropout
	from keras.layers.wrappers import TimeDistributed
	from keras.layers import Convolution1D
	from keras.utils import np_utils
	import pickle
	import numpy as np


	MAX_SEQUENCE_LENGTH = 70
	from keras.preprocessing.text import Tokenizer
	from keras.preprocessing.sequence import pad_sequences

	test_x = list()

	json_file = open('../model/RNN_polarity.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	obj = model_from_json(loaded_model_json)
	# load weights into new model
	obj.load_weights("./model/model.h5")
	print("Loaded model from disk")


	pit = dict()
	for key, value in obj.iteritems():
		temp = dict()
		for aspect in value:
			pred = model.predict(self,[a.sentence[key]+" "+aspect])
			temp[aspect] = stringval(pred)
		pit[key] = temp

	print pit

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
