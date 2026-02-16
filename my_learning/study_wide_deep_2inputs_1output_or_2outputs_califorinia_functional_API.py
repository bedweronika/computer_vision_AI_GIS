from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import tensorflow as tf

use_auxiliary_output = True

housing = fetch_california_housing()
X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, random_state=42)

input_wide = tf.keras.layers.Input(shape=[5])       # features 0 to 4
input_deep = tf.keras.layers.Input(shape=[6])       # features 2 to 7
norm_layer_wide = tf.keras.layers.Normalization()
norm_layer_deep = tf.keras.layers.Normalization()

norm_wide = norm_layer_wide(input_wide)
norm_deep = norm_layer_deep(input_deep)

hidden1 = tf.keras.layers.Dense(30, activation="relu")(norm_deep)
hidden2 = tf.keras.layers.Dense(30, activation="relu")(hidden1)
concat = tf.keras.layers.concatenate([norm_wide, hidden2])
if use_auxiliary_output:
    output = tf.keras.layers.Dense(1)(concat)
    aux_output = tf.keras.layers.Dense(1)(hidden2)
    model = tf.keras.Model(inputs=[input_wide, input_deep], outputs=[output, aux_output])
    optimizer = tf.keras.optimizers.Adam(learning_rate=1e-3)
    model.compile(loss=("mse", "mse"), loss_weights=(0.9, 0.1), optimizer=optimizer, metrics=["RootMeanSquaredError", "RootMeanSquaredError"])
else :
    output = tf.keras.layers.Dense(1)(concat)
    model = tf.keras.Model(inputs=[input_wide, input_deep], outputs=[output])
    optimizer = tf.keras.optimizers.Adam(learning_rate=1e-3)
    model.compile(loss="mse", optimizer=optimizer, metrics=["RootMeanSquaredError"])

print(model.summary())


X_train_wide, X_train_deep = X_train[:, :5], X_train[:, 2:]
X_valid_wide, X_valid_deep = X_valid[:, :5], X_valid[:, 2:]
X_test_wide, X_test_deep = X_test[:, :5], X_test[:, 2:]
X_new_wide, X_new_deep = X_test_wide[:3], X_test_deep[:3]
norm_layer_wide.adapt(X_train_wide)
norm_layer_deep.adapt(X_train_deep)

if use_auxiliary_output:
    history = model.fit( (X_train_wide, X_train_deep), (y_train, y_train), epochs=20, validation_data=( (X_valid_wide, X_valid_deep), (y_valid, y_valid) ) )
    eval_results = model.evaluate( (X_test_wide, X_test_deep), (y_test, y_test) )
    weighted_sum_of_losses, main_loss, aux_loss, main_rmse, aux_rmse = eval_results
    y_pred_main, y_pred_aux = model.predict((X_new_wide, X_new_deep))
    # other way to return the results as dict
    # y_pred_tuple = model.predict((X_new_wide, X_new_deep))
    # y_pred = dict(zip(model.output_names, y_pred_tuple))
    print(weighted_sum_of_losses, main_loss, aux_loss, main_rmse, aux_rmse)

else:
    history = model.fit( (X_train_wide, X_train_deep), y_train, epochs=20, validation_data=( (X_valid_wide, X_valid_deep), y_valid ) )
    mse_test = model.evaluate( (X_test_wide, X_test_deep), y_test )
    y_pred = model.predict((X_new_wide, X_new_deep))

print(history.history)