import datetime
import pandas as pd
import plotly.graph_objs as go

data_dir = "../../data/2018.csv"
df = pd.read_csv(data_dir)

month_dict = dict()
month_31=[1,3,5,7,8,10,12]
month_30=[4,6,9,11]
for i in range(1, 13):
    day_list = list()
    if i==2:
        for j in range(1,29):
            d = datetime.date(2018, i, j)
            day_list.append(str(d))
    if i in month_30:
        for j in range(1,31):
            d = datetime.date(2018, i, j)
            day_list.append(str(d))
    if i in month_31:
        for j in range(1,32):
            d = datetime.date(2018, i, j)
            day_list.append(str(d))
    month_dict[i] = day_list

month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

df_day_delay = df[df['ARR_DELAY']>0]
df_day_delay = df_day_delay.groupby(['FL_DATE'])['ARR_DELAY'].count().sort_values(ascending=False)

monthly_delay = dict()
for i in month_dict:
    monthly_delay[i] = 0
    for d in month_dict[i]:
        monthly_delay[i] += df_day_delay[d]

layout = go.Layout(title='Number of delayed flights for each month',
                    xaxis={'title':'Months'},
                    yaxis={'title':'Number of Flights'},
                    )
fig = go.Figure(layout = layout)
fig.add_trace(go.Scatter(x=month_name, y=list(monthly_delay.values()),line_color='Blue',
                    name='lines'))
fig.show()