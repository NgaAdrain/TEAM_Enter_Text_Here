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

DATA_TYPE = ' Timestamp,Odometer,Gear(dashboard),RPM,\
Fuel_level,Avg_fuel_consumption,Velocity,\
Acceleration_x,Acceleration_y,Acceleration_z,\
Coordinate(location)_x,Coordinate(location)_y,Coordinate(location)_z,\
Rotation_angle_x,Rotation_angle_y,Rotation_angle_z,\
Steering_wheel_x,Accelerator,Brake,Clutch,Winker(left),Winker(right)'

def save(fname, data):
    out_name = fname[:-4] + '.csv'
    out_file = os.path.join(OUT_LOCATION, out_name)
    fout = open(out_file, 'w', encoding='utf-8', newline='')
    wr = csv.writer(fout)
    
    # list name 
    element_type = str(DATA_TYPE).split(',')
    wr.writerow(element_type)

    # data input
    for element in data:
        dlist = str(element).split(',')
        wr.writerow(dlist)
    fout.close()


def read(fpath):
    with open(fpath, 'rb') as fin:
        readData = fin.read()
        log.ParseFromString(readData)
        for info in log.info:
            yield Ets2Data(info)


if __name__ == '__main__':
    log = Simlog_pb2.Simlog()
    for fname in TARGET_FILE:
        curr_file = os.path.join(TARGET_LOCATION, fname)
        data = read(curr_file)
        save(fname, data)
