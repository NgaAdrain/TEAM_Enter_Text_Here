import csv
import os, sys
import datetime
from datetime import timedelta
from loader.ets2data import Ets2Data
from loader import Simlog_pb2

TARGET_LOCATION = r'.\log_data'
OUT_LOCATION = r'.\csv_data'

# TARGET_FILE = (
#     r'20181129_150355.dat',
#     r'o_20181129_150355.dat'
# )
TARGET_FILE = [file for file in os.listdir(TARGET_LOCATION) if file.endswith('.dat')]

DATA_TYPE = 'Timestamp,Velocity,accel_X,accel_Z,Steering_wheel_x,Accelerator,Brake,Winker(left),Winker(right),Label,Timecheck'

#CSV 데이터 열
TIMESTAMP = 0
VELOCITY = 1
ACCELX = 2
ACCELZ = 3
STEERING = 4
ACCEL = 5
BRAKE = 6
W_LEFT = 7
W_RIGHT = 8
TIMECHECK = 9

def save(fname, data, index):
    out_name = fname[:-4] + '.csv'
    out_file = os.path.join(OUT_LOCATION, out_name)
    fout = open(out_file, 'w', encoding='utf-8', newline='')
    wr = csv.writer(fout)
    cnt1 = 0
    cnt2 = 0
    prev_time = 0
    start_time = 0
    time_cnt = 0
    label = 0
    angle_limit = 7

    # list name
    element_type = str(DATA_TYPE).split(',')
    wr.writerow(element_type)

    # data input

    for element in data:
        dlist = str(element).split(',')
        dlist[6] = round(float(dlist[6]), 0)
        """
        del dlist[21] #winker right
        del dlist[20] #winker left
        """
        del dlist[19] #clutch
        """
        del dlist[18] #brake
        del dlist[17] #accelerator
        del dlist[16] #steering x #나중에 -1 추가 예정
        """
        del dlist[15] #z
        del dlist[14] #y
        del dlist[13] #rotation x
        del dlist[12] #z
        del dlist[11] #y
        del dlist[10] #coordinate x
        """
        del dlist[9] #z
        """
        del dlist[8] #y
        """
        del dlist[7] #acceleration x
        del dlist[6] #velocity
        """
        del dlist[5] #avg_fuel_consumption
        del dlist[4] #fuel_level
        del dlist[3] #rpm
        del dlist[2] #gear
        del dlist[1] #odometer

        dlist[STEERING] = round(float(dlist[STEERING]) * 450, 0)
        dlist[ACCEL] = round(float(dlist[ACCEL]) * 100, 0) #accel
        dlist[BRAKE] = round(float(dlist[BRAKE]) * 100, 0) #brake
        dlist[ACCELX] = round(float(dlist[ACCELX]), 6)
        dlist[ACCELZ] = round(float(dlist[ACCELZ]), 6)

        dlist[-1] = 0

        #기초 Labeling
        if float(dlist[W_LEFT]) == 1:
            dlist[-1] = 3
            cnt1 = 10
        elif float(dlist[W_LEFT]) == 0 and 30 > cnt1 >= 10:
            dlist[-1] = 3
            cnt1 += 1
        elif float(dlist[W_RIGHT]) == 1:
            dlist[-1] = 4
            cnt1 = 40
        elif float(dlist[W_RIGHT]) == 0 and 60 > cnt1 >= 40:
            dlist[-1] = 4
            cnt1 += 1
        elif cnt1 == 30 or cnt1 == 60:
            cnt1 = 0
        elif float(dlist[STEERING]) > angle_limit and float(dlist[VELOCITY]) != 0:
            dlist[-1] = 1
            cnt1 = 0
        elif float(dlist[STEERING]) < -1 * angle_limit and float(dlist[VELOCITY]) != 0:
            dlist[-1] = 2
            cnt1 = 0
        if float(dlist[VELOCITY]) == 0:
            dlist[-1] = 7

        #dlist[4] = round(float(dlist[4]),4)

        #Timecheck 추가
        prev_time = dlist[TIMESTAMP][0:4] + "-" + dlist[TIMESTAMP][4:6] + "-" + dlist[TIMESTAMP][6:8] + " " + dlist[TIMESTAMP][9:11] +\
                    ":" + dlist[TIMESTAMP][11:13] + ":" + dlist[TIMESTAMP][13:15]
        if time_cnt == 0:
            start_time = datetime.datetime.strptime(prev_time,'%Y-%m-%d %H:%M:%S')
            time_cnt += 1
        delta_time = datetime.datetime.strptime(prev_time,'%Y-%m-%d %H:%M:%S') - start_time
        dlist.append(delta_time)

        wr.writerow(dlist)
        index += 1
    fout.close()


def read(fpath):
    with open(fpath, 'rb') as fin:
        readData = fin.read()
        log.ParseFromString(readData)
        for info in log.info:
            yield Ets2Data(info)


if __name__ == '__main__':
    log = Simlog_pb2.Simlog()
    index = 0
    for fname in TARGET_FILE:
        curr_file = os.path.join(TARGET_LOCATION, fname)
        data = read(curr_file)
        save(fname, data, index)
