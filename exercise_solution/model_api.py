# load the model from disk
import pickle
import pandas as pd
import numpy as np


# load saved model

encoding_values = {'buying price': {'vhigh': 4, 'high': 3, 'med': 2, 'low': 1},
                   'maintenance price': {'vhigh': 4, 'high': 3, 'med': 2, 'low': 1},
                   'number of doors': {'5more': 4, '4': 3, '3': 2, '2': 1},
                   'person capacity': {'more': 3, '4': 2, '2': 1},
                   'luggage boot': {'big': 3, 'med': 2, 'small': 1},
                   'safety': {'high': 3, 'med': 2, 'low': 1}}

acceptability_encoding = {4: 'vgood', 3:'good', 2:'acc', 1:'unacc'}

# function that the endpoint calls
def predict(data):
	# read the car's features
	data = data.split(' ')
	if len(data)!=7:
		raise Exception("Error: missing some feature(s) or the name of the model to use!!")
	
	# get name of the model to load
	filename = data[0]+'_model.sav'
	# load model  
	model = pickle.load(open(filename, 'rb'))
	# get the features of the car
	data = np.array(data[1:])
	to_predict = pd.DataFrame([data],columns=['buying price','maintenance price', 'number of doors', 'person capacity', 'luggage boot', 'safety'])
	# encode ordinal values
	to_predict.replace(encoding_values, inplace=True)
	# predict using the model
	prediction = model.predict(to_predict)
	result =  [acceptability_encoding.get(x) for x in prediction]
	# return result
	return "The car's acceptability class is: {}  ".format(result[0])


