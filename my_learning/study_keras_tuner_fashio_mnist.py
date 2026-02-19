import keras_tuner as kt
import tensorflow as tf

def build_model(hp):        # hp -> Hyper Parameters
    n_hidden = hp.Int("n_hidden", min_value=0, max_value=8, default=2)
    n_neurons = hp.Int("n_neurons", min_value=16, max_value=256)
    learning_rate = hp.Float("learning_rate", min_value=1e-4, max_value=1e-2, sampling="log")
    optimizer = hp.Choice("optimizer", values=["sgd", "adam"])

    if optimizer == "sgd":
        optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate)
    else: 
        optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Flatten())

    for _ in range(n_hidden):
        model.add(tf.keras.layers.Dense(n_neurons, activation="relu"))
    model.add(tf.keras.layers.Dense(10, activation="softmax"))
    model.compile(loss="sparse_categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])

    return model




fashion_mnist = tf.keras.datasets.fashion_mnist.load_data()
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist
X_train, y_train = X_train_full[:-5000], y_train_full[:-5000]
X_valid, y_valid = X_train_full[-5000:], y_train_full[-5000:]
X_train_255, X_valid_255, X_test_255 = X_train/255, X_valid/255, X_test/255




"""
RandomSearch
- calls build_model()
- run 5 trails - each trialmbuilds a model using hyperparameters sampled randomly
- train with 10 epochs
- save to directory my_fashion_mnist/my_rnd_search
- overwrite = True -> my_rnd_search is deletd befire training starts
- objective="val_accuracy"  the tuner prefers models with a higher validation accuracy

"""
random_search_tuner = kt.RandomSearch(
    build_model, objective="val_accuracy", max_trials=5, overwrite=True, directory="my_learning/my_fashion_mnist", project_name="my_learning/my_rnd_search", seed=42
)
random_search_tuner.search(X_train_255, y_train, epochs=10, validation_data=(X_valid_255, y_valid))

top3_params = random_search_tuner.get_best_models(num_models=3)
best_model = top3_params[0]
print(best_model.summary())    # best hyperparameter values


best_trial = random_search_tuner.oracle.get_best_trials(num_trials=1)[0]
print("\nBest trial summary\n", best_trial.summary())


# fit the best model
best_model.fit(X_train_full, y_train_full, epochs=10)
test_loss, test_accuracy = best_model.evaluate(X_test, y_test)
print("test_loss ", test_loss, "test_accuracy ", test_accuracy)
