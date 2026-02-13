import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from a_sequential_API import model

to_print = False



fashion_mnist = tf.keras.datasets.fashion_mnist.load_data()
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist
X_train, y_train = X_train_full[:-5000], y_train_full[:-5000]
X_valid, y_valid = X_train_full[-5000:], y_train_full[-5000:]
X_train_255, X_valid_255, X_test_255 = X_train/255, X_valid/255, X_test/255


class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]


if to_print:
    index_n = 10
    print(class_names[y_train[index_n]])
    print(y_train[index_n])

    #plt.imshow(X_train[index_n])
    #plt.show()

    #print(y_valid_255[index_n])
    plt.imshow(X_valid_255[index_n])
    plt.show()


"""
32 bathes
55000 images
1719 batches per epoch   ->   1718 of size 32 + 1 size of 24
"""


history = model.fit(X_train_255, y_train, epochs = 2, validation_data = (X_valid_255, y_valid))
print("params: \n", history.params)
print("history: \n", history.history.keys())

print(model.evaluate(X_test_255, y_test))

show_history_param = False
if show_history_param:
    pd.DataFrame(history.history).plot(figsize=(8, 5), xlim=[0, 29], ylim=[0, 1], grid=True, xlabel="Epoch", style=["r--", "r--.", "b-", "b-*"])
    plt.show()

# prediction 
X_new = X_test_255[:3]

y_prob = model.predict(X_new)   # sklearn predict_proba()
print("PREDICTION: \n", y_prob.round(2))

y_pred = y_prob.argmax(axis=-1)
print(y_pred)
print(np.array(class_names)[y_pred])

y_new = y_test[:3]
print()

show_x_NEW = True
if show_x_NEW:
    fig, axes = plt.subplots(1, 3, figsize=(9, 5))

for i in range(3):
    axes[i].imshow(X_new[i])
    axes[i].set_title(f"{class_names[y_new[i]]}")
    axes[i].axis("off")

plt.tight_layout()
plt.show()




