import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Heart_monitoring.csv")

print(df.shape)

#Checking first 5 rows
print(df.head())

#checking 5 summary
print(df.describe())

#checking datatypes
print(df.info())

#checking for na values
print(df.isna())

# Age group vs blood pressure
df['Age Group'] = ((df['Age'] - 18) // 10) * 10 + 18

avg_bp = df.groupby('Age Group')['Blood Pressure'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Age Group', y='Blood Pressure', data=avg_bp, palette='viridis', edgecolor='black')
plt.title('Average Blood Pressure Across Age Groups', fontsize=14, fontweight='bold')
plt.xlabel('Age Group')
plt.ylabel('Average Blood Pressure')
plt.xticks(rotation=45)
plt.show()



# Calculate average Blood Pressure for each Cholesterol Group
df['Cholesterol Group'] = (df['Cholesterol Level'] // 10) * 10
avg_bp_chol = df.groupby('Cholesterol Group')['Blood Pressure'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Cholesterol Group', y='Blood Pressure', data=avg_bp_chol, palette='crest', edgecolor='black')
plt.title('Average Blood Pressure Across Cholesterol Levels')
plt.xlabel('Cholesterol Level Range')
plt.ylabel('Average Blood Pressure')
plt.xticks(rotation=45)
plt.show()


#sleep cycle distribution

plt.figure(figsize=(10, 6))
sns.histplot(df['Sleep Hours'], bins=10, kde=True, color='lightcoral')
plt.title('Distribution of Sleep Hours')
plt.xlabel('Sleep Hours')
plt.ylabel('Count')
plt.show()


'''
Insights - 

1) In the age range of 18 - 28 we have high blood pressure 140+
2) People have high Cholesterol 
3) People are getting less sleep (many people are sleeping less than 7 hours)

'''