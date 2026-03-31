#regression with PCA and without PCA

from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

X, y = load_boston(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Without PCA
model = LinearRegression()
model.fit(X_train, y_train)
print("Without PCA:", model.score(X_test, y_test))

# With PCA
pca = PCA(n_components=5)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

model.fit(X_train_pca, y_train)
print("With PCA:", model.score(X_test_pca, y_test))
