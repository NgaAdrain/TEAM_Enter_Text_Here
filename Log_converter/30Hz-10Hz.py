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

#정규화 용 변수
NOR_MAX = 31.75
NOR_MIN = -32
VELOCITY_MAX = 100
VELOCITY_MIN = 0
ACCEL_X_MAX = 0.6
ACCEL_X_MIN = -0.6
STEERING_MAX = 225
STEERING_MIN = -225
ACCEL_MAX = 70
ACCEL_MIN = 0
BRAKE_MAX = 50
BRAKE_MIN = 0


def normalize(line):
#VELOCITY
    if float(line[VELOCITY]) >= VELOCITY_MAX:
        line[VELOCITY] = NOR_MAX
    elif float(line[VELOCITY]) >= (VELOCITY_MAX/2):
        line[VELOCITY] = round((float(line[VELOCITY]) - 50) / 50 * NOR_MAX, 2)
    elif float(line[VELOCITY]) > VELOCITY_MIN:
        line[VELOCITY] = round((float(line[VELOCITY]) - 50) / 50 * 32, 2)
    else:
        line[VELOCITY] = NOR_MIN
#ACCEL_X
    if float(line[ACCELX]) >= ACCEL_X_MAX:
        line[ACCELX] = NOR_MAX
    elif float(line[ACCELX]) >= 0:
        line[ACCELX] = round(float(line[ACCELX]) / 0.6 * NOR_MAX, 2)
    elif float(line[ACCELX]) > ACCEL_X_MIN:
        line[ACCELX] = round(float(line[ACCELX]) / 0.6 * 32, 2)
    else:
        line[ACCELX] = NOR_MIN
#STEERING
    if float(line[STEERING]) >= STEERING_MAX:
        line[STEERING] = NOR_MAX
    elif float(line[STEERING]) >= 0:
        line[STEERING] = round(float(line[STEERING]) / 270 * NOR_MAX, 2)
    elif float(line[STEERING]) > STEERING_MIN:
        line[STEERING] = round(float(line[STEERING]) / 270 * 32, 2)
    else:
        line[STEERING] = NOR_MIN
#ACCEL
    if float(line[ACCEL]) >= ACCEL_MAX:
        line[ACCEL] = NOR_MAX
    elif float(line[ACCEL]) >= (ACCEL_MAX/2):
        line[ACCEL] = round((float(line[ACCEL]) - 35) / 35 * NOR_MAX, 2)
    elif float(line[ACCEL]) > ACCEL_MIN:
        line[ACCEL] = round((float(line[ACCEL]) - 35) / 35 * 32, 2)
    else:
        line[ACCEL] = NOR_MIN
#BRAKE
    if float(line[BRAKE]) >= BRAKE_MAX:
        line[BRAKE] = NOR_MAX
    elif float(line[BRAKE]) >= (BRAKE_MAX/2):
        line[BRAKE] = round((float(line[BRAKE])-25) / 25 * NOR_MAX, 2)
    elif float(line[BRAKE]) > BRAKE_MIN:
        line[BRAKE] = round((float(line[BRAKE])-25) / 25 * 32, 2)
    else:
        line[BRAKE] = NOR_MIN


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
