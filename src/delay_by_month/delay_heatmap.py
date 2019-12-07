'''
This file creates the heatmap for total time of delays per month for each airline.
Plot the heatmap from the delay_heatmap.csv created by the data extraction function.

:param data_dir: name of csv file
:type data_dir: str

'''


import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go

data_dir = "delay_heatmap.csv"
df1_transposed = pd.read_csv(data_dir,index_col=0)
print(df1_transposed)
plt.rcParams['font.size'] = 20
fig = plt.figure(figsize=(20,10))
sns.heatmap(df1_transposed, linecolor="w", linewidths=1, cmap="Reds", annot_kws={'size':10},)
plt.show()
