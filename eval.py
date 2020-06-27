from keras.models import load_model
import csv, os
import numpy as np

def load_valid_data_and_labels():
	csv500 = csv.reader(open("./data/test_500.csv"))
	csv1000 = csv.reader(open("./data/test_1000.csv"))
	csv1500 = csv.reader(open("./data/test_1500.csv"))
	
	features500 = np.array([list(map(float, row[0:len(row)-1])) for row in csv500])
	features1000 = np.array([list(map(float, row[0:len(row)-1])) for row in csv1000])
	features1500 = np.array([list(map(float, row[0:len(row)-1])) for row in csv1500])
	feature = np.concatenate((features500, features1000, features1500), axis=1)

	csv500 = csv.reader(open("./data/test_500.csv"))
	csv1000 = csv.reader(open("./data/test_1000.csv"))
	csv1500 = csv.reader(open("./data/test_1500.csv"))
	res500 = np.array([list(map(float, row[len(row)-1:])) for row in csv500])
	# res500 = np.array(LabelBinarizer().fit_transform(res500) )
	res1000 = np.array([list(map(float, row[len(row)-1:])) for row in csv1000])
	# res1000 = np.array(LabelBinarizer().fit_transform(res1000) )
	res1500 = np.array([list(map(float, row[len(row)-1:])) for row in csv1500])
	# res1500 = np.array(LabelBinarizer().fit_transform(res1500) )
	res = np.concatenate((res500, res1000, res1500), axis=1) 
	return feature, res500



valid_x, valid_y = load_valid_data_and_labels()
valid_x = valid_x.reshape( (530,3,9) )
# print(valid_y)
model = load_model('./model/three_scale_all_h3.h5')
pred = model.predict(valid_x)
# t_y = [ float(i) for i in list(pred)]
# lens = len(t_y)
# out = open('./res/all_h3.csv','w', newline='', encoding='utf-8')
# for alen in range(lens):
# 	csv_write = csv.writer(out, dialect='excel')
# 	csv_write.writerow([t_y[alen]])

# from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
# r2 = r2_score(valid_y[360:],pred[360:])
# print(r2)

print(pred[360:])