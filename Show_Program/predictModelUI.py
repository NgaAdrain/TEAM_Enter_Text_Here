#import csv
import cv2
import sys, os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


from keras.models import load_model

from loader.ets2data import Ets2Data
from loader import Simlog_pb2
print(keras.__version__)
VIDEO_FILE_LOCATION =  os.getcwd()
VIDEO_DIR_LOCATION = os.getcwd()
CSV_FILE_LOCATION = os.getcwd()
CSV_DIR_LOCATION = os.getcwd()

state_list = ["직진", "좌커브", "우커브", "좌회전", "우회전", "좌차선", "우차선", "정지"]
WINDOW_SIZE = 48
issim = 0

class ViewerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.defUIsetting()



    def defUIsetting(self):
        self.setGeometry(0,0,600,300)

        predictFont = QtGui.QFont()
        predictFont.setPointSize(20)

        percentFont = QtGui.QFont()
        percentFont.setPointSize(20)

        systemFont = QtGui.QFont()
        systemFont.setPointSize(10)

        labelFont =  QtGui.QFont()
        labelFont.setPointSize(20)

        self.csvFileList = QListView(self)
        self.videoLocButton = QPushButton("\nVideo Location\n")
        self.csvLocButton = QPushButton("\nCSV File Location\n")
        self.runButton = QPushButton("\nrun\n")
        self.result = QLabel("<b>predict data<b>")
        self.resultLabel = QLabel("No Data")
        self.resultLabel.setFont(predictFont)
        self.real = QLabel("<b>real data<b>")
        self.realLabel = QLabel("No Data")
        self.realLabel.setFont(labelFont)
        self.percent = QLabel("<b>percent<b>")
        self.percentLable = QLabel("No Data")
        self.percentLable.setFont(percentFont)
        self.system = QLabel("<b>System Message<b>")
        self.stateMsgLabel = QLabel("SysMsg")

        predict_layout = QGridLayout(self)

        predict_layout.addWidget(self.csvFileList,0,0,4,3)
        predict_layout.addWidget(self.videoLocButton,0,3)
        predict_layout.addWidget(self.csvLocButton,1,3)
        predict_layout.addWidget(self.runButton,2,3)
        predict_layout.addWidget(self.percentLable,5,3)
        predict_layout.addWidget(self.percent,4,3)
        predict_layout.addWidget(self.resultLabel,5,2)
        predict_layout.addWidget(self.result,4,2)
        predict_layout.addWidget(self.realLabel,5,1)
        predict_layout.addWidget(self.real,4,1)
        predict_layout.addWidget(self.stateMsgLabel,5,0)
        predict_layout.addWidget(self.system,4,0)

        self.csvBox = QFileSystemModel()
        self.csvBox.setFilter(QDir.NoDotAndDotDot | QDir.Files)

        self.csvFileList.setModel(self.csvBox)
        self.csvFileList.setRootIndex(self.csvBox.index(CSV_FILE_LOCATION))
        self.csvFileList.clicked.connect(self.list_clicked)

        self.videoLocButton.clicked.connect(self.video_clicked)
        self.csvLocButton.clicked.connect(self.csv_clicked)
        self.runButton.clicked.connect(self.show_image)
        self.runButton.setDisabled(True)


        self.setLayout(predict_layout)

    def list_clicked(self,index):
        global CSV_FILE_LOCATION, VIDEO_FILE_LOCATION
        for ix in self.csvFileList.selectedIndexes():
            CSV_FILE_LOCATION = os.path.join(CSV_DIR_LOCATION, ix.data())
            if (CSV_FILE_LOCATION.endswith('.csv')):
                video_name = ix.data()[:-4] + '.mp4'
                VIDEO_FILE_LOCATION = VIDEO_DIR_LOCATION + '/' + video_name
                if os.path.isfile(os.path.abspath(VIDEO_FILE_LOCATION)):
                    self.runButton.setEnabled(True)
                    self.stateMsgLabel.setText("File Matched")
                else:
                    self.stateMsgLabel.setText("File Not Exist")
                    self.runButton.setDisabled(True)
            else:
                self.stateMsgLabel.setText("File is Not CSV File")
                self.runButton.setDisabled(True)


    def video_clicked(self):
        global VIDEO_DIR_LOCATION
        VIDEO_DIR_LOCATION = QFileDialog.getExistingDirectory()
        print(VIDEO_DIR_LOCATION)

    def csv_clicked(self):
        global CSV_DIR_LOCATION
        CSV_DIR_LOCATION = os.path.abspath(QFileDialog.getExistingDirectory())
        self.csvFileList.setRootIndex(self.csvBox.setRootPath(CSV_DIR_LOCATION))
        print(CSV_DIR_LOCATION)


    def show_image(self):
        pop_data = pd.read_csv(CSV_FILE_LOCATION, encoding='utf-8')
        label_pd = pop_data.pop('Label')
        label_list = []
        for label in label_pd:
            label_list.append(label)
        predicted_list = dataPredict(pop_data)
        label_list = label_list[WINDOW_SIZE - 1:-1]
        if(len(predicted_list) == len(label_list)):
            accuracy = accuracycheck(predicted_list,label_list)
            accuracy = (round(accuracy,3) * 100)
            self.percentLable.setText(str(accuracy) + '%')
        else: self.stateMsgLabel.setText("data low not same")
        video = cv2.VideoCapture(VIDEO_FILE_LOCATION)
        print(video.get(cv2.CAP_PROP_FRAME_COUNT))
        video_skip = 0
        label_index = 0
        dFrame_data = WINDOW_SIZE * 3
        while (video.isOpened()):
            if (video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT)):
                video.release()
                cv2.destroyAllWindows()
                break
            ret, frame = video.read()
            if issim : rframe = cv2.resize(frame, dsize=(1660, 313), interpolation=cv2.INTER_AREA)
            else : rframe = cv2.resize(frame, dsize=(640, 480), interpolation=cv2.INTER_AREA)
            if (video_skip < dFrame_data):
                video_skip = video_skip + 1
                continue
            cv2.imshow("video",rframe)
            if ret:
                if ((label_index % 3 == 0)) :
                    state_index = int(label_list[int(label_index/3)])
                    self.realLabel.setText(state_list[state_index])
                    state_index = int(predicted_list[int(label_index/3)])
                    self.resultLabel.setText(state_list[state_index])

                label_index = label_index + 1
                if cv2.waitKey(15) & 0xFF == ord('q'):
                    video.release()
                    cv2.destroyAllWindows()
                    break

