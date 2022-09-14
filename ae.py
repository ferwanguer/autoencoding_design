import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import sys


class Sampling(layers.Layer):
    """Uses (z_mean, z_log_var) to sample z, the vector encoding a digit."""

    def call(self, inputs):
        z_mean, z_log_var = inputs
        batch = tf.shape(z_mean)[0]
        dim = tf.shape(z_mean)[1]
        epsilon = tf.keras.backend.random_normal(shape=(batch, dim))
        return z_mean + tf.exp(0.5 * z_log_var) * epsilon


class VAE(keras.Model):
    def __init__(self, real_dim=50, latent_dim=2):
        super(VAE, self).__init__()
        self.real_dim = real_dim
        self.latent_dim = latent_dim
        self.total_loss_tracker = keras.metrics.Mean(name="total_loss")
        self.reconstruction_loss_tracker = keras.metrics.Mean(
            name="reconstruction_loss"
        )
        self.kl_loss_tracker = keras.metrics.Mean(name="kl_loss")
        self.optimizer = tf.keras.optimizers.Adam()
        self.encoder_constructor()
        self.decoder_constructor()

    def encoder_constructor(self):

        encoder_inputs = keras.Input(shape=(self.real_dim))
        x = layers.Dense(50, activation="sigmoid")(encoder_inputs)
        x = layers.Dense(20, activation="sigmoid")(x)
        z_mean = layers.Dense(self.latent_dim, name="z_mean")(x)
        z_log_var = layers.Dense(self.latent_dim, name="z_log_var")(x)
        sampler = Sampling()
        z = sampler.call(inputs=[z_mean, z_log_var])
        self.encoder = keras.Model(encoder_inputs, [z_mean, z_log_var, z], name="encoder")

    def decoder_constructor(self):
        latent_inputs = keras.Input(shape=(self.latent_dim,))
        x = layers.Dense(20, activation="sigmoid")(latent_inputs)
        x = layers.Dense(50, activation="sigmoid")(x)
        decoder_outputs = layers.Dense(self.real_dim, activation="linear")(x)
        self.decoder = keras.Model(latent_inputs, decoder_outputs, name="decoder")

    def loss(self, data):
        z_mean, z_log_var, z = self.encoder(data)
        reconstruction = self.decoder(z)
        # print(reconstruction)
        mse = tf.keras.losses.MeanSquaredError()
        reconstruction_loss = mse(data, reconstruction)

        kl_loss = -0.5 * (1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var))
        # print(kl_loss)
        kl_loss = tf.reduce_mean(tf.reduce_sum(kl_loss, axis=1))
        beta = 0.005
        total_loss = reconstruction_loss + beta * kl_loss

        return total_loss

    def grad(self, data):
        with tf.GradientTape() as tape:
            loss_value = self.loss(data)
            grads = tape.gradient(loss_value, self.trainable_weights)
        return loss_value, grads

    def optimization_step(self, data):
        loss_value, grads = self.grad(data)

        self.optimizer.apply_gradients(zip(grads, self.trainable_weights))
        return loss_value

    def train(self, training_data, N_iterations=1000, batch_size=8):
        for i in range(N_iterations):
            idx = np.random.choice(training_data.shape[0], batch_size, replace=False)
            train_batch = training_data[idx, :]
            loss_value = self.optimization_step(train_batch)
            if i % 100 == 0:
                print(f'The loss value for {i} iterations is {loss_value.numpy()}')
                # sys.stdout.write('\r%s %s%s %s' % ("N_it = ", i, '     Loss = ', loss_value.numpy()))
                # sys.stdout.flush()


class ForwardMapper:

    def __init__(self, latent_dim=2):
        self.layers = [latent_dim, 5, 5, 5, latent_dim]
        tf.keras.backend.set_floatx('float64')
        self.model = tf.keras.Sequential()
        self.model.optimizer = tf.keras.optimizers.Adam()
        self.model.add(tf.keras.layers.InputLayer(input_shape=(self.layers[0],)))

        for width in self.layers[1:-1]:
            self.model.add(tf.keras.layers.Dense(width, activation=tf.nn.tanh, kernel_initializer="glorot_normal"))

        self.model.add(tf.keras.layers.Dense(
            self.layers[-1], activation=None, kernel_initializer="glorot_normal"))

    def loss(self, latent_design, latent_polar):
        prediction = self.model(latent_design)
        # print(reconstruction)
        mse = tf.keras.losses.MeanSquaredError()
        reconstruction_loss = mse(latent_polar, prediction)
        total_loss = reconstruction_loss

        return total_loss

    def grad(self, latent_design, latent_polar):
        with tf.GradientTape() as tape:
            loss_value = self.loss(latent_design, latent_polar)
            grads = tape.gradient(loss_value, self.model.trainable_weights)
        return loss_value, grads

    def optimization_step(self, latent_design, latent_polar):
        loss_value, grads = self.grad(latent_design, latent_polar)

        self.model.optimizer.apply_gradients(zip(grads, self.model.trainable_weights))
        return loss_value

    def train(self, training_data, labels, N_iterations=1000, batch_size=8):
        for i in range(N_iterations):
            idx = np.random.choice(training_data.shape[0], batch_size, replace=False)
            train_batch = training_data[idx, :]
            label_batch = labels[idx,:]
            loss_value = self.optimization_step(train_batch, label_batch)
            if i % 100 == 0:
                print(f'The loss value for {i} iterations (MAPPER) is {loss_value.numpy()}')
                # sys.stdout.write('\r%s %s%s %s' % ("N_it = ", i, '     Loss = ', loss_value.numpy()))
                # sys.stdout.flush()

# test = ForwardMapper()
# training = np.zeros((10,2))
# labels = np.ones((10,2))
# test.train(training,labels)
# a = test.model(np.zeros((1,2)))
# print(a)