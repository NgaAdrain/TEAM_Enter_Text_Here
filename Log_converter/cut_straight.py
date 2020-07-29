import csv
import os, sys
import datetime
from loader.ets2data import Ets2Data
from loader import Simlog_pb2

TARGET_LOCATION = r'.\csv_data'
OUT_LOCATION = r'.\csv_data\10Hz'
TARGET_FILE = [file for file in os.listdir(TARGET_LOCATION) if file.endswith('.csv')]

# CSV 데이터 열
TIMESTAMP = 0
VELOCITY = 1
ACCELX = 2
#ACCELZ = 3
STEERING = 3
ACCEL = 4
BRAKE = 5
W_LEFT = 6
W_RIGHT = 7
TIMECHECK = 8
LABEL = 9




def save(fname, fpath):
    file = open(fpath, 'r')
    reader = csv.reader(file)
    out_name = fname[:-4] + '_cut.csv'
    out_file = os.path.join(OUT_LOCATION, out_name)
    fout = open(out_file, 'w', encoding='utf-8', newline='')
    wr = csv.writer(fout)
    cnt = 0
    is_start = True
    for line in reader:
        if is_start:
            wr.writerow(line)
            is_start = False
        elif int(line[-2]) == 0:
            if cnt == 0:
                wr.writerow(line)
                cnt += 1
            elif cnt < 1:
                cnt += 1
            else:
                cnt = 0
        else:
            wr.writerow(line)
    fout.close()


def read(fpath):
    file = open(fpath,'r')
    reader = csv.reader(file)
    for line in reader:
        print(line)


if __name__ == '__main__':
    index = 0
    for fname in TARGET_FILE:
        curr_file = os.path.join(TARGET_LOCATION, fname)
        save(fname, curr_file)
