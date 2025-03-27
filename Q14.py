import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load Iris dataset
df = sns.load_dataset('iris')

print(df.head())

# Basic info and summary
print(df.info())
print(df.describe())

sns.pairplot(df, hue='species')
plt.show()