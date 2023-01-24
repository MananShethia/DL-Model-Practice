# -*- coding: utf-8 -*-
"""FCN Multiclass classification Sole.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rSOLSm0Exf6iFrGquwRjwI9HT0DyHCkk
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.models import Sequential
from keras.layers import BatchNormalization # a normalization technique done between the layers of a Neural Network instead of in the raw data. It is done along mini-batches 
                                            # instead of the full data set. It serves to speed up training and use higher learning rates, making learning easier
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from keras.datasets import cifar10
from keras.utils import normalize, to_categorical

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# normalizing data set : it is the organization of data to appear similar across all records and fields

X_train = normalize(X_train, axis=1)
X_test = normalize(X_test, axis=1)

# categorize training dataset : tf your training data uses classes as numbers, to_categorical will transform those numbers in proper vectors for using with models

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# image augmentation

train_datagen = ImageDataGenerator(rotation_range=45, width_shift_range=0.2, zoom_range = 0.2, horizontal_flip = True)
train_datagen.fit(X_train)

train_generator = train_datagen.flow(X_train, y_train, batch_size = 32)

# building model

# kernel_initializer : the main purpose is to initialize the weight matrix in the neural network
# he_uniform : Draws samples from a uniform distribution within [-limit, limit] , where limit = sqrt(6 / fan_in) ( fan_in is the number of input units in the weight tensor)

# padding : "same" results in padding with zeros evenly to the left/right or up/down of the input.
model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(32, 32, 3)))
model.add(BatchNormalization())

model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(BatchNormalization())

model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(BatchNormalization())

model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
model.add(BatchNormalization())
model.add(Dense(10, activation='softmax'))

# compile model

# from keras.optimizers import SGD
# opt = SGD(lr=0.001, momentum=0.9)
# model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.summary()

# train with input data

history = model.fit_generator(train_generator, epochs = 10, validation_data = (X_test, y_test))

# plot the training and validation accuracy and loss at each epoch

loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'y', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()


accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']
plt.plot(epochs, accuracy, 'y', label='Training accuracy')
plt.plot(epochs, val_accuracy, 'r', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()



# making prediction

index = random.randint(0, len(X_test))
plt.imshow(X_test[index, :])
plt.show()

y_pred = model.predict(X_test[index, :].reshape(1, 32, 32, 3))
print('probability of image: ', y_pred)

y_class = np.argmax(y_pred)
print(y_class)

# CLASSES
# 0: airplane
# 1: automobile
# 2: bird
# 3: cat
# 4: deer
# 5: dog
# 6: frog
# 7: horse
# 8: ship
# 9: truck

