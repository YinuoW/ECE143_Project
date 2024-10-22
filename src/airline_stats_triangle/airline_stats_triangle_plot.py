import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def airline_stats_triangle(file):
    '''
    This file plot the scoring map of 6 airlines:
    'Endeavor Air','American Airlines','JetBlue Airways','Delta Air Lines',
    'Envoy Air' , 'PSA Airlines' , 'SkyWest Airlines' , 'United Airlines' ,
    'Southwest Airlines'

    There are 3 parameters in our scoring system: 'Departure delay', 'Arrival delay', 'Cancellations'.
    The closer the score to 1, the better the airline.
    :param file:
    :return:
    '''
    assert isinstance(file, str)

    airlines_stats = pd.read_csv(file, index_col=0, header=0)

    airlines = list(airlines_stats.index)
    airlines_name = {'F9': 'Frontier Airlines', '9E': 'Endeavor Air', 'EV': 'ExpressJet Airlines',
                     'YX': 'Midwest Airlines', 'UA': 'United Airlines', 'VX': 'Virgin America', 'MQ': 'Envoy Air',
                     'DL': 'Delta Air Lines', 'AA': 'American Airlines', 'OO': 'SkyWest Airlines',
                     'YV': 'Mesa Airlines', 'HA': 'Hawaiian Airlines',
                     'AS': 'Alaska Airlines', 'OH': 'PSA Airlines', 'G4': 'Allegiant Air', 'WN': 'Southwest Airlines',
                     'NK': 'Spirit Airlines', 'B6': 'JetBlue Airways'}
    airlines_stats = airlines_stats.rename(index=airlines_name)
    print(airlines_stats)

    def plt_stats(name):
        r = 3
        an = np.linspace(0, 2 * np.pi, 100)
        linestyles = ['solid', 'dashed']
        for i, j in zip([1, 0.5], linestyles):
            plt.plot(i * r * np.cos(an), i * r * np.sin(an), color='#2a7e19', lw=1, linestyle=j)
        plt.axis('equal')
        axis_angle = 2 * np.pi / 8
        for i in [0.5, 1]:
            plt.text(x=i * r * np.cos(axis_angle), y=i * r * np.sin(axis_angle), s=str(i), rotation=45)
        an_axis = [0, 2 * np.pi / 3, 2 * np.pi / 3 * 2]
        axis_name = ['Departure delay', 'Arrival delay', 'Cancellations']

        text_rot = [0, 0, 0]
        offset_x = [-2, 0.05, -0.2]
        offset_y = [0.05, -1.3, 0.1]
        for (i, j, k, l, m) in zip(an_axis, axis_name, text_rot, offset_x, offset_y):
            plt.plot([0, r * np.cos(i)], [0, r * np.sin(i)], color='#2a7e19', lw=1, linestyle='dashed')
            plt.text(x=r * np.cos(i) + l, y=r * np.sin(i) + m, s=j, rotation=k, size=15)
        plt.text(x=-1.5, y=-4, s=name, size=25, color='black')
        x = []
        y = []
        length = []
        for stat in airlines_stats.columns:
            if airlines_stats.loc[name][stat] > 0:
                length.append(r * (1 - airlines_stats.loc[name][stat] / max(list(airlines_stats[stat]))))
            else:
                length.append(r)
        for (i, j) in zip(length, an_axis):
            x.append(i * np.cos(j))
            y.append(i * np.sin(j))

        plt.fill(x, y, color='orange')
        plt.axis('off')
        plt.show()

    name = {'Endeavor Air', 'American Airlines', 'JetBlue Airways', 'Delta Air Lines',
            'Envoy Air', 'PSA Airlines', 'SkyWest Airlines', 'United Airlines',
            'Southwest Airlines'
            }

    plt.figure(figsize=(8, 8))
    for i in name:
        plt_stats(i)

def main():
    file='airlines_stats.csv'
    airline_stats_triangle(file)

if __name__ == '__main__':
    main()
