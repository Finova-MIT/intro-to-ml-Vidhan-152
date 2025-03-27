import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = {
    'Name': ['Hemit', 'Vidhan', 'Tejas', 'Hemit', 'Tejas'],
    'Math': [85, np.nan, 78, 80, 82],
    'Science': [88, 95, np.nan, 85, 89],
    'English': [80, 86, 77, np.nan, 75],
    'History': [90, 84, 88, 92, np.nan],
    'Computer': [np.nan, 98, 85, 91, 86]
}


df = pd.read_csv("DATA.csv", index_col=0)

df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda row: row.fillna(row.mean()), axis=1)

print(df)

grouped = df.groupby("Name").sum()

print(grouped)