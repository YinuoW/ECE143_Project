import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def delay_heatmap(data_dir):
    '''
    This file creates the heatmap for total time of delays per month for each airline.
    Plot the heatmap from the delay_heatmap.csv created by the data extraction function.
    :param file:
    :return:
    '''
    assert isinstance(data_dir, str)
    df1_transposed = pd.read_csv(data_dir, index_col=0)
    print(df1_transposed)
    plt.rcParams['font.size'] = 20
    fig = plt.figure(figsize=(20, 10))
    sns.heatmap(df1_transposed, linecolor="w", linewidths=1, cmap="Reds", annot_kws={'size': 10}, )
    plt.show()

def main():
    file = 'delay_vs_airline_in2018.csv'
    delay_heatmap(file)

if __name__ == '__main__':
    main()
