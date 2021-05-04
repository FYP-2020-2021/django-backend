import os
import pickle
import tensorflow as tf
from tensorflow import keras

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

# Loading the data manager
print("Loading data manager...")
dm_path = os.path.join(dir_path, "model/actual/datamanager.pkl")
with open(dm_path, 'rb') as pickle_file:
	dm = pickle.load(pickle_file)

# Loading the trained model
print("Loading model...")
model_path = os.path.join(dir_path, "model/actual/epoch_03-val_acc_0.87")
model = tf.keras.models.load_model(model_path)

