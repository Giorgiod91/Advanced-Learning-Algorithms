# Advanced-Learning-Algorithms Part 2 of the Machine Learning course from andrew ng

- layer of neurons

![Screenshot 2025-01-17 111005](https://github.com/user-attachments/assets/46755972-a086-4ef6-a928-8fc01b288fa9)

# forward propagation Algorithm (forward direction)

- compute a[1] a[2] a[3] for example
  ![Screenshot 2025-01-17 111621](https://github.com/user-attachments/assets/988d98bc-d3f0-4839-a3c3-ae3bf4403105)

- final compute of a[3]
- an optional step would be to check if a[3] >= 0.5 to make it binary with the sigmoid function

![Screenshot 2025-01-17 111702](https://github.com/user-attachments/assets/57f26342-459d-4602-a178-95ab059f20f4)

# forward prop implementation in python with numpy

![image](https://github.com/user-attachments/assets/50e12e9b-bc29-4b1c-93be-27ffc9cb8ba4)

# guidance

- load data --> X,y = load_data()
- visualize the dataSet
- print out the data x and y to see whats in there ---> print(X[0]) for example
- print out the shape to check out the demension ---> print(X.shape)

<<<<<<< HEAD
# Train a neural Network

- step 1 specify the model
- step2 compiles the model using a specific loss function
- step 3 is to train the model
=======
# Vector matric multiplication 
![image](https://github.com/user-attachments/assets/3b596046-cb90-4bba-93ca-140784d655a2)

# matrix matrix multiplication

- transpose a matrix then u take the columsn and lay them on the side like here in the picture

![image](https://github.com/user-attachments/assets/2fd62fc8-11fb-466f-a433-91950e9dddde)

- multiplicaiton steps
![image](https://github.com/user-attachments/assets/d64e0234-2be4-4f75-86ff-0121afa3e34c)
# rules 
-you can only take dot products between vectors that are the same length
![image](https://github.com/user-attachments/assets/192a6a04-a419-44af-899f-a725d0af6830)

# matrix multiplication in python with numpy
- AT= A.T  will lay them on the side
![image](https://github.com/user-attachments/assets/53162ee0-ac71-4944-a130-8b77acc91136)


# matrix multiplicaiton in the neural network 
![image](https://github.com/user-attachments/assets/afbed372-08fc-4745-bbdf-7c730dd60a92)



# steps for creating a neural network 
# Step 1    ---- >  Create the Model

![Screenshot 2025-01-25 114710](https://github.com/user-attachments/assets/f71cdd4d-5b6b-41f8-9e2c-78c7aab2ddd0)

# Step 2    ---- >  Loss and Cost function
![image](https://github.com/user-attachments/assets/b8046a04-c6de-4ff4-92ec-26a5cb1d4ce5)


# Step 2    ---- >  Train the Model

![image](https://github.com/user-attachments/assets/c2d323ba-6083-4893-91e1-7ddd6303c790)



# most 3 commonly activation functions 
![image](https://github.com/user-attachments/assets/8d5daa4c-4fe2-4268-a7a4-59044267cf67)



# choosing the right activation functions for the output layer
- binary classification problem then use the sigmoid functiion    0 or 1
- for stock price predictions for example the linear activaiton function is better because it can go from minus to plus can go down or up
- for house price predictions the output can never be negativ so then should choose the ReLU activation function   0 or positiv values

 ![image](https://github.com/user-attachments/assets/bc4be845-62e5-4233-99f7-e79eb7c23359)

# for the hidden layer activatopn functions
- the most common choice is the ReLU function today (faster learning)
- sigmoid if there is a binary classificaiton problem (its less efficent )
- dont use linear activation function



# multi classification
- y can take on more than just two possible values

# Softmax regression
- a's will end up together as 1 so for example a1= 0.30 a2=0.20 a3=0.15 then a4=0.35   a1+a2+a3+a4 = 1
![image](https://github.com/user-attachments/assets/17d0f9d7-b42b-47e0-9380-0510c28b0c78)

# recap on cost function for logistic regression and Softmax regression
![{39DAD3CD-43EA-4BD7-BE04-745DDC590901}](https://github.com/user-attachments/assets/5df095ae-3018-4f7e-8b32-d423d9219ee2)

# Neural Network with Softmax output
- each of the the activation values depends on the values of Z
  ![image](https://github.com/user-attachments/assets/eee41260-e483-4b9e-9939-d4157c89e784)


# the more numerically accurate implementation of softmax with tensorflow

![image](https://github.com/user-attachments/assets/3f9cbded-491e-4038-9a4e-75cb7b56e563)


# multi-label Classification
- target output y is a vector
- could build multiple neural networks

![Screenshot 2025-01-27 191014](https://github.com/user-attachments/assets/ea5f8671-1e80-4c7f-a46b-fb19b5723260)


![image](https://github.com/user-attachments/assets/f4e13734-aecf-471f-a68d-7cc96f75581b)



# Adam algorithm
- faster then gradient descent and it should be the default choice
- increases alpha to get faster to the minimum
- decreases alpha to get faster to the minimum
- if wj or b keeps moving in the same direction increases learning rate alpha j aj
- if wj or b keeps oscillating back and forth reduce the learnign rate alpha j aj
-  The Adam optimization algorithm does need some default initial learning rate alpha
![image](https://github.com/user-attachments/assets/1ecdcce3-ca52-478b-bc7f-aa24785c67a6)

# other layer Type for example Convolutional Layer

![image](https://github.com/user-attachments/assets/1c32bf33-0992-4a54-a32e-90302ca32833)

## Training/cross validation/test set
- 60% training set
- 20% cross validation
- 20% test set
![image](https://github.com/user-attachments/assets/21e9a147-75ab-4aad-ad5b-7bb6b28c8e98)


