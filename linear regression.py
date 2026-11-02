import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(42)

# Data: y = 2x + 1 + noise
X = np.random.randn(1000, 1)
X = np.clip(X, -3, 3)
y = 2 * X + 1 + np.random.randn(1000, 1) * 1.5

# Model
model = LinearRegression()
model.fit(X, y)

# Line from -3 to 3
x_line = np.linspace(-3, 3, 100).reshape(-1, 1)
y_line = model.predict(x_line)

# Plot (hand-drawn xkcd style)
with plt.xkcd():
    plt.figure(figsize=(8, 6))
    plt.scatter(X, y, color="blue", s=15)
    plt.plot(x_line, y_line, color="red", linewidth=4)
    plt.title("Linear Regression")
    plt.xlabel("X - Input")
    plt.ylabel("y - target / true value")
    plt.xlim(-3, 3)
    plt.xticks([-3, -2, -1, 0, 1, 2, 3])
    plt.show()