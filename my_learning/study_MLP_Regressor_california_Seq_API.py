from sklearn.datasets import fetch_california_housing
from sklearn.metrics import root_mean_squared_error # before was: mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor     # MLP with tree hidden layers composed of 50 neurons each
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler



"fetch data"
housing = fetch_california_housing()
print(housing.data.shape, housing.target.shape)
print(housing.feature_names[0:6])

"split data"
X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, random_state=42)

show_MLP_PROGRESSOR_sklearn = False
if show_MLP_PROGRESSOR_sklearn:

    "pipeline to standarize the input"
    mlp_reg = MLPRegressor(hidden_layer_sizes=[50, 50, 50], random_state=42)
    pipeline = make_pipeline(StandardScaler(), mlp_reg)
    pipeline.fit(X_train, y_train)  # trained using gradiend descent, does not coverage when the features have very different scales
    y_pred=pipeline.predict(X_valid)
    rmse = root_mean_squared_error(y_valid, y_pred) # result is about 0.505




""" MLP Regressor with sequential API """
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

"""3 hidden layers with 50 neurons"""
tf.random.set_seed(42)
norm_layer = tf.keras.layers.Normalization(input_shape=X_train.shape[1:])
model = tf.keras.Sequential([
    norm_layer,
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(1)                        # 1 output layer, , to predict single value
])

optimizer = tf.keras.optimizers.Adam(learning_rate = 1e-3)
model.compile(loss = "mse", optimizer=optimizer, metrics=["RootMeanSquaredError"])
norm_layer.adapt(X_train)
history = model.fit(X_train, y_train, epochs=20, validation_data = (X_valid, y_valid))
mse_test, rmse_testr = model.evaluate(X_test, y_test)
X_new = X_test[:3]
y_pred = model.predict(X_new)

pd.DataFrame(history.history).plot(figsize=(8, 5), xlim=[0, 19], ylim=[0, 2], grid=True, xlabel="Epoch", style=["r--", "r--.", "b-", "b-*"])
plt.show()