def accuracycheck(list1, list2):
    accuracy = 0
    for check in range(0, len(list1), 1):
        if list1[check] == list2[check]: accuracy = accuracy + 1
    accuracy = accuracy / len(list2)
    return accuracy



def read(fpath):
    with open(fpath, 'rb') as fin:
        readData = fin.read()
        log.ParseFromString(readData)
        for info in log.info:
            yield Ets2Data(info)

def dataPredict(data_file):
    global  issim
    if(data_file.columns[0] == "Timestamp"):
        print("simulation data")
        issim = 1
        data_file_time = data_file.pop('Timestamp')
        data_file.drop(['Winker(left)','Winker(right)','Timecheck'],axis = 'columns',inplace = True)
    else: issim = 0
    real_array = np.delete(data_file.values,-1,0).astype(np.float)

    if issim:
        real_array = range_limitation(real_array)
        reg = [1, 4, 2, 1, 1, 1]
        reg = np.array(reg)
        real_array = real_array / reg

    real_dataset_data = []
    for i in range(WINDOW_SIZE, real_array.shape[0] + 1, 1):
      real_dataset_data.append(real_array[i-WINDOW_SIZE:i])
    re_data = np.array(real_dataset_data)
    print(re_data.shape)
    re_c_data = re_data.reshape(-1,6,WINDOW_SIZE,1)

    cnn_model_main = load_model('./Sim2Real_Model_CNN_GAP_Final.h5')
    cnn_model_sub = load_model('./Sim2Real_Model_CNN_FLATTEN_Final.h5')
    #loaded_model_predictions = loaded_model.predict(re_c_data)
    cnn_test_predictions_1 = cnn_model_main.predict(re_c_data)
    cnn_test_predictions_2 = cnn_model_sub.predict(re_c_data)
    predicted_list = model_prediction_merge(cnn_test_predictions_1,cnn_test_predictions_2)
    print(len(predicted_list))
    return predicted_list
    #for pCount in re_c_data:
    #    index_data = np.argmax(loaded_model_predictions[input_count])
    #    predicted_list.append(index_data)
    #    input_count = input_count + 1

def model_prediction_merge(prediction_1,prediction_2):
  count = 0
  cnn_prediction = []
  for main_pred in prediction_1:
    if 0 < np.argmax(prediction_2[count]) < 5:
        cnn_prediction.append(np.argmax(prediction_2[count]))
    else:
        cnn_prediction.append(np.argmax(main_pred))
    count = count + 1
  #cnn_prediction = np.array(cnn_prediction)
  return cnn_prediction

def range_limitation(array):
  VELOCITY = 0
  ACCEL_X = 1
  ROT_Z = 2
  STEERING = 3
  ACCEL = 4
  BRAKE = 5
  VELOCITY_MAX = 120
  ACCEL_X_MAX =  2.0
  ACCEL_X_MIN = -2.0
  ROT_Z_MAX = 45
  ROT_Z_MIN = -45
  STEERING_MAX = 270
  STEERING_MIN = -270
  ACCEL_MAX = 80
  BRAKE_MAX = 50
  #length = int(len(array)/25)
  for i in range(len(array)):
    array[i][VELOCITY] = round(array[i][VELOCITY],0)
    if(array[i][VELOCITY]>=VELOCITY_MAX):    #MAX
      array[i][VELOCITY] = VELOCITY_MAX
    else:
      continue
  for i in range(len(array)):
    if(array[i][ACCEL_X]>=ACCEL_X_MAX):     #MAX
      array[i][ACCEL_X] = ACCEL_X_MAX
    elif(array[i][ACCEL_X]<=ACCEL_X_MIN):
      array[i][ACCEL_X] = ACCEL_X_MIN
    else:
      continue
  for i in range(len(array)):
    if(array[i][ROT_Z]>=ROT_Z_MAX):       #MAX
      array[i][ROT_Z] = ROT_Z_MAX
    elif(array[i][ROT_Z]<=ROT_Z_MIN):     #MIN
      array[i][ROT_Z] = ROT_Z_MIN
    else:
      continue
  for i in range(len(array)):
    if(array[i][STEERING]>=STEERING_MAX):    #MAX
      array[i][STEERING] = STEERING_MAX
    elif(array[i][STEERING]<= STEERING_MIN): #MIN
      array[i][STEERING] = STEERING_MIN
    else:
      continue
  for i in range(len(array)):
    if(array[i][ACCEL]>=ACCEL_MAX):        #MAX
      array[i][ACCEL] = ACCEL_MAX
    else:
      continue
  for i in range(len(array)):
    if(array[i][BRAKE]>=BRAKE_MAX):        #MAX
      array[i][BRAKE] = BRAKE_MAX
    else:
      continue
  return array

if __name__ == "__main__":
    log = Simlog_pb2.Simlog()
    app = QtWidgets.QApplication(sys.argv)
    window = ViewerUI()
    window.show()
    sys.exit(app.exec_())