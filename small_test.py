import tensorflow as tf
import numpy as np
y_true = np.random.randint(0, 2, size=(2, 3))
y_pred = np.random.random(size=(2, 3))
print(y_true.shape,y_pred.shape)
loss = tf.keras.losses.mean_squared_error(y_true, y_pred)
print(loss)