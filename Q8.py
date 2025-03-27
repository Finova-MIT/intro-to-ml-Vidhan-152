import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

date_rng = pd.date_range(start='2022-01-01', periods=20)
df_ts = pd.DataFrame({'Date': date_rng, 'Value': np.random.randint(0, 100, size=(20))})
df_ts.set_index('Date', inplace=True)
df_ts.plot()
plt.title("Time Series Plot")
plt.show()