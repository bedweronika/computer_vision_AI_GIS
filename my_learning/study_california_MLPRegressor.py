from sklearn.datasets import fetch_california_housing
from sklearn.metrics import root_mean_squared_error # before was: mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor     # MLP with tree hidden layers composed of 50 neurons each
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

"""

"""
print("Start script")
"fetch data"
housing = fetch_california_housing()
print(housing.data.shape, housing.target.shape)
print(housing.feature_names[0:6])

"split data"
X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, random_state=42)

"pipeline to standarize the input"
mlp_reg = MLPRegressor(hidden_layer_sizes=[50, 50, 50], random_state=42)
pipeline = make_pipeline(StandardScaler(), mlp_reg)
pipeline.fit(X_train, y_train)  # trained uding gradiend descent, does not coverage when the features have very different scales
y_pred=pipeline.predict(X_valid)
rmse = root_mean_squared_error(y_valid, y_pred) # result is about 0.505


print("End script")