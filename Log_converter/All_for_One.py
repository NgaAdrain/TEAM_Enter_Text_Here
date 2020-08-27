import csv
import os, sys

TARGET_LOCATION = r'.\csv_data\10Hz'
OUT_LOCATION = r'.\csv_data\10Hz\combined'
TARGET_FILE = [file for file in os.listdir(TARGET_LOCATION) if file.endswith('.csv')]
DATA_TYPE = 'Timestamp,Velocity,Accel_X,Rotate_Z,Steering_wheel_x,' \
            'Accelerator,Brake,Winker(left),Winker(right),Label,Timecheck'


def save(fname, fpath,wr):
    file = open(fpath, 'r')
    is_start = True
    reader = csv.reader(file)
    for line in reader:
        if not is_start:
            wr.writerow(line)
        else:
            is_start = False


if __name__ == '__main__':
    out_name = 'ALL_in_One.csv'
    out_file = os.path.join(OUT_LOCATION, out_name)
    fout = open(out_file, 'w', encoding='utf-8', newline='')
    wr = csv.writer(fout)
    element_type = str(DATA_TYPE).split(',')
    wr.writerow(element_type)
    index = 0
    for fname in TARGET_FILE:
        curr_file = os.path.join(TARGET_LOCATION, fname)
        save(fname, curr_file, wr)
