import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot

def cancellation_rate_colorbar(cancel_group, cancell_count_airlines):
    '''
    This file produces the cancellation rate of each airline in the form of a stacked bar chart.
    The airlines are ranked in descending order of number of cancellations for each airline.
    :param df: the data frame for all the data in 2018.csv
    :param code_name: the dictionary recording airline code as key and airline name as value
    :return: bar chart for total cancellation
    '''

    assert isinstance(cancel_group, pd.DataFrame)
    assert isinstance(cancell_count_airlines, pd.DataFrame)

    cancell_count_airlines['Rate'] = cancell_count_airlines['Cancelled'] / cancell_count_airlines['Numbers']
    trace = go.Bar(
        x=cancel_group['OP_CARRIER'],
        y=cancell_count_airlines['Rate'],
        marker=dict(
            color=cancell_count_airlines['Rate'],
            colorscale='Reds',
            showscale=True
        )
    )

    data = [trace]
    layout = go.Layout(
        title='Cancel rate of each Airline',
        yaxis=dict(title='Airlines'))

    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(barmode='group', xaxis_tickangle=45)
    iplot(fig)

def main():
    df_airline2018, df = data_loader()
    code_name = get_full_code2name_dict(df_airline2018)
    cancel_group, cancell_count_airlines = get_cancelled(df, code_name)
    cancellation_rate_colorbar(cancel_group, cancell_count_airlines)

if __name__ == '__main__':
    import sys
    import os

    module_path = os.path.abspath(os.path.join('..'))
    sys.path.append(module_path)
    from utils import data_loader, get_full_code2name_dict, get_cancelled
    main()