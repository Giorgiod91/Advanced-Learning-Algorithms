# Advanced-Learning-Algorithms  Part 2 of the Machine Learning course from andrew ng
- layer of neurons


![Screenshot 2025-01-17 111005](https://github.com/user-attachments/assets/46755972-a086-4ef6-a928-8fc01b288fa9)


# forward propagation Algorithm (forward direction)
- compute a[1] a[2] a[3] for example 
![Screenshot 2025-01-17 111621](https://github.com/user-attachments/assets/988d98bc-d3f0-4839-a3c3-ae3bf4403105)


- final compute of a[3]
- an optional step would be to check if a[3] >= 0.5  to make it binary   with the sigmoid function

![Screenshot 2025-01-17 111702](https://github.com/user-attachments/assets/57f26342-459d-4602-a178-95ab059f20f4)


# forward prop implementation in python with numpy

![image](https://github.com/user-attachments/assets/50e12e9b-bc29-4b1c-93be-27ffc9cb8ba4)



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










