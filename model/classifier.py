import os
import numpy as np
from config import dm, model

def run_model(arr_of_texts):
	# Getting the path information of current directory
	path = os.path.abspath(__file__)
	dir_path = os.path.dirname(path)

	print("Getting prediction results..")
	print("Number of input texts:", len(arr_of_texts))

	# Perform prediction
	dm_path = os.path.join(dir_path, "model/actual/tokenizer.pkl")
	print("dm_path =", dm_path)
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

