import matplotlib.pyplot as plt
# Data
hours = [1, 2, 3, 4, 5]
marks = [20, 35, 50, 65, 80]
# Plot the graph
plt.plot(hours, marks, marker='o')
# Labels and title
plt.xlabel("Study Hours")
plt.ylabel("Exam Marks")
plt.title("Study Hours vs Exam Marks")
# Display graph
plt.show()
