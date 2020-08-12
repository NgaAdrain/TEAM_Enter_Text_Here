import csv
import os, sys
import datetime


TARGET_LOCATION = r'.\csv_data'
OUT_LOCATION = r'.\csv_data'
TARGET_FILE = [file for file in os.listdir(TARGET_LOCATION) if file.endswith('.csv')]


def save(fname, fpath):
    file = open(fpath, 'r')
    reader = csv.reader(file)
    out_name = fname[:-4] + '_new.csv'
    out_file = os.path.join(OUT_LOCATION, out_name)
    fout = open(out_file, 'w', encoding='utf-8', newline='')
    wr = csv.writer(fout)
    cnt = 0
    is_start = True
    for line in reader:
        if is_start:
            wr.writerow(line)
            is_start = False
        else:
            #output = [(line[0]),(line[1]),(line[2]),(float(line[3]) * -1),(line[4]),(line[5]),(line[6]),(line[7]),(line[8]),(line[9]),(line[10])]
            #print(float(line[3]) * -1, output[3])
            line[3] = float(line[3]) * -1
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
