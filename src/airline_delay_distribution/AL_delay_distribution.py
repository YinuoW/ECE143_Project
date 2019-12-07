import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def AL_delay_distribution(df, code_name):
    '''
    This function generates the scatter plot of all flights of top 10 airlines, with the delay time as x-axis.
    df: the data frame for all the data in 2018.csv
    code_name: the dictionary recording airline code as key and airline name as value
    output: scatter plot
    '''
    assert isinstance(df, pd.DataFrame)
    assert isinstance(code_name, dict)

    df = df[['OP_CARRIER', 'ARR_DELAY']]

    to_drop = ['AS', 'EV', 'F9', 'G4', 'HA', 'NK', 'VX', 'YV']
    df = df[~df['OP_CARRIER'].isin(to_drop)]

    df3 = df.loc[:, ['OP_CARRIER', 'ARR_DELAY']]
    df3['OP_CARRIER'] = df3['OP_CARRIER'].replace(code_name)
    qualitative_colors = sns.color_palette("Set3", 18)
    ax = sns.stripplot(y="OP_CARRIER", x="ARR_DELAY", data=df3, jitter=True, linewidth=0.2, palette=qualitative_colors)
    ax.set_xticklabels(['{:2.0f}h{:2.0f}m'.format(*[int(y) for y in divmod(x, 60)])
                        for x in ax.get_xticks()])
    ax.set_title('Arrival Delay Distribution of Airlines')
    plt.show()

def main():
    df_airline2018, df = data_loader()
    code_name = get_part_code2name_dict(df_airline2018)
    AL_delay_distribution(df, code_name)

if __name__ == '__main__':
    import sys
    import os

    module_path = os.path.abspath(os.path.join('..'))
    sys.path.append(module_path)
    from utils import data_loader, get_part_code2name_dict

    main()
