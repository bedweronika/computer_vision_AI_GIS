from funct.WideAndDeepModel import model
import tensorflow as tf


# save the model (or save_weights())
model.save("./tests/keras_model.keras")

# load model (or load_weigths())
model = tf.keras.models.load_model("./tests/keras_model.keras")