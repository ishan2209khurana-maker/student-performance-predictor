import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

X = np.array([[1],[2],[3],[6],[7],[8]])
y = np.array([0,0,0,1,1,1])
new_point = np.array([[5]])

model = LogisticRegression()
model.fit(X, y)

pred = model.predict(new_point)[0]
prob = model.predict_proba(new_point)[0][1]
print("New point class:", pred)
print("Probability of Class 1:", prob)

# Sigmoid curve
xs = np.linspace(0, 9, 300).reshape(-1, 1)
ps = model.predict_proba(xs)[:, 1]

plt.figure(figsize=(8, 5))
plt.scatter(X[y==0], y[y==0], c="blue", s=120, label="Class 0")
plt.scatter(X[y==1], y[y==1], c="green", s=120, label="Class 1")
plt.scatter(new_point, [prob], c="red", s=200, label=f"New point (Class {pred})")
plt.plot(xs, ps, "r-", linewidth=2, label="Sigmoid curve")
plt.axhline(0.5, color="gray", linestyle=":", label="Threshold (0.5)")

# Decision boundary (jahan probability = 0.5)
boundary = -model.intercept_[0] / model.coef_[0][0]
plt.axvline(boundary, color="black", linestyle="--", label="Decision boundary")

plt.xlabel("Input")
plt.ylabel("Probability / Class")
plt.title("Logistic Regression Classification")
plt.xlim(0, 9)
plt.ylim(-0.1, 1.1)
plt.grid(True)
plt.legend(loc="center right")
plt.show()
