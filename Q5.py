import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("DATA.csv", index_col=False)

print(df.describe())

#Mean

print("Mean : ",df["GPA"].mean())

#Median

print("Median : ",df["GPA"].median())

#Std Deviation

print("STD DEV : ",np.std(df['GPA']))