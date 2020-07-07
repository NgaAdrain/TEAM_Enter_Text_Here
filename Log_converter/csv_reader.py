import csv
import pandas as pd
import os, sys
import matplotlib as mpl
import matplotlib.pyplot as plt

TARGET_LOCATION = r'.\csv_data\\'
OUT_LOCATION = r'.\csv_data_labeled\\'

TARGET_FILE = [file for file in os.listdir(TARGET_LOCATION) if file.endswith('.csv')]
"""
f = open('test.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
  print(line)
f.close()
"""
for fname in TARGET_FILE:
    print(TARGET_LOCATION + fname + " DONE")

    data_file = pd.read_csv(TARGET_LOCATION + fname, encoding='utf-8')

    data_file.drop(['Odometer','Gear(dashboard)','Avg_fuel_consumption','Clutch'],axis='columns', inplace=True)
    data_file.drop(['Fuel_level','Coordinate(location)_x','Coordinate(location)_y','Coordinate(location)_z'],axis='columns',inplace=True)
    data_file.drop(['Acceleration_x','Acceleration_y', 'Acceleration_z'],axis='columns',inplace=True)
    data_file.drop(['Rotation_angle_x','Rotation_angle_y', 'Rotation_angle_z'],axis='columns',inplace=True)
    data_file = data_file.rename(columns=({'Steering_wheel_x':'Steering_wheel_x'}))
    data_file['Label'] = 0

    out_name = fname[:-4] + '_labeled.csv'
    out_file = os.path.join(OUT_LOCATION, out_name)
    data_file.to_csv(out_file)
    #print(data_file.columns)