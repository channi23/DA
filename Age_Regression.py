import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample dataset (features → height, weight; target → age)
X = np.array([
    [150, 50],
    [160, 60],
    [170, 65],
    [180, 75],
    [155, 55],
    [165, 62]
])

y = np.array([20, 25, 30, 35, 22, 28])  # Age

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Evaluation
print("Predicted:", pred)
print("Actual:", y_test)
print("Accuracy (R2):", model.score(X_test, y_test))