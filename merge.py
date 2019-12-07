'''
This is used to generate '2018.csv' using raw data from Bureau Transposition Statistics.
'''
import os
import glob
import pandas as pd
os.chdir("./raw_data")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
#export to csv
combined_csv.to_csv("../data/2018.csv", index=False)
