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

def normalize(line):
#VELOCITY
    if float(line[VELOCITY]) >= 100:
        line[VELOCITY] = 31.75
    elif float(line[VELOCITY]) >= 50:
        line[VELOCITY] = round((float(line[VELOCITY]) - 50) / 50 * 31.75, 2)
    elif float(line[VELOCITY]) > 0:
        line[VELOCITY] = round((float(line[VELOCITY]) - 50) / 50 * 32, 2)
    else:
        line[VELOCITY] = -32
#ACCEL_X
    if float(line[ACCELX]) >= 0.6:
        line[ACCELX] = 31.75
    elif float(line[ACCELX]) >= 0:
        line[ACCELX] = round(float(line[ACCELX]) / 0.6 * 31.75, 2)
    elif float(line[ACCELX]) > -0.6:
        line[ACCELX] = round(float(line[ACCELX]) / 0.6 * 32, 2)
    else:
        line[ACCELX] = -32
#STEERING
    if float(line[STEERING]) >= 270:
        line[STEERING] = 31.75
    elif float(line[STEERING]) >= 0:
        line[STEERING] = round(float(line[STEERING]) / 270 * 31.75, 2)
    elif float(line[STEERING]) > -270:
        line[STEERING] = round(float(line[STEERING]) / 270 * 32, 2)
    else:
        line[STEERING] = -32
#ACCEL
    if float(line[ACCEL]) >= 70:
        line[ACCEL] = 31.75
    elif float(line[ACCEL]) >= 35:
        line[ACCEL] = round((float(line[ACCEL]) - 35) / 35 * 31.75, 2)
    elif float(line[ACCEL]) > 0:
        line[ACCEL] = round((float(line[ACCEL]) - 35) / 35 * 32, 2)
    else:
        line[ACCEL] = -32
#BRAKE
    if float(line[BRAKE]) >= 50:
        line[BRAKE] = 31.75
    elif float(line[BRAKE]) >= 25:
        line[BRAKE] = round((float(line[BRAKE])-25) / 25 * 31.75, 2)
    elif float(line[BRAKE]) > 0:
        line[BRAKE] = round((float(line[BRAKE])-25) / 25 * 32, 2)
    else:
        line[BRAKE] = -32


def save(fname, fpath):
    file = open(fpath, 'r')
    reader = csv.reader(file)
    out_name = fname[:-4] + '_10Hz_normalized.csv'
    out_file = os.path.join(OUT_LOCATION, out_name)
    fout = open(out_file, 'w', encoding='utf-8', newline='')
    wr = csv.writer(fout)
    cnt = 0
    is_start = True
    for line in reader:
        if is_start:
            wr.writerow(line)
            is_start = False
        elif cnt == 0:
            normalize(line)
            wr.writerow(line)
            cnt += 1
        elif cnt < 2:
            cnt += 1
        else:
            cnt = 0

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
