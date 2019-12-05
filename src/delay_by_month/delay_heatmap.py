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