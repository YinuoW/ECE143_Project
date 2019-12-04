# ECE143 Project Group 19

Group members:

|Name|Email|
|---|---|
|Lu, Heqian|h7lu@ucsd.edu|
|Leong, Samantha|s5leong@ucsd.edu|
|Zhao, Shuheng|shzhao@ucsd.edu|
|Wang, Yinuo|yiw010@ucsd.edu|


## 1. File Structure

#### `raw_data` folder

This folder contains the raw data of our main dataset. 
There are 12 files in it, each represents the data for one single month in 2018. 
Use `merge.py` to generate our final dataset which contains all the data in year 2018.

#### `data` folder

This is the folder contains our datasets.

#### Source code folders

For all the other folders except data folders, there are source code files making the visualization.
The folder names are summary of the relevant problems we concern.

There are `.py` files in each folder. 
- The one ending with `extraction` is the file used to extract the data from our dataset and save it to `.csv` files within the folder.
- The others without `extraction` are used to generate corresponding plots directly from the `.csv` files.

## 2. How to Run the Code

#### Step1: get the dataset `2018.csv`

Since our main dataset is too large to upload, you will need to generate it from raw data.
To get the `2018.csv`, run the `merge.py` first.

#### Step2: select one folder and get the corresponding extracted data from the dataset

In some folders, there are source files ending with `extraction`.
Run these files first to get the extracted `.csv` files to make the plots.

#### Step3: genetate plots

Run the files without `extraction` to generate the plots.

## 3. Third-party modules

pandas

numpy

matplotlib (matplotlib.pyplot)

plotly.graph_objs

plotly.offline

seaborn

datetime

