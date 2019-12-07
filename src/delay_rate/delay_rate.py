import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def delay_rate(airlines, delay_freq):
    '''
    This file generate the delay and ontime rates as percantage of each airline
    :param airlines: list stores selected airlines
    :param delay_freq: dataframe about delay freq for airlines
    :return:
    '''

    assert isinstance(airlines, list)
    assert isinstance(delay_freq, pd.DataFrame)
    font = {'size': 20}
    plt.rc('font', **font)

    # visualization
    width = 0.7
    plt.figure(figsize=(9, 7))

    p1 = plt.barh(delay_freq.index, delay_freq['delay'], width, label='Delay')
    p2 = plt.barh(delay_freq.index, delay_freq['on-time_and_adv'], width, left=delay_freq['delay'],
                  label='On-time/Early')
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.legend(bbox_to_anchor=(1, -0.3), loc='lower right')
    plt.xlabel('Rate')
    plt.ylabel('Airlines')
    plt.show()

def main():
    airlines, delay_freq = get_delay_freq('delay_rate.csv')
    delay_rate(airlines, delay_freq)

if __name__ == '__main__':
    import sys
    import os
    module_path = os.path.abspath(os.path.join('..'))
    sys.path.append(module_path)
    from utils import get_delay_freq
    main()