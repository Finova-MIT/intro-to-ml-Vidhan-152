import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 6)
y1 = [85, 90, 88, 92, 87]  # Marks in Math
y2 = [80, 84, 86, 79, 83]  # Marks in Science
y3 = [75, 78, 82, 76, 81]  # Marks in English


fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Line plot
axes[0].plot(x, y1, marker='o', color='b', label='Math')
axes[0].set_title('Line Plot - Math')
axes[0].set_xlabel('Exams')
axes[0].set_ylabel('Marks')
axes[0].legend()

# Bar plot
axes[1].bar(x, y2, color='g', label='Science')
axes[1].set_title('Bar Plot - Science')
axes[1].set_xlabel('Exams')
axes[1].set_ylabel('Marks')
axes[1].legend()

# Scatter plot
axes[2].scatter(x, y3, color='r', label='English')
axes[2].set_title('Scatter Plot - English')
axes[2].set_xlabel('Exams')
axes[2].set_ylabel('Marks')
axes[2].legend()


plt.show()
