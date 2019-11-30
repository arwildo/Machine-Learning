#!/bin/python3
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# load data
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# load model
model = tf.keras.models.load_model('number_guesser.model')

# make prediction
subject = 9
prediction = model.predict([x_test])
print('prediction :', np.argmax(prediction[subject]))

# plot prediction
plt.imshow(x_test[subject], cmap=plt.cm.binary)
plt.title('Actual')
plt.show()