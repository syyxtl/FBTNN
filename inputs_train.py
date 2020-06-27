import os
import csv
import cv2
import numpy as np
import mmodel
import keras.backend as K
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer
from keras.preprocessing import image
from keras.models import load_model
from keras.optimizers import SGD

def load_train_data_and_labels():
	csv500 = csv.reader(open("./data/all_500.csv"))
	csv1000 = csv.reader(open("./data/all_1000.csv"))
	csv1500 = csv.reader(open("./data/all_1500.csv"))
	
	features500 = np.array([list(map(float, row[0:len(row)-1])) for row in csv500])
	features1000 = np.array([list(map(float, row[0:len(row)-1])) for row in csv1000])
	features1500 = np.array([list(map(float, row[0:len(row)-1])) for row in csv1500])
	feature = np.concatenate((features500, features1000, features1500), axis=1)

	csv500 = csv.reader(open("./data/all_500.csv"))
	csv1000 = csv.reader(open("./data/all_1000.csv"))
	csv1500 = csv.reader(open("./data/all_1500.csv"))
	res500 = np.array([list(map(float, row[len(row)-1:])) for row in csv500])
	# res500 = np.array(LabelBinarizer().fit_transform(res500) )
	res1000 = np.array([list(map(float, row[len(row)-1:])) for row in csv1000])
	# res1000 = np.array(LabelBinarizer().fit_transform(res1000) )
	res1500 = np.array([list(map(float, row[len(row)-1:])) for row in csv1500])
	# res1500 = np.array(LabelBinarizer().fit_transform(res1500) )
	res = np.concatenate((res500, res1000, res1500), axis=1) 
	return feature, res500

#all (4841, )
#sh (3241, )
#sz (1600, )
#eval (530, )

## train
train_x, train_y = load_train_data_and_labels()
train_x = train_x.reshape( (4841,3,9) )
# train_y = train_y.reshape( (3601,3,1) )

model = mmodel.Hidden_2().back_model()
model.compile(optimizer=SGD(lr=0.0001), loss='mse', metrics=['mse'])  # regression
# model.compile(optimizer=SGD(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])  # classification
model.fit(train_x, train_y, batch_size=8, epochs=30, validation_split=0.1)
model.save("three_scale_all_h2.h5")