import pandas as pd
import matplotlib.pyplot as plt

def box_line_delay_vs_airline_in2018(file):
    '''
    This file extracts the dataframe from delay_vs_airline_in2018.py in order to draw the delay box line plots of airlines.
    :param file: a string represent the file name
    :return:
    '''
    assert isinstance(file, str)
    delay_vs_airline_in2018 = pd.read_csv(file,
                                          usecols=['9E', 'YX', 'UA', 'MQ', 'DL', 'AA', 'OO', 'OH', 'WN', 'NK', 'B6'])

    airlines = list(delay_vs_airline_in2018.columns)
    airlines_name = {'F9': 'Frontier Airlines', '9E': 'Endeavor Air', 'EV': 'ExpressJet Airlines',
                     'YX': 'Midwest Airlines', 'UA': 'United Airlines', 'VX': 'Virgin America', 'MQ': 'Envoy Air',
                     'DL': 'Delta Air Lines', 'AA': 'American Airlines', 'OO': 'SkyWest Airlines',
                     'YV': 'Mesa Airlines', 'HA': 'Hawaiian Airlines',
                     'AS': 'Alaska Airlines', 'OH': 'PSA Airlines', 'G4': 'Allegiant Air', 'WN': 'Southwest Airlines',
                     'NK': 'Spirit Airlines', 'B6': 'JetBlue Airways'}
    delay_vs_airline_in2018 = delay_vs_airline_in2018.rename(columns=airlines_name)
    delay_vs_airline_in2018.boxplot(sym='', vert=False, showmeans=True, manage_ticks=True)

    plt.xlabel('Average delay')
    plt.ylabel('Airlines')
    plt.title('Average delay vs airlines')
    plt.show()

def main():
    file = 'delay_vs_airline_in2018.csv'
    box_line_delay_vs_airline_in2018(file)

if __name__ == '__main__':
    main()