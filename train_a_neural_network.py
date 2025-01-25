import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import BinaryCrossentropy
# simple train of a neural network with TensorFlow

#step 1  specify the model


model = Sequential([
    #layers 
    Dense(units=25, activation="sigmoid"),
    Dense(units=15, activation="sigmoid"),
    #output layer
    Dense(units=1, activation="sigmoid"),

])
# step2 compiles the model using a specific loss function 


model.compile(loss=BinaryCrossentropy())

# step 3 is to train the model


model.fit(X,Y, epochs=100)  # epochs is for the number of steps


