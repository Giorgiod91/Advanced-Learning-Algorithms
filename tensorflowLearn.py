import tensorflow as tf
from tensorflow.python.keras.layers import Input, Dense
import numpy as np





x= np.array([[200.0, 17.0]])
#dense is a other name for layers 
layer_1 = Dense(units=3, activation="sigmoid")
a1 = layer_1(x)

layer_2 = Dense(units=1, activation="sigmoid")
a2 = layer_2(a1)