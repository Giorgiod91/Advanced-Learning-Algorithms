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






>>>>>>> 8eb24c3b0d65f11de29f600ab0f6955c0eb6881f
