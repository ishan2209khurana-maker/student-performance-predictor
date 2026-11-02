import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

X = np.array([[1,2],[2,3],[3,3],[6,7],[7,8],[8,8]])
y = np.array([0,0,0,1,1,1])
new_point = np.array([[4,5]])

model = SVC(kernel="linear", C=1e5)
model.fit(X, y)

pred = model.predict(new_point)[0]
print("New point class:", pred)
print("Support vectors:", model.support_vectors_)

w = model.coef_[0]
b = model.intercept_[0]
xs = np.linspace(0, 9, 100)
ys = -(w[0]*xs + b) / w[1]
margin = 1 / w[1]

plt.scatter(X[y==0,0], X[y==0,1], c="blue", label="Class 0")
plt.scatter(X[y==1,0], X[y==1,1], c="green", label="Class 1")
plt.scatter(new_point[:,0], new_point[:,1], c="red", s=150, label=f"New point (Class {pred})")
plt.plot(xs, ys, "k--", label="Decision boundary")
plt.plot(xs, ys + margin, "gray", linestyle=":", label="Margin")
plt.plot(xs, ys - margin, "gray", linestyle=":")
plt.scatter(model.support_vectors_[:,0], model.support_vectors_[:,1],
            s=200, facecolors="none", edgecolors="k", label="Support vectors")

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Support Vector Machine (SVM)")
plt.xlim(0, 9)
plt.ylim(0, 9)
plt.grid(True)
plt.legend(loc="lower right")
plt.show()
