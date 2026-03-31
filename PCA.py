#6 PCA
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

data = load_iris()
X = data.data
y = data.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

pca_model = PCA(n_components=2)
X_train_pca = PCA.fit_transform(X_train)
X_test_pca = PCA.transform(X_test)


print("Original shape:", X_train.shape)
print("Reduced shape:", X_train_pca.shape)

