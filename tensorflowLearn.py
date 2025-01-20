import tensorflow as tf

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense





x= np.array([[200.0, 17.0],[120.0, 5.0],[425.0, 20.0], [212.0 ,18.0]])
y= np.array([1,0,0,1])
#dense is a other name for layers 
#layer_1 = Dense(units=3, activation="sigmoid")
#a1 = layer_1(x)
#layer_2 = Dense(units=1, activation="sigmoid")
#a2 = layer_2(a1)
g = sigmoid
# forward prop
def dense(a_in,W,b):
    units = W.shape[1]
    a_out = np.zeros(units)
    #going through 3 times
    for j in range(units):
        #pull out the j column
        w = W[:,j]
        #compute z
        z = np.dot(w,a_in) + b[j]
        # compute 
        a_out[j] = g(z)
    return a_out
# this add a 2 layer neural network
def my_sequential(x, W1, b1, W2, b2):
    a1 = my_dense(x,  W1, b1)
    a2 = my_dense(a1, W2, b2)
    return(a2)

# this function is similar to the tensoflows model.predict() it will take a matrix X with all m examples 
def my_predict(X, W1, b1, W2, b2):
    m = X.shape[0]
    p = np.zeros((m,1))
    for i in range(m):
        p[i,0] = my_sequential(X[i], W1, b1, W2, b2)
    return(p)

#more usual definition 

model = Sequential([
    Dense(units=3, activation="sigmoid", name="layer1"), 
    Dense(units=1, activation="sigmoid", name="layer2")
])

#string them together(2 layers) to build the neural network


model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.01), loss = tf.keras.losses.BinaryCrossentropy())

model.fit(x,y,epochs=10,)

predictions = model.predict(x)
print(predictions)

# provides a description of the network
model.summary()
W1, b1 = model.get_layer("layer1").get_weights()
W2, b2 = model.get_layer("layer2").get_weights()
print(f"W1{W1.shape}:\n", W1, f"\nb1{b1.shape}:", b1)
print(f"W2{W2.shape}:\n", W2, f"\nb2{b2.shape}:", b2)



