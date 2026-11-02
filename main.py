import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load dataset
df = pd.read_csv("student_data.csv")
print(df.head())
print(df.info())

# 2. Preprocessing
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates().dropna()

# 3. Exploratory data analysis
print(df.describe())
print(df.corr())

# 4. Visualization
plt.hist(df["Final_Score"], bins=10, edgecolor="black")
plt.xlabel("Final Score"); plt.ylabel("Number of Students")
plt.title("Distribution of Student Performance Scores"); plt.show()

plt.scatter(df["Study_Hours"], df["Final_Score"])
plt.xlabel("Study Hours per Day"); plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score"); plt.show()

# 5. Features and target
X = df[["Study_Hours", "Attendance", "Previous_Score"]]
y = df["Final_Score"]

# 6. Train-test split (80:20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 7. Train model
model = LinearRegression()
model.fit(X_train, y_train)
print("Intercept:", model.intercept_)
print("Coefficients:", dict(zip(X.columns, model.coef_)))

# 8. Predict
y_pred = model.predict(X_test)
print(pd.DataFrame({"Actual": y_test.values, "Predicted": y_pred.round(2)}).head(10))

# 9. Evaluate
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print("MAE :", round(mae, 2))
print("MSE :", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R2  :", round(r2, 4))

plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
plt.xlabel("Actual Score"); plt.ylabel("Predicted Score")
plt.title("Actual vs Predicted Student Performance"); plt.show()

# 10. Predict for a new student
new = pd.DataFrame([[6.0, 90.0, 70.0]], columns=X.columns)
print("Predicted Final Score:", round(model.predict(new)[0], 2))