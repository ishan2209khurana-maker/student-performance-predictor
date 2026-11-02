import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

X = np.array([[1],[2],[3],[6],[7],[8]])
y = np.array([0,0,0,1,1,1])
new_point = np.array([[5]])

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
pred = knn.predict(new_point)[0]
dist, idx = knn.kneighbors(new_point)

plt.figure(figsize=(8, 5))

# Decision regions
xx = np.linspace(0, 9, 500).reshape(-1, 1)
zz = knn.predict(xx)
plt.fill_between(xx.ravel(), -0.1, 1.1, where=(zz == 0), color="blue", alpha=0.1)
plt.fill_between(xx.ravel(), -0.1, 1.1, where=(zz == 1), color="green", alpha=0.1)

# Points
plt.scatter(X[y==0], y[y==0], c="blue", s=120, label="Class 0")
plt.scatter(X[y==1], y[y==1], c="green", s=120, label="Class 1")
plt.scatter(new_point, [pred], c="red", s=200, label=f"New point (Class {pred})")

# Lines to nearest neighbors
for i in idx[0]:
    plt.plot([new_point[0][0], X[i][0]], [pred, y[i]], "k--", alpha=0.6)

plt.xlabel("Input")
plt.ylabel("Class")
plt.title("KNN Classification (k=3)")
plt.ylim(-0.1, 1.1)
plt.grid(True)
plt.legend(loc="center right")
plt.xlim(0,9)
plt.show()