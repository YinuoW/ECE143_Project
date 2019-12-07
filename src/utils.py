import pandas as pd

def get_full_code2name_dict(df_airline2018):
    '''
    generate a code to name dictionary from a dataframe
    :param df_airline2018: the data frame of airlines in 2018
    :return: a code to name dictionary
    '''
    assert isinstance(df_airline2018, pd.DataFrame)

    airlines_code = list(df_airline2018['Code'])
    airlines_name = list(df_airline2018['Description'])

    code_name = dict()
    for idx, air in enumerate(airlines_code):
        code_name[air] = airlines_name[idx]

    return code_name


def data_loader():
    '''
    Load data from our dataset
    :return: dataframe including airlines code to name and full data from 2018.csv
    '''
    data_dir = "../../data/2018.csv"
    airline2018_dir = "../../data/airline2018_lookup.csv"

    df_airline2018 = pd.read_csv(airline2018_dir)
    df = pd.read_csv(data_dir)
    return df_airline2018, df


def get_part_code2name_dict(df_airline2018):
    '''
    generate a code to name dictionary of only selected airlines from a dataframe
    :param df_airline2018: the data frame of airlines in 2018
    :return: a code to name dictionary
    '''
    import re
    assert isinstance(df_airline2018, pd.DataFrame)
    airlines_code = list(df_airline2018['Code'])
    airlines_name = list(df_airline2018['Description'])
    # remove all words within brackets
    airlines_name = [re.sub("[\(\[].*?[\)\]]", "", elem) for elem in airlines_name]
    code_name = dict()
    for idx, air in enumerate(airlines_code):
        code_name[air] = airlines_name[idx]

    return code_name

def get_month_dict():
    '''
    This generate a month number to month dates dictionary
    :return: dictionary
    '''
    import datetime
    month_dict = dict()
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]
    for i in range(1, 13):
        day_list = list()
        if i == 2:
            for j in range(1, 29):
                d = datetime.date(2018, i, j)
                day_list.append(str(d))
        if i in month_30:
            for j in range(1, 31):
                d = datetime.date(2018, i, j)
                day_list.append(str(d))
        if i in month_31:
            for j in range(1, 32):
                d = datetime.date(2018, i, j)
                day_list.append(str(d))
        month_dict[i] = day_list
    return month_dict

def get_cancelled(df, code_name):
    '''
    This function gets two dataframes for cancellation of selected airlines
    :param df: the data frame for all the data in 2018.csv
    :param code_name: the dictionary recording airline code as key and airline name as value
    :return: two dataframes
    '''
    assert isinstance(df, pd.DataFrame)
    assert isinstance(code_name, dict)

    df4 = df.loc[:, ['OP_CARRIER']]
    df4['OP_CARRIER'] = df4['OP_CARRIER'].replace(code_name)
    count = []
    op_list = df4['OP_CARRIER'].unique()
    for op in op_list:
        c = df4.loc[df4['OP_CARRIER'] == op].count()
        count.append(c[0])

    name_count_dict = dict()
    op_list = df4['OP_CARRIER'].unique()
    for idx, op in enumerate(op_list):
        name_count_dict[op] = count[idx]

    name_count_dict_value = list(name_count_dict.values())
    name_count_dict_value.sort(reverse=True)
    new_key = list()
    for i in name_count_dict_value:
        for key in name_count_dict.keys():
            if name_count_dict[key] == i:
                new_key.append(key)

    name_count_dict_ordered = dict()
    for idx, op in enumerate(new_key):
        name_count_dict_ordered[op] = name_count_dict_value[idx]

    keylist = list(name_count_dict_ordered.keys())
    valuelist = list(name_count_dict_ordered.values())
    df_ = pd.DataFrame({'Airlines': keylist[0:10], 'Number of Flights': valuelist[0:10]})
    df_[['Airlines', 'Number of Flights']]

    #### Total cancellation
    cancel_group = df.groupby(['OP_CARRIER'])['CANCELLED'].sum().sort_values(ascending=False)
    cancel_group = cancel_group.reset_index()
    cancel_group['OP_CARRIER'] = cancel_group['OP_CARRIER'].replace(code_name)

    drop_list = list()
    for idx, i in enumerate(cancel_group['OP_CARRIER']):
        if i not in keylist[0:10]:
            drop_list.append(idx)
    cancel_group = cancel_group.drop(drop_list)
    cancel_group_new = pd.DataFrame(list(cancel_group['CANCELLED']), index=cancel_group['OP_CARRIER'],
                                    columns={'Cancelled'})
    df_new = pd.DataFrame(list(df_['Number of Flights']), index=df_['Airlines'], columns={'Numbers'})

    cancell_count_airlines = pd.concat([cancel_group_new, df_new], axis=1, join='inner')

    return cancel_group, cancell_count_airlines

def get_delay_freq(file):
    '''
    This function get datframe from a extracted .csv file
    :param file: .csv file name
    :return: selected airline names and data frame
    '''
    assert isinstance(file, str)
    delay_freq = pd.read_csv(file, index_col=0, header=0)
    delay_freq = delay_freq.drop(labels=['AS', 'EV', 'F9', 'G4', 'HA', 'NK', 'VX', 'YV'])
    airlines = list(delay_freq.index)
    airlines_name = {'F9': 'Frontier Airlines', '9E': 'Endeavor Air', 'EV': 'ExpressJet Airlines',
                     'YX': 'Midwest Airlines', 'UA': 'United Airlines', 'VX': 'Virgin America', 'MQ': 'Envoy Air',
                     'DL': 'Delta Air Lines', 'AA': 'American Airlines', 'OO': 'SkyWest Airlines',
                     'YV': 'Mesa Airlines', 'HA': 'Hawaiian Airlines',
                     'AS': 'Alaska Airlines', 'OH': 'PSA Airlines', 'G4': 'Allegiant Air', 'WN': 'Southwest Airlines',
                     'NK': 'Spirit Airlines', 'B6': 'JetBlue Airways'}
    delay_freq = delay_freq.rename(index=airlines_name)
    airlines = list(delay_freq.index)
    return airlines, delay_freq
