import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DATA.csv")

#Box PLot

sns.boxplot(y=df['GPA'])
plt.show()

#Histogram and desnsity plot

sns.histplot(df['GPA'], kde=True)
plt.show()