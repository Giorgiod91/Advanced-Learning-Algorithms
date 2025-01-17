import tensorflow as tf

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense





x= np.array([[200.0, 17.0],[120.0, 5.0],[425.0, 20.0], [212.0 ,18.0]])
y= np.array([1,0,0,1])
#dense is a other name for layers 
layer_1 = Dense(units=3, activation="sigmoid")
a1 = layer_1(x)

layer_2 = Dense(units=1, activation="sigmoid")
a2 = layer_2(a1)

#string them together(2 layers) to build the neural network
model = Sequential([layer_1, layer_2])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x,y)

predictions = model.predict(x)
print(predictions)
