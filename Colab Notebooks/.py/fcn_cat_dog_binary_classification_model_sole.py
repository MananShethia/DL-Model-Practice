# -*- coding: utf-8 -*-
"""FCN Cat-Dog Binary Classification Model Sole.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10KW1rezCMkPYTiy-d4W0zf-9VdVLNAOI
"""

from google.colab import drive
drive.mount('/content/drive')

# import the libraries

import numpy as np # Used for working with array
import random
import matplotlib.pyplot as plt # to display out image
from keras.models import Sequential # importing sequential model
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten # importing convolutional layers as Conv2D, MaxPooling2D, fully connected network as Dense, 2D to 1D by Flatten

# path for files

xtrain = '/content/drive/MyDrive/Dataset/cats_and_dogs_images/input.csv'
ytrain = '/content/drive/MyDrive/Dataset/cats_and_dogs_images/labels.csv'
xtest = '/content/drive/MyDrive/Dataset/cats_and_dogs_images/input_test.csv'
ytest = '/content/drive/MyDrive/Dataset/cats_and_dogs_images/labels_test.csv'

# load dataset

X_train = np.loadtxt(xtrain, delimiter = ',')
y_train = np.loadtxt(ytrain, delimiter = ',')
X_test = np.loadtxt(xtest, delimiter = ',')
y_test = np.loadtxt(ytest, delimiter = ',')

# resizing dataset

X_train = X_train.reshape(len(X_train), 100, 100, 3)
y_train = y_train.reshape(len(y_train), 1)
X_test = X_test.reshape(len(X_test), 100, 100, 3)
y_test = y_test.reshape(len(y_test), 1)

# as values are in range from 0 to 255
# but to train our model appropriately we need to rescale these values between 0 to 1

X_train = X_train/255.0
X_test = X_test/255.0

X_train[1, :]

# shape of dataset after resizing

print("Shape of X_train: ", X_train.shape)
print("Shape of y_train: ", y_train.shape)
print("Shape of X_test: ", X_test.shape)
print("Shape of y_test: ", y_test.shape)

# displaying random image

index = random.randint(0, len(X_train))
plt.imshow(X_train[index, :])
plt.show()

# model

# Sequential model means that the layers are going to be stacked up in the sequence
# first convolutional layer, than maxpooling layer, than another convolutional layer, than maxpooling layer, than we couple of fully connected layers and thats how out convoltional neural network made
model = Sequential([
    Conv2D(32, (3, 3), # first parameter of convolutional layer are the number of filters we want to use and second parameter is the size of the filter
           activation = 'relu',
    
           # for the first layer always in keras we need to mention the input shape which means what kind of shape is this model expecting
           input_shape = (100, 100, 3) # our model expecting 100x100x3 size image
          ),# this is how we add our first layer
    
    #adding next layer which is maxpooling layer
    MaxPooling2D((2, 2)), # one parameter which is filter size
    
    # second convolutioanl layer
    Conv2D(32, (3, 3), activation = 'relu'),
    MaxPooling2D((2,2)),
    
    
    Flatten(),
    # now making fully connected layer using Dense()
    Dense(64, activation = 'relu'), # first parameter is number of neurons we want to keep in first fully connected layer and second parameter is the activation function we are using
    
    # final fully connected layer which is our output layer
    # output layer must have the same number of neurons as our output class but for binary classification we only need one output neuron
    Dense(1, activation = 'sigmoid') # activation function is SIGMOID because it is a bianry classification
])

# we can also make model by add individual layer separately as it is Sequential

model = Sequential()

model.add(Conv2D(32, (3, 3), activation = 'relu', input_shape = (100, 100, 3)))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(32, (3, 3), activation = 'relu'))
model.add(MaxPooling2D((2,2)))

model.add(Flatten())
model.add(Dense(64, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model = Sequential([
    Conv2D(32, (3, 3), activation = 'relu', input_shape = (100, 100, 3)),
    MaxPooling2D((2,2)),
    
    Conv2D(32, (3, 3), activation = 'relu'),
    MaxPooling2D((2,2)),
    
    Flatten(),
    Dense(64, activation = 'relu'),
    Dense(1, activation = 'sigmoid')
])

# now compile the model by adding the loss and the back propagation model
# parameters are loss, optimizer and metrics
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
# 'binary_crossentropy' because we are implimenting binary classification
# metrics indicate a metric on which we want to evaluate our model

# train with our input data

history = model.fit(X_train, y_train, epochs = 10, batch_size = 64)
# epochs = number of epochs for which we want to train our model

loss_train = history.history['loss']
accuracy_train = history.history['accuracy']
# loss_val = history.history['val_loss']
epochs = range(1,11)
plt.plot(epochs, loss_train, 'r', label='Training loss')
plt.plot(epochs, accuracy_train, 'g', label='Training Accuracy')
# plt.plot(epochs, loss_val, 'b', label='validation loss')
plt.title('Training Accuracy & loss')
plt.xlabel('Epochs')
plt.ylabel('Loss & Accuracy')
plt.legend()
plt.show()

# evaluate the model on the test data set

model.evaluate(X_test, y_test)

# making prediction

index2 = random.randint(0, len(X_test))
plt.imshow(X_test[index2, :])
plt.show()

y_pred = model.predict(X_test[index2, :].reshape(1, 100, 100, 3))
print('probability of image: ', y_pred)

y_pred = y_pred > 0.5
print('boolean probability of image: ', y_pred)
if(y_pred == 0):
    pred = 'dog'
else:
    pred = 'cat'

print('According to model it is: ', pred)

