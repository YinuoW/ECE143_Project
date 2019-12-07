import pandas as pd
import plotly.graph_objs as go

def total_cancellation(cancel_group, cancell_count_airlines):
    '''
    This funtion plots the cancellation rate of each airline as a bar chart.
    :param df: the data frame for all the data in 2018.csv
    :param code_name: the dictionary recording airline code as key and airline name as value
    :return: bar chart for total cancellation
    '''

    assert isinstance(cancel_group, pd.DataFrame)
    assert isinstance(cancell_count_airlines, pd.DataFrame)

    print(cancell_count_airlines)

    layout = go.Layout(title='Cancelled Flights vs. Total Flights',
                       xaxis={'title': 'Airlines'},
                       yaxis={'title': 'Number of Flights'})

    fig = go.Figure(data=[
        go.Bar(name='Cancelled flights', x=cancel_group['OP_CARRIER'], y=cancell_count_airlines['Cancelled']),
        go.Bar(name='Total flights', x=cancel_group['OP_CARRIER'], y=cancell_count_airlines['Numbers'])
    ], layout=layout)
    # Change the bar mode

    fig.update_layout(barmode='group')
    fig.show()


def main():
    df_airline2018, df = data_loader()
    code_name = get_full_code2name_dict(df_airline2018)
    cancel_group, cancell_count_airlines = get_cancelled(df, code_name)
    total_cancellation(cancel_group, cancell_count_airlines)

if __name__ == '__main__':
    import sys
    import os

    module_path = os.path.abspath(os.path.join('..'))
    sys.path.append(module_path)
    from utils import data_loader, get_full_code2name_dict, get_cancelled
    main()