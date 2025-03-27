import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Math': [85, 90, 78, 92, 88],
    'Science': [82, 95, 80, 89, 84],
    'English': [78, 85, 86, 80, 77],
    'History': [75, 89, 84, 90, 82]
}

df = pd.DataFrame(data)

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()