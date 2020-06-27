import csv
import numpy as np
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer
from keras.models import Model
from keras.models import load_model
from keras.optimizers import SGD,Adam
from keras.layers import Reshape, Convolution2D, Activation, MaxPooling2D, Flatten, Dropout, Dense 

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

def add_new_layer_1(base_model):
	x = base_model.output
	x = Dense(12, activation='relu',name='N_dense_1')(x)
	x = Dense(12, activation='relu',name='N_dense_2')(x)
	x = Dense(9, activation='relu',name='N_dense_3')(x)
	predictions = Dense(1, name='N_dense_out')(x)
	return predictions

def add_new_layer_2(base_model):
	x = base_model.output
	x = Dense(12, activation='relu',name='N_dense_1')(x)
	x = Dense(15, activation='relu',name='N_dense_2')(x)
	x = Dense(15, activation='relu',name='N_dense_3')(x)
	x = Dense(12, activation='relu',name='N_dense_4')(x)
	x = Dense(9, activation='relu',name='N_dense_5')(x)
	predictions = Dense(1, name='N_dense_out')(x)
	return predictions

def add_new_layer_3(base_model):
	x = base_model.output
	x = Dense(12, activation='relu',name='N_dense_1')(x)
	x = Dense(15, activation='relu',name='N_dense_2')(x)
	x = Dense(18, activation='relu',name='N_dense_3')(x)
	x = Dense(18, activation='relu',name='N_dense_4')(x)
	x = Dense(15, activation='relu',name='N_dense_5')(x)
	x = Dense(12, activation='relu',name='N_dense_6')(x)
	x = Dense(9, activation='relu',name='N_dense_7')(x)
	predictions = Dense(1, name='N_dense_out')(x)
	return predictions

# create the base pre-trained model
base_model = load_model('./model/three_scale_sh_h3.h5').get_layer(index=0)

# add new layer for TL
new_model = add_new_layer_2(base_model)

# the latest model
model = Model(inputs=base_model.input, outputs=new_model)

for layer in model.layers:
   print(layer.name)

for layer in model.layers[:1]:
   layer.trainable = False
for layer in model.layers[1:]:
   layer.trainable = True

#all (4841, )
#sh (3241, )
#sz (1600, )
#eval (530, )

train_x, train_y = load_train_data_and_labels()
train_x = train_x.reshape( (4841,3,9) )

model.compile(optimizer=SGD(lr=0.0001), loss='mse', metrics=['mse'])
model.fit(train_x, train_y, batch_size=4, epochs=30, validation_split=0.1)

model.save("three_scale_tl_h2_l.h5")