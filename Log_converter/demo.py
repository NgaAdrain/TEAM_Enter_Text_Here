import csv
import os, sys
import datetime
from datetime import timedelta
#
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
        """
        del dlist[0] #timestamp
        """
        """
        if float(dlist[8]) == 1:
            dlist[-1] = 1
            cnt1 = 10
        elif float(dlist[8]) == 0 and 30 > cnt1 >= 10:
            dlist[-1] = 1
            cnt1 += 1
        elif float(dlist[9]) == 1:
            dlist[-1] = 2
            cnt1 = 40
        elif float(dlist[9]) == 0 and 60 > cnt1 >= 40:
            dlist[-1] = 2
            cnt1 += 1
        elif cnt1 == 30 or cnt1 == 60:
            dlist[-1] = 100
            cnt1 = 0
        else:
            dlist[-1] = 0
            cnt1 = 0
        """


        dlist[5] = round(float(dlist[5]) * 450, 0)
        dlist[6] = float(dlist[6]) * 100 #accel
        dlist[7] = float(dlist[7]) * 100 #brake
        dlist[2] = round(float(dlist[2]), 6)
        dlist[3] = round(float(dlist[3]), 6)
        dlist[4] = round(float(dlist[4]), 6)
        dlist[-1] = 0
        if float(dlist[8]) == 1:
            dlist[-1] = 3
            cnt1 = 10
        elif float(dlist[8]) == 0 and 30 > cnt1 >= 10:
            dlist[-1] = 3
            cnt1 += 1
        elif float(dlist[9]) == 1:
            dlist[-1] = 4
            cnt1 = 40
        elif float(dlist[9]) == 0 and 60 > cnt1 >= 40:
            dlist[-1] = 4
            cnt1 += 1
        elif cnt1 == 30 or cnt1 == 60:
            cnt1 = 0
        elif float(dlist[5]) > angle_limit:
            dlist[-1] = 1
            cnt1 = 0
        elif float(dlist[5]) < -1 * angle_limit:
            dlist[-1] = 2
            cnt1 = 0
        if float(dlist[1]) == 0:
            dlist[-1] = 7

        """
        if cnt1 == 0:
            if float(dlist[5]) > angle_limit:
                label = 1
                cnt1 = 11
                if float(dlist[5]) > left_most:
                    left_most = float(dlist[5])
            elif float(dlist[5]) < -1 * angle_limit:
                label = 2
                cnt1 = 21
                if float(dlist[5]) < right_most:
                    right_most = float(dlist[5])
            dlist[-1] = label
        if cnt1 == 11:
            if float(dlist[5]) > angle_limit:
                label = 1
                if float(dlist[5]) > left_most:
                    left_most = float(dlist[5])
            else:
                cnt1 = 12
            dlist[-1] = label
        if cnt1 == 12:
            cnt2 += 1
            label = 1
            if float(dlist[5]) > angle_limit:
                cnt1 = 11
                cnt2 = 0
            elif float(dlist[5]) < -1 * angle_limit:
                cnt1 = 13
                cnt2 = 0
            if cnt2 > 30:
                label = 0
                cnt1 = 0
                cnt2 = 0
                left_most = 0
                right_most = 0
            dlist[-1] = label
        if cnt1 == 13:
            label = 1
            if float(dlist[5]) < -1 * angle_limit:
                if float(dlist[5]) < right_most:
                    right_most = float(dlist[5])
            else:
                cnt1 = 14
            dlist[-1] = label
        if cnt1 == 14:
            if right_most * (-1) > 0.5 * left_most:
                dlist[-1] = 100
            label = 0
            cnt1 = 0
            left_most = 0
            right_most = 0
        if cnt1 == 21:
            if float(dlist[5]) < -1 * angle_limit:
                label = 2
                if float(dlist[5]) < right_most:
                    right_most = float(dlist[5])
            else:
                cnt1 = 22
            dlist[-1] = label
        if cnt1 == 22:
            cnt2 += 1
            label = 2
            if float(dlist[5]) < -1 * angle_limit:
                cnt1 = 21
                cnt2 = 0
            elif float(dlist[5]) > angle_limit:
                cnt1 = 23
                cnt2 = 0
            if cnt2 > 30:
                label = 0
                cnt1 = 0
                cnt2 = 0
                left_most = 0
                right_most = 0
            dlist[-1] = label
        if cnt1 == 23:
            label = 2
            if float(dlist[5]) > angle_limit:
                if float(dlist[5]) > left_most:
                    left_most = float(dlist[5])
            else:
                cnt1 = 24
            dlist[-1] = label
        if cnt1 == 24:
            if left_most > (-0.5) * right_most:
                dlist[-1] = 200
            label = 0
            cnt1 = 0
            left_most = 0
            right_most = 0
        """

        """
        if float(dlist[6])>0:
            if float(dlist[7])>0:
                dlist.append(3)
            else:
                dlist.append(1)
        elif float(dlist[7])>0:
            dlist.append(2)
        else:
            dlist.append(0)
        """
        dlist[5] = round(float(dlist[5]),4)

        prev_time = dlist[0][0:4] + "-" + dlist[0][4:6] + "-" + dlist[0][6:8] + " " + dlist[0][9:11] + ":" + dlist[0][11:13] + ":" + dlist[0][13:15]
        if time_cnt == 0:
            start_time = datetime.datetime.strptime(prev_time,'%Y-%m-%d %H:%M:%S')
            time_cnt += 1
        delta_time = datetime.datetime.strptime(prev_time,'%Y-%m-%d %H:%M:%S') - start_time
        #delta_time = timedelta(seconds = delta_time.seconds, microseconds = delta_time.microseconds)

        dlist.append(delta_time)
        #dlist.append(float(dlist[0][9:15]))

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
