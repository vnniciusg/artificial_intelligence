# Handwritten Digit Recognition
## Overview
This project aims to develop a system for recognizing handwritten digits, specifically numbers from 0 to 9. The system will take an input of binary representations of handwritten digits and output the corresponding digit.

## Dataset
The system uses a dataset of binary representations of handwritten digits. Each digit is represented as a 5x5 grid, where '1' represents a written part and '0' represents a blank space. Each line in the dataset represents a digit, with the last digit in the line indicating the actual number the binary pattern represents.

## Model Architecture
The model is a feed-forward neural network and consists of the following layers:

1. An input layer that flattens the input data, converting the 2D array of pixel values for each image into a 1D array. This is necessary because the subsequent dense layer expects a 1D array as input.

2. A dense layer (fully connected layer) with 45 neurons and a ReLU (Rectified Linear Unit) activation function. This layer is designed to learn features from the input data.

3. An output layer, which is another dense layer with as many neurons as there are classes in the target data (the digits 0-9). This layer uses the softmax activation function to output a probability distribution over the classes. This means the output of this layer is 10 probabilities that sum to 1, each representing the model's confidence that the input image represents each possible digit.

The model is trained on the binary digit dataset to learn the patterns and features of the digits.

## Dataset Example
Here is an example of how the digits are represented in the dataset:

00100,01100,10100,00100,00100,00100,00100,00100,00100,1000000000
01110,10001,00001,00001,00010,00100,01000,10000,11111,0100000000
01110,10001,00001,00001,00010,00001,00001,10001,01110,0010000000
00010,00110,00110,01010,01010,10010,11111,00010,00010,0001000000
11111,10000,10000,11110,10001,00001,00001,10001,01110,0000100000
01110,10001,10000,10000,11110,10001,10001,10001,01110,0000010000
11111,00001,00010,00010,00100,00100,01000,01000,01000,0000001000
01110,10001,10001,10001,01110,10001,10001,10001,01110,0000000100
01110,10001,10001,10001,01111,00001,00001,10001,01110,0000000010
01110,10001,10001,10001,10001,10001,10001,10001,01110,0000000001

In the above example, each line represents a digit from 0 to 9. The last 10 digits of each line indicate the actual number the binary pattern represents, with '1' in the position corresponding to the number. For example, the first line represents the digit '0', as indicated by the '1' in the first position of the last 10 digits