from keras.models import Sequential
from keras.layers import Reshape, Convolution2D, Activation, MaxPooling2D, Flatten, Dropout, Dense, GlobalAveragePooling2D
from keras.layers import LeakyReLU

class Hidden_0(object):
	def __init__(self):
		self.model = Sequential()
		self.model.add(Flatten(input_shape=(3, 9 )))
		self.model.add(Dense(1))
		self.model.summary()

	def back_model(self):
		return self.model

class Hidden_1(object):
	def __init__(self):
		self.model = Sequential()
		self.model.add(Flatten(input_shape=(3, 9 )))
		self.model.add(Dense(12, activation='relu'))
		self.model.add(Dense(12, activation='relu'))
		self.model.add(Dense( 9, activation='relu'))
		self.model.add(Dense(1))
		self.model.summary()

	def back_model(self):
		return self.model

class Hidden_2(object):
	def __init__(self):
		self.model = Sequential()
		self.model.add(Flatten(input_shape=(3, 9 )))
		self.model.add(Dense(12, activation='relu'))
		self.model.add(Dense(15, activation='relu'))
		self.model.add(Dense(15, activation='relu'))
		self.model.add(Dense(12, activation='relu'))
		self.model.add(Dense( 9, activation='relu'))
		self.model.add(Dense(1))
		self.model.summary()

	def back_model(self):
		return self.model

class Hidden_3(object):
	def __init__(self):
		self.model = Sequential()
		self.model.add(Flatten(input_shape=(3, 9 )))
		self.model.add(Dense(12, activation='relu'))
		self.model.add(Dense(15, activation='relu'))
		self.model.add(Dense(18, activation='relu'))
		self.model.add(Dense(18, activation='relu'))
		self.model.add(Dense(15, activation='relu'))
		self.model.add(Dense(12, activation='relu'))
		self.model.add(Dense( 9, activation='relu'))
		self.model.add(Dense(1))
		self.model.summary()

	def back_model(self):
		return self.model