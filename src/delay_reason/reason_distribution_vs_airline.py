import pandas as pd
import plotly.graph_objs as go

def reason_distribution_vs_airline(df, code_name):
    '''
    This function plots bar chart for delay reasons distribution of selected airlines
    :param df: the data frame for all the data in 2018.csv
    :param code_name: the dictionary recording airline code as key and airline name as value
    :return: bar chart
    '''
    assert isinstance(df, pd.DataFrame)
    assert isinstance(code_name, dict)

    keylist = ['Southwest Airlines Co.', 'Delta Air Lines Inc.', 'American Airlines Inc.', 'SkyWest Airlines Inc.',
               'United Air Lines Inc.', 'Republic Airline', 'JetBlue Airways', 'Envoy Air', 'PSA Airlines Inc.',
               'Endeavor Air Inc.', 'Alaska Airlines Inc.', 'Mesa Airlines Inc.', 'ExpressJet Airlines Inc.',
               'Spirit Air Lines', 'Frontier Airlines Inc.', 'Allegiant Air', 'Hawaiian Airlines Inc.',
               'Virgin America']

    carrier_delay = list()
    for i in keylist[0:10]:
        for key in code_name:
            if code_name[key] == i:
                i = key
        carrier_delay.append(df.loc[df['OP_CARRIER'] == i]['CARRIER_DELAY'].sum())

    whether_delay = list()
    for i in keylist[0:10]:
        for key in code_name:
            if code_name[key] == i:
                i = key
        whether_delay.append(df.loc[df['OP_CARRIER'] == i]['WEATHER_DELAY'].sum())

    aircraft_delay = list()
    for i in keylist[0:10]:
        for key in code_name:
            if code_name[key] == i:
                i = key
        aircraft_delay.append(df.loc[df['OP_CARRIER'] == i]['LATE_AIRCRAFT_DELAY'].sum())

    nas_delay = list()
    for i in keylist[0:10]:
        for key in code_name:
            if code_name[key] == i:
                i = key
        nas_delay.append(df.loc[df['OP_CARRIER'] == i]['NAS_DELAY'].sum())

    security_delay = list()
    for i in keylist[0:10]:
        for key in code_name:
            if code_name[key] == i:
                i = key
        security_delay.append(df.loc[df['OP_CARRIER'] == i]['SECURITY_DELAY'].sum())

    fig = go.Figure(go.Bar(x=keylist[0:10], y=carrier_delay, name='Carrier delay', marker_color='goldenrod'))
    fig.add_trace(go.Bar(x=keylist[0:10], y=security_delay, name='Security delay'))
    fig.add_trace(go.Bar(x=keylist[0:10], y=whether_delay, name='Weather delay', marker_color='burlywood'))
    fig.add_trace(go.Bar(x=keylist[0:10], y=aircraft_delay, name='Aircraft delay', marker_color='saddlebrown'))
    fig.add_trace(go.Bar(x=keylist[0:10], y=nas_delay, name='NAS delay', marker_color='darkorange'))

    fig.update_layout(title='Delay reasons for each airline',
                      yaxis={'title': 'Time'},
                      barmode='stack', xaxis={'categoryorder': 'array', 'categoryarray': keylist[0:10]})
    fig.show()


def main():
    df_airline2018, df = data_loader()
    code_name = get_full_code2name_dict(df_airline2018)
    reason_distribution_vs_airline(df, code_name)

if __name__ == '__main__':
    import sys
    import os

    module_path = os.path.abspath(os.path.join('..'))
    sys.path.append(module_path)
    from utils import data_loader, get_full_code2name_dict
    main()
