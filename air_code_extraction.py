# extract airports and airline ['Code', 'Description'] pairs
import os
import glob
import pandas as pd
import csv

# 2018.csv Info
# RangeIndex: 7213446 entries, 0 to 7213445
# Data columns (total 28 columns):
# FL_DATE                  object
# OP_CARRIER_AIRLINE_ID    int64   X
# OP_CARRIER               object
# ORIGIN_AIRPORT_ID        int64   X
# ORIGIN_AIRPORT_SEQ_ID    int64
# ORIGIN                   object
# ORIGIN_STATE_ABR         object
# DEST_AIRPORT_ID          int64
# DEST_AIRPORT_SEQ_ID      int64
# DEST                     object
# DEST_STATE_ABR           object
# DEP_DELAY                float64
# DEP_DEL15                float64
# DEP_DELAY_GROUP          float64
# DEP_TIME_BLK             object
# ARR_DELAY                float64
# ARR_DEL15                float64
# ARR_DELAY_GROUP          float64
# ARR_TIME_BLK             object
# CANCELLED                float64
# CANCELLATION_CODE        object
# DISTANCE                 float64
# CARRIER_DELAY            float64
# WEATHER_DELAY            float64
# NAS_DELAY                float64
# SECURITY_DELAY           float64
# LATE_AIRCRAFT_DELAY      float64
# Unnamed: 27              float64
# dtypes: float64(14), int64(5), object(9)

#data_dir = './data/Airline_Lookup.csv'
data_dir_2018 = './data/2018.csv'
data_dir = './data/Airport_Lookup.csv'
# df = pd.read_csv(data_dir)
# print(len(df.ORIGIN.unique()))
# 18 airlines
# airline_code = ['AA', '9E', 'DL', 'B6', 'EV', 'HA', 'MQ', 'OH', 'OO', 'NK', 'WN', 'YV', 'YX', 'AS', 'G4', 'UA', 'F9', 'VX']
# 358 airports
airport_code = []
csv_file = open(data_dir_2018)
readCSV = csv.reader(csv_file)
for row in readCSV:
    if row[5] not in airport_code:
        airport_code.append(row[5])
    if row[9] not in airport_code:
        airport_code.append(row[9])
print(len(airport_code))

csv_file2 = open(data_dir)
readCSV2 = csv.reader(csv_file2)
with open('./data/airport2018_lookup.csv', 'w') as csvfile_write:
    filewriter = csv.writer(csvfile_write)
    filewriter.writerow(['Code','Description'])
    for row in readCSV2:
        if row[0] in airport_code:
            filewriter.writerow(row)

csv_file.close()
csvfile_write.close()