import pandas as pd
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go

def count_flight_airline_colorbar(df, code_name):
    '''
    generate the total number of flights with color bar
    :param df: the data frame for all the data in 2018.csv
    :param code_name: the dictionary recording airline code as key and airline name as value
    :return: plot with colorbar
    '''

    assert isinstance(df, pd.DataFrame)
    assert isinstance(code_name, dict)

    df4 = df.loc[:, ['OP_CARRIER']]
    df4['OP_CARRIER'] = df4['OP_CARRIER'].replace(code_name)

    airline_group = df4.groupby(['OP_CARRIER'])['OP_CARRIER'].count().sort_values(ascending=False)
    trace = go.Bar(x=airline_group[:10].index,
                   y=airline_group[:10].values,
                   name='airlines',
                   marker={
                       'color': airline_group[:10].values,
                       'colorscale': 'Oranges',
                       'showscale': True,
                   },
                   )

    layout = go.Layout(title='Number of Flights of Airlines',
                       xaxis={'title': 'Airlines'},
                       yaxis={'title': 'Number of Flights'},
                       autosize=False,
                       width=800,
                       height=500,
                       margin=go.layout.Margin(
                           l=50,
                           r=40,
                           b=80,
                           t=80,
                           pad=4
                       ))
    fig = go.Figure(data=[trace], layout=layout)
    iplot(fig, filename='airline_bar')

def main():
    df_airline2018, df = data_loader()
    code_name = get_full_code2name_dict(df_airline2018)
    count_flight_airline_colorbar(df, code_name)

if __name__ == '__main__':
    import sys
    import os

    module_path = os.path.abspath(os.path.join('..'))
    sys.path.append(module_path)
    from utils import data_loader, get_full_code2name_dict
    main()