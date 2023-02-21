# import keras
# from keras.datasets import mnist
# from keras.models import Sequential
# from keras.layers import Dense, Dropout
# from keras.optimizers import RMSprop
# import pickle

# # Save the history object separately
# with open('path/to/history.pkl', 'wb') as file:
#     pickle.dump(history.history, file)


import matplotlib.pyplot as plt
import pickle
import keras

# Load the model from its .h5 file
model = keras.models.load_model('D:/_M@N@N_/University/sem-8/Test/demo1.h5')

# Load the history from a separate file
with open('D:/_M@N@N_/University/sem-8/Test/history1.pkl', 'rb') as file:
    history = pickle.load(file)

# Plot the loss
plt.plot(history['loss'])
plt.plot(history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'], loc='upper right')
plt.show()

# Plot the accuracy
plt.plot(history['acc'])
plt.plot(history['val_acc'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'], loc='lower right')
plt.show()
