import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Hemit', 'Vidhan', 'Tejas', 'Hemit', 'Tejas'],
    'Math': [85, 92, 78, 80, 82],
    'Science': [88, 95, 82, 85, 89],
    'English': [80, 86, 77, 79, 75],
    'History': [90, 84, 88, 92, 85],
    'Computer': [95, 98, 85, 91, 86]
}

df = pd.DataFrame(data)

grouped_data = df.groupby('Name').sum()

print(grouped_data)
grouped_data.plot(kind='bar')
plt.show()