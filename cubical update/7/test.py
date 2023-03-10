# -*- coding: utf-8 -*-
"""Test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lsECi6ihXsajgxQTLiK1uHtgM4lafxUj
"""

print("hello world")

a = 5
print(a)

b = input("Enter your number: ")
print(b)

print(type(b))

!pip install -q condacolab

import condacolab
condacolab.install()

!conda --version

!which conda







import numpy as np
from sklearn.metrics import confusion_matrix

# Define the ground truth and predicted output arrays
y_true = np.array([[0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 1], [1, 1, 0, 1]])
y_pred = np.array([[0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]])

print(y_true.shape, y_pred.shape)

# Convert the arrays to 1D arrays before computing the confusion matrix
y_true = y_true.ravel()
y_pred = y_pred.ravel()

print(y_true.shape, y_pred.shape)

# Compute the confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Get the true positive, false positive, false negative, and true negative values
tp = cm[1][1]
fp = cm[0][1]
fn = cm[1][0]
tn = cm[0][0]

# Compute the accuracy
accuracy = (tp + tn) / (tp + tn + fp + fn)

# Compute the recall
recall = tp / (tp + fn)

# Compute the precision
precision = tp / (tp + fp)

# Compute the Intersection over Union (IoU)
iou = tp / (tp + fp + fn)

# Print the results
print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("IOU:", iou)





TP = np.sum((y_pred == 1) & (y_true == 1))
FP = np.sum((y_pred == 1) & (y_true == 0))
FN = np.sum((y_pred == 0) & (y_true == 1))
TN = np.sum((y_pred == 0) & (y_true == 0))

# Calculate accuracy, recall, precision, and IOU
accuracy = (TP + TN) / (TP + TN + FP + FN)
recall = TP / (TP + FN)
precision = TP / (TP + FP)
IOU = TP / (TP + FP + FN)

print("Accuracy: ", accuracy)
print("Recall: ", recall)
print("Precision: ", precision)
print("IOU: ", IOU)



