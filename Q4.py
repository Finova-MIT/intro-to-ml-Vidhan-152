import pandas as pd

data = {'Name': ['Vidhan', 'Hemit', 'Tejas'], 'GPA': [8.5, 9.05, 8.95]}

df = pd.DataFrame(data)

# df.to_csv("DATA.csv",index = True)

print(df)

#Filter 
print(df[df["GPA"] > 8.5])

#Sort
print(df.sort_values(by="GPA" , ascending=False))