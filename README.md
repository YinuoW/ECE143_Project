# ECE143 Project Group 19

## Project: Analysis of Flight Delay and Cancellation

Group members:

|Name|Email|
|---|---|
|Lu, Heqian|h7lu@ucsd.edu|
|Leong, Samantha|s5leong@ucsd.edu|
|Zhao, Shuheng|shzhao@ucsd.edu|
|Wang, Yinuo|yiw010@ucsd.edu|

### Overview 

This project aims to provide analysis of flight delays and cancellations for our top 10 airlines in 2018.

These airlines are ranked according to the volumes of flights, and the top 10 airlines with the most number of flights are chosen to do our analysis. 

These analysis are conducted to provide us with the understanding of the most appropriate time of the day and year to travel, rate of delays and cancellations, as well as reasons for delay.

These analysis are then compiled to form a scoring system so the user can decide to which airline to take based on
arrival delays, departure delays, and cancellations.

Terminology and definitions:

`arrival delays` the flight arrives at the destination location later than expected.

`departure delays` the flight leaves the departed location later than expected.

`cancellations` the flight is cancelled. 


## 1. File Structure

#### `raw_data` folder

This folder contains the raw data of our main dataset. 
There are 12 files in it, each represents the data for one single month in 2018. 
Use `merge.py` to generate our final dataset which contains all the data in year 2018.

#### `data` folder

This is the folder contains our datasets.

#### `src` folder

This folder contains all the source code files making the visualization.

##### `utils.py` file

This is the file containing all the reusable modules.

##### `Demo` folder

This folder contains the **jupyter notebook for the demo**.

##### Other folders

The folder names are summary of the relevant problems we concern.

There are `.py` files in each folder. 
- The one ending with `extraction` is the file used to extract the data from our dataset and save it to `.csv` files within the folder.
- The others without `extraction` are used to generate corresponding plots directly from the `.csv` files.

## 2. How to Run the Code (This is the version for runing in terminal, you can also clone this repo and run it in IDE directly)

#### Step1: get the dataset `2018.csv`

Since our main dataset is too large to upload, you will need to generate it from raw data.
To get the `2018.csv`, run the `merge.py` first.

> location: root directory

> command: `$python3 merge.py` (`cd` in the root directory first)


#### Step2: select one folder in the `src` and get the corresponding extracted data from the dataset

In some folders, there are source files ending with `extraction`.
Run these files first to get the extracted `.csv` files to make the plots.

Take the folder `airline_stats_triangle` for example:

> location: "src/airline_stats_triangle"

> command: 
- `$cd src/airline_stats_triangle`
- `$python3 airline_stats_triangle_plot_data_extraction.py`

#### Step3: genetate plots

Run the files without `extraction` to generate the plots.

**Note: `cd` into the lowest folders first!**

Take the folder `airline_stats_triangle` for example:

> location: "src/airline_stats_triangle"

> command: 
- `$cd src/airline_stats_triangle`
- `$python3 airline_stats_triangle_plot.py`

In some folders, there is no file ending with `extraction`.
Then run the `.py` files directly.

Take the folder `cancellation` for example:

> location: "src/cancellation"

> command:
- `$cd src/cancellation`
- `$python3 total_cancellation.py`

## 3. Third-party modules

pandas

numpy

matplotlib (matplotlib.pyplot)

plotly.graph_objs

plotly.offline

seaborn

datetime

## Appendix (files used to generate plots in our presentation)

We did a lot of visualization to dive into our problems, but only able to present part of it due to the time limit.

The followings are the files generating plots we used in our presentation:

src/airline_delay_distribution:
- AL_delay_distribution.py

src/airline_stas_triangle:
- airline_stats_triangle_plot_data_extraction.py
- airline_stats_triangle_plot.py

src/box_line_delay_vs_airline_in2018:
- box_line_delay_data_extraction.py
- box_line_delay_vs_airline_in2018.py

src/cancellation:
- cancellation_rate_colorbar.py
- cancellation/total_cancellation.py

src/delay_by_month:
- delay_by_month.py
- delay_heatmap.py
- delay_heatmap_extraction.py

src/delay_ontime_flights_number:
- delay_ontime_flights_number.py
- delay_ontime_flights_number_extraction.py

src/delay_rate:
- delay_rate.py
- delay_rate_data_extraction.py

src/delay_reason:
- reason_distribution_vs_airline.py
- reasons_piechart.py

src/flights_count_per_airline:
- count_flight_airline_colorbar.py

src/time_block_barh:
- time_block.py
- time_block_data_extraction.py
