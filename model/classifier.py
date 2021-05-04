import os
import argparse
import re
import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from model.data_manager import DataManager



def run_model(arr_of_texts):
	"""
	No probability is returned here
	Only the predicted classes for each of the text given in the array
	"""
	# Getting the path information of current directory
	path = os.path.abspath(__file__)
	dir_path = os.path.dirname(path) 

	# Loading the data manager
	print("Loading data manager...")
	dm_path = os.path.join(dir_path, "actual/datamanager.pkl")
	with open(dm_path, 'rb') as pickle_file:
		dm = pickle.load(pickle_file)

	# Loading the trained model
	print("Loading model...")
	model_path = os.path.join(dir_path, "actual/epoch_03-val_acc_0.87")
	model = tf.keras.models.load_model(model_path)

	# Perform prediction
	print("Getting prediction results..")
	arr_of_texts = dm.predict_preprocess(arr_of_texts)
	result = model.predict(arr_of_texts)

	# Get maximum result
	amax = np.argmax(result, 1)

	temp  = dm.labels[amax]
	predicted_classes = [pred_class[2:] for pred_class in temp]
	
	return predicted_classes

