import csv
import sys, os
from PyQt5.QtWidgets import *

from loader.ets2data import Ets2Data
from loader import Simlog_pb2

#TARGET_LOCATION = r'\Users\cherr\Documents\GitHub\TEAM_Enter_Text_Here\Log_converter\log_data'
TARGET_LOCATION =  os.getcwd()
#OUT_LOCATION = r'\Users\cherr\Documents\GitHub\TEAM_Enter_Text_Here\Log_converter\csv_data'
OUT_LOCATION = os.getcwd()

TARGET_FILE = [file for file in os.listdir(TARGET_LOCATION) if file.endswith('.dat')]
DATA_TYPE = 'Timestamp,Velocity,accel_X,accel_Y,accel_Z,Steering_wheel_x,Accelerator,Brake,Winker(left),Winker(right),Label1'

def save(fname, data, index):
    out_name = fname[:-4] + '.csv'
    out_file = os.path.join(OUT_LOCATION, out_name)
    fout = open(out_file, 'w', encoding='utf-8', newline='')
    wr = csv.writer(fout)
    cnt1 = 0
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
        del dlist[8] #y
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
        dlist[5] = round(float(dlist[5]) * 450, 0)
        dlist[6] = float(dlist[6]) * 100 #accel
        dlist[7] = float(dlist[7]) * 100 #brake
        dlist[2] = round(float(dlist[2]), 6)
        dlist[3] = round(float(dlist[3]), 6)
        dlist[4] = round(float(dlist[4]), 6)
        dlist[-1] = 0
        if float(dlist[1]) == 0:
            dlist[-1] = 5
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
        dlist[5] = round(float(dlist[5]),4)
        wr.writerow(dlist)
        index += 1
        print("check")
    fout.close()

def read(fpath):
    with open(fpath, 'rb') as fin:
        readData = fin.read()
        log.ParseFromString(readData)
        for info in log.info:
            yield Ets2Data(info)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(320, 240)
        #self.setAcceptDrops(True)
        self.setWindowTitle("CSV converter")
        self.convertButton = QPushButton("\nConvert\n")
        self.openLocationButton = QPushButton("Open CSV file directory")
        self.makeLocationButton = QPushButton("Set dat file location")
        self.outFileLocationButton = QPushButton("Set Out File location")
        self.convertButton.clicked.connect(self.convertCSV)
        self.openLocationButton.clicked.connect(self.openLocation)
        self.makeLocationButton.clicked.connect(self.makeLocation)
        self.outFileLocationButton.clicked.connect(self.outFileLocation)
        self.dattext = QLabel()
        self.datLocation = QLabel()
        self.outtext = QLabel()
        self.outLocation = QLabel()

        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.makeLocationButton)
        mainLayout.addWidget(self.outFileLocationButton)
        mainLayout.addWidget(self.convertButton)
        mainLayout.addWidget(self.openLocationButton)
        mainLayout.addWidget(self.dattext)
        mainLayout.addWidget(self.datLocation)
        mainLayout.addWidget(self.outtext)
        mainLayout.addWidget(self.outLocation)
        self.dattext.setText("dat File Location")
        self.datLocation.setText(TARGET_LOCATION)
        self.outtext.setText("out File Location")
        self.outLocation.setText(OUT_LOCATION)
        self.setLayout(mainLayout)

    def convertCSV(self):
        for fname in TARGET_FILE:
            print(TARGET_LOCATION)
            curr_file = os.path.join(TARGET_LOCATION, fname)
            data = read(curr_file)
            save(fname, data, index)

    def openLocation(self):
        path = OUT_LOCATION
        path = os.path.realpath(path)
        os.startfile(path)

    def makeLocation(self):
        global TARGET_LOCATION, TARGET_FILE
        TARGET_LOCATION = QFileDialog.getExistingDirectory(self)
        TARGET_FILE = [file for file in os.listdir(TARGET_LOCATION) if file.endswith('.dat')]
        self.datLocation.setText(TARGET_LOCATION)

    def outFileLocation(self):
        global OUT_LOCATION
        OUT_LOCATION = QFileDialog.getExistingDirectory(self)
        self.outLocation.setText(OUT_LOCATION)

#    def dragEnterEvent(self, event):
#        if event.mimeData().hasUrls():
#            event.accept()
#        else:
#            event.ignore()

#    def dropEvent(self, event):
#        global fileLocation
#        file = [u.toLocalFile() for u in event.mimeData().urls()]
#        fileLocation = file

if __name__ == "__main__":
    log = Simlog_pb2.Simlog()
    index = 0
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()
    sys.exit(app.exec_())