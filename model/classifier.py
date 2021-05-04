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

from config import dm, model

def run_model(arr_of_texts):
	"""
	No probability is returned here
	Only the predicted classes for each of the text given in the array
	"""
	# Getting the path information of current directory
	path = os.path.abspath(__file__)
	dir_path = os.path.dirname(path)
	tf.get_logger().setLevel('INFO')

	# Perform prediction
	print("Getting prediction results..")
	arr_of_texts = dm.predict_preprocess(arr_of_texts)
	result = model.predict(arr_of_texts)

	# Get maximum result
	amax = np.argmax(result, 1)
	predicted_classes = dm.labels[amax]

	final_result = []
	for i in range(len(arr_of_texts)):
		percentages = [round(r * 100, 2) for r in result[i]]
		pred_class = predicted_classes[i][2:]
		final_result.append((pred_class, percentages))

	return final_result


if __name__ == '__main__':
	sample_file = open("middle1.txt", "r")
	text = sample_file.read()
	arr = [text]
	res = run_model(arr)
	print(f'Results = {res}')