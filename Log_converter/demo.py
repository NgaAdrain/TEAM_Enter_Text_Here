import csv
import os, sys
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

DATA_TYPE = 'Timestamp,RPM,Velocity,Steering_wheel_x,Accelerator,Brake,Winker(left),Winker(right),Label1,Label2'


def save(fname, data, index):
    out_name = fname[:-4] + '.csv'
    out_file = os.path.join(OUT_LOCATION, out_name)
    fout = open(out_file, 'w', encoding='utf-8', newline='')
    wr = csv.writer(fout)
    cnt1 = 0
    cnt2 = 0
    line_cnt = 0

    # list name
    element_type = str(DATA_TYPE).split(',')
    wr.writerow(element_type)

    # data input

    for element in data:
        dlist = str(element).split(',')
        del dlist[19]
        del dlist[15]
        del dlist[14]
        del dlist[13]
        del dlist[12]
        del dlist[11]
        del dlist[10]
        del dlist[9]
        del dlist[8]
        del dlist[7]
        del dlist[5]
        del dlist[4]
        del dlist[2]
        del dlist[1]

        if int(dlist[6]) == 1:
            dlist[-1] = 1
            cnt1 = 10
        elif int(dlist[6]) == 0 and 30 > cnt1 >= 10:
            dlist[-1] = 1
            cnt1 += 1
        elif int(dlist[7]) == 1:
            dlist[-1] = 2
            cnt1 = 10
        elif int(dlist[7]) == 0 and 30 > cnt1 >= 10:
            dlist[-1] = 2
            cnt1 += 1
        else:
            dlist[-1] = 0
            cnt1 = 0

        if float(dlist[4])>0:
            if float(dlist[5])>0:
                dlist.append(3)
            else:
                dlist.append(1)
        elif float(dlist[5])>0:
            dlist.append(2)
        else:
            dlist.append(0)

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

