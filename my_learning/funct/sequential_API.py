import tensorflow as tf

run1_bool = False
run2_bool = True
tf.random.set_seed(42)

if run1_bool:
    model = tf.keras.Sequential()       # sequential API
    model.add(tf.keras.layers.Input(shape=[28, 28]))            # Input layer to specify the shape of instance. keras can determine the shape of the connection weight matrix of the first hidden layer
    model.add(tf.keras.layers.Flatten())                        # convert each image into 1D array
    model.add(tf.keras.layers.Dense(300, activation='relu'))    # Dense hidden layer with 300 neurons with ReLu activation function
    model.add(tf.keras.layers.Dense(100, activation='relu'))    # Dense hidden layer with 100 neurons with ReLu activation function
    model.add(tf.keras.layers.Dense(10, activation='softmax'))  # Dense hidden layer with 10 neurons with softmax activation function


if run2_bool:
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=[28, 28]),          # 784 --- explanation ---->>> batch shape [32, 28, 28]   --- FLATTEN --> [32, 784]
        tf.keras.layers.Dense(300, activation='relu'),
        tf.keras.layers.Dense(100, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])


print(model.summary())
# 784 * 300 + = 235200 
# 235200 + 300 (bias) = 235500 -> parameters        ---->>  a lot of flexibility for model to fit training data but when not a lot traning data it casuse OVERFITTING
#tf.keras.utils.plot_model(model)

# to clean the global keras state use: tf.keras.backend.clear_session() 

print(model.layers)
hidden1 = model.layers[1]
print(hidden1.name)
print(model.get_layer('dense') is hidden1)


# weights and bias
weights, biases = hidden1.get_weights()
print(weights)
print(weights.shape)

print(biases)
print(biases.shape)

# for use different initialization method: kernel_initializer (kernel is another name for the matrix of connectio weights) or bias_initializer (when creating the layer)

### COMPILE
model.compile(
    loss="sparse_categorical_crossentropy",     # == tf.keras.losses.sparse_categorical_crossentropy
    optimizer="sgd",                            # == tf.keras.optimizier.SGD()              # stohastic gradient descent
    metrics=['accuracy'])                       # == [tf.keras.metrics.sparse_categorical_accuracy]             --> keras.io/api/ losses, optimiries, metrics