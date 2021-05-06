"""
This file is customized as a tester for:
1) Read in different file types
2) Convert (or extract) texts 
3) Pass to run model

Note: codes here are not involved in any Django adminstration tasks.
"""

import os
import sys
import textract
import numpy as np
import tensorflow as tf
from tensorflow import keras

sys.path.insert(0, "..")
from data_manager import DataManager


def run_model(arr_of_texts):
	# Perform prediction
	print("Getting prediction results..")
	print("Number of input texts:", len(arr_of_texts))

	dm_path = "actual/tokenizer.pkl"
	arr_of_texts = dm.predict_preprocess(arr_of_texts, dm_path)

	print("Shape of input tensor:", arr_of_texts.shape)
	result = model.predict(arr_of_texts)

	# Get maximum result
	amax = np.argmax(result, 1)
	predicted_classes = dm.labels[amax]

	final_result = []
	for i in range(len(arr_of_texts)):
		percentages = [round(r * 100, 2) for r in result[i]]
		pred_class = predicted_classes[i]
		final_result.append((pred_class, percentages))

	return final_result


"""
SETUP CONFIGURATION AREA
"""

# Supress tensorflow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Getting the path of the files
par_path = os.path.abspath("..")
dm_path = par_path + "/tmp"
model_path = par_path + "/model/actual/epoch_03-val_acc_0.87"

# Loading the data manager
print(">> Loading data manager...")
dm = DataManager(dm_path, encoding="latin")
dm.labels = np.asarray(["Elementary School", "Middle School", "High School", "Undergraduate"])

# Loading the trained model
print(">> Loading model...")
model = tf.keras.models.load_model(model_path)


"""
DO NOT CHANGE THE CODE IN THE SETUP CONFIGURATION AREA ABOVE,
ONLY CHANGE BELOW FOR TESTING PURPOSES
"""

"""
RUNNING SAMPLE TESTS BELOW
"""

# Running file tests for different document types
files_tests = ["sample_files/fyp_doc.docx", "sample_files/middle_1.docx", "sample_files/middle_2.docx", 
								"sample_files/middle_1.txt", "sample_files/middle_2.txt", "sample_files/university.txt", 
								"sample_files/fyp_lecture_slides.pdf", "sample_files/research_1.pdf", "sample_files/research_2.pdf", 
								"sample_files/research_3.pdf", "sample_files/research_4.pdf", "sample_files/research_5.pdf"]

for file in files_tests:
	print(f">> Processing {file}")
	try:
		text = textract.process(file)
		text = text.decode('utf-8')
		res = run_model([text])
		print(f">> Result: {res}")
	except:
		print(f">> Result not found")
	
	print("==============================")





