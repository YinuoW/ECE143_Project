import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def delay_ontime_flights_number(airlines, delay_freq):
    '''
    This file generates the delay and ontime number of flights for each airline
    :param airlines: list stores selected airlines
    :param delay_freq: dataframe about delay freq for airlines
    :return:
    '''

    assert isinstance(airlines, list)
    assert isinstance(delay_freq, pd.DataFrame)
    font = {'size': 20}
    plt.rc('font', **font)

    print(delay_freq)

    # visualization
    width = 0.7
    plt.figure(figsize=(10, 7))
    k = np.arange(len(airlines))
    p1 = plt.barh(k, delay_freq['delay'], width, label='Delay')
    p2 = plt.barh(k, delay_freq['on-time_and_adv'], width, left=delay_freq['delay'], label='On-time/Early')
    plt.legend(bbox_to_anchor=(1, -0.4), loc='lower right')
    plt.yticks(k, airlines)
    ax = plt.axes()
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.0f}'.format(x / 1000) + 'K'))
    plt.xticks(rotation=30)

    plt.show()

def main():
    airlines, delay_freq = get_delay_freq('delay_number.csv')
    delay_ontime_flights_number(airlines, delay_freq)

if __name__ == '__main__':
    import sys
    import os

    module_path = os.path.abspath(os.path.join('..'))
    sys.path.append(module_path)
    from utils import get_delay_freq
    main()