import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
math_marks = [85, 90, 88, 92, 87]


plt.plot(x, math_marks, marker='o', color='orange', label='Math')


plt.title('Math Performance')
plt.xlabel('Exam Number')
plt.ylabel('Marks')
plt.legend()

plt.show()