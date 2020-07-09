import csv
import sys, os
from PyQt5.QtWidgets import *

from loader.ets2data import Ets2Data
from loader import Simlog_pb2

#TARGET_LOCATION = r'\Users\cherr\Documents\GitHub\TEAM_Enter_Text_Here\Log_converter\log_data'
TARGET_LOCATION =  os.getcwd() + r'..\log_data'
#OUT_LOCATION = r'\Users\cherr\Documents\GitHub\TEAM_Enter_Text_Here\Log_converter\csv_data'
OUT_LOCATION = os.getcwd() + r'..\log_data'

TARGET_FILE = [file for file in os.listdir(TARGET_LOCATION) if file.endswith('.dat')]
DATA_TYPE = 'Timestamp,RPM,Velocity,Steering_wheel_x,Accelerator,Brake,Winker(left),Winker(right),Label'

def save(fname, data, index):
    out_name = fname[:-4] + '.csv'#means remove .dat and add .csv and save
    out_file = os.path.join(OUT_LOCATION, out_name)#write location and file name
    fout = open(out_file, 'w', encoding='utf-8', newline='')
    wr = csv.writer(fout)#write csv

    # list name
    element_type = str(DATA_TYPE).split(',')
    wr.writerow(element_type)#make column

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
        dlist[-1] = (float(dlist[-3]) * 1) + (float(dlist[-2])) * 2
        wr.writerow(dlist)
        index += 1
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
        self.convertState = QLabel()

        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.makeLocationButton)
        mainLayout.addWidget(self.outFileLocationButton)
        mainLayout.addWidget(self.convertButton)
        mainLayout.addWidget(self.openLocationButton)
        mainLayout.addWidget(self.dattext)
        mainLayout.addWidget(self.datLocation)
        mainLayout.addWidget(self.outtext)
        mainLayout.addWidget(self.outLocation)
        mainLayout.addWidget(self.convertState)
        self.dattext.setText("dat File Location")
        self.datLocation.setText(TARGET_LOCATION)
        self.outtext.setText("out File Location")
        self.outLocation.setText(OUT_LOCATION)
        self.convertState.setText("convert state")
        self.setLayout(mainLayout)

    def convertCSV(self):
        for fname in TARGET_FILE:
            #self.convertState.setText(fname)
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