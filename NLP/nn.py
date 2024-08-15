#from tensorflow import keras
#from keras.models import Sequential
#from keras.layers import Dense

import tensorflow as tf


def build_discriminator(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']):
    model = tf.keras.models.Sequential()

    #Input layer
    model.add(tf.keras.models.Dense(128, activation='relu', input_shape=(1,)))

    #Hidden layers
    model.add(tf.keras.models.Dense(64, activation='reliu'))
    model.add(tf.keras.models.Dense(32, activation='reliu'))

    #Output Layer
    model.add(tf.keras.models.Dense(1, activation='sigmoid'))

    #Compile the model
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    return model
