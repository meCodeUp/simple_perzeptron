# Simple perceptron
This Python code implements a simple perceptron, a basic model of an artificial neuron used for binary classification tasks. The perceptron is trained with a step activation function and can be used to learn logical operations such as the AND operation.
Classes and methods

## 1. perceptron class

The perceptron class contains the main logic for the perceptron model. It includes the following attributes and methods:

### Attributes:

- learning_rate: The learning rate that determines how much the weights are adjusted with each update.
- n_iterations: The number of training runs over the entire data set.
- weights: The weights of the perceptron that are adjusted during training.
- bias: The bias term, which is also adjusted during training.
- 
### Methods:

- __init__(self, learning_rate=0.1, n_iterations=100): Constructor that initializes the learning rate and the number of iterations.
- fit(self, X, y): This method trains the perceptron. It initializes the weights and the bias to zero and then performs the training for the specified number of iterations. In each iteration, the weighted sum of the inputs is calculated, the activation function is applied and the weights and bias are updated according to the prediction errors.
- activation_function(self, x): This method implements the step activation function. It returns 1 if the input value x is greater than or equal to 0, and 0 if it is less.
- predict(self, X): This method uses the trained weights and bias to make predictions for new input values. It calculates the weighted sum for each input and applies the activation function.

## 2. example use

In the main part of the code, an example of the use of the perceptron is given:

- Input data (X): an array of input values representing the possible combinations of two binary inputs (0 and 1). In this case, the AND operation is used.
- Target values (y): An array of target values that represents the expected outputs for the AND operation.
- Perceptron instance: An instance of the perceptron class is created and the model is trained with the input data and target values.
- Predictions: After training, predictions are made for the input values and the results are output.

This code provides a simple implementation of a perceptron suitable for basic binary classification tasks. It can easily be extended or modified to solve more complex problems or to use other activation functions.
