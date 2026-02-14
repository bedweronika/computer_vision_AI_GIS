from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import tensorflow as tf

housing = fetch_california_housing()
X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, random_state=42)


normalization_layer = tf.keras.layers.Normalization()           # standarize the inputs
hidden_layer1 = tf.keras.layers.Dense(30, activation="relu")
hidden_layer2 = tf.keras.layers.Dense(30, activation="relu")
concat_layer = tf.keras.layers.Concatenate()
output_layer = tf.keras.layers.Dense(1)                         # Dense without any activation function


input_ = tf.keras.layers.Input(shape=X_train.shape[1:])         # Input object
normalized = normalization_layer(input_)                        # normalization layer as functional API, passing it the Input object -> We are telling keras how it should connect the layers together - no sctisal data is beeing processed yet
hidden1 = hidden_layer1(normalized)
hidden2 = hidden_layer2(hidden1)
concat = concat_layer([normalized, hidden2])                    # concatination -> no more sequenially connections, we concatinate normalized and hidden2
output = output_layer(concat)                                   # final output


model = tf.keras.Model(inputs=[input_], outputs=[output])

print(model.summary())

