import pandas as pd
import plotly.graph_objs as go

def delay_by_month(df, month_dict):
    '''
    This function plots the delay of each flight by month
    :param df: the data frame for all the data in 2018.csv
    :param month_dict: a month number to month dates dictionary
    :return:
    '''
    assert isinstance(df, pd.DataFrame)
    assert isinstance(month_dict, dict)

    month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    df_day_delay = df[df['ARR_DELAY'] > 0]
    df_day_delay = df_day_delay.groupby(['FL_DATE'])['ARR_DELAY'].count().sort_values(ascending=False)

    monthly_delay = dict()
    for i in month_dict:
        monthly_delay[i] = 0
        for d in month_dict[i]:
            monthly_delay[i] += df_day_delay[d]

    layout = go.Layout(title='Number of delayed flights for each month',
                       xaxis={'title': 'Months'},
                       yaxis={'title': 'Number of Flights'},
                       )
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(x=month_name, y=list(monthly_delay.values()), line_color='Blue',
                             name='lines'))
    fig.show()

def main():
    df_airline2018, df = data_loader()
    month_dict = get_month_dict()
    delay_by_month(df, month_dict)

if __name__ == '__main__':
    import sys
    import os

    module_path = os.path.abspath(os.path.join('..'))
    sys.path.append(module_path)
    from utils import data_loader, get_month_dict
    main()