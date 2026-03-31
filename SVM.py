from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load dataset
X, y = load_iris(return_X_y=True)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Accuracy
print("Accuracy:", model.score(X_test, y_test))