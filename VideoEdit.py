from pydoc import doc
from signal import signal
import sys
from xml.etree.ElementTree import tostring
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


import numpy as np
import ffmpeg
import subprocess
import cv2
import math
import os
from datetime import datetime

ui = uic.loadUiType("VideoEdit.ui")[0]


class MyWindow(QMainWindow, ui):

    def __init__(self):
        self.chosen_points = []
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Video Edit Tool")

        self.idx = 0
        self.dir = None
        self.entry = None
        self.filelist = None
        self.inputFile = None

        self.pb_import.clicked.connect(self.open)
        self.pb_codec.clicked.connect(self.codecEdit)
        self.pb_size.clicked.connect(self.sizeEdit)
        self.pb_time.clicked.connect(self.timeEdit)
        self.pb_frame.clicked.connect(self.addFrameNum)
        self.list_file.itemClicked.connect(self.fileInfo)
        self.list_file.itemEntered.connect(self.selectAuto)

        self.radio_1920.setChecked(True)
        self.radio_avc.setChecked(True)
        self.setAcceptDrops(True)

    def open(self):
        self.list_file.clear()

        if (self.dir == None):
            settings = QSettings()
            self.dir = ""
        else:
            self.dir = None
        file_names = QFileDialog.getOpenFileNames(self,
                                                  "Open Video File", self.dir, '"Videos (*.mp4)')
        self.filelist = list(file_names[0])

        for file in self.filelist:
            self.list_file.addItem(file)
        self.list_file.setCurrentRow(0)

        if self.filelist != []:
            self.fileInfo()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            l = []
            for url in event.mimeData().urls():
                self.list_file.insertItem(0, url.toLocalFile())
                # self.list_file.addItem(url.toLocalFile())
            self.list_file.setCurrentRow(0)
            self.fileInfo()
        else:
            event.ignore()

    def fileInfo(self):
        self.idx = self.list_file.row(self.list_file.currentItem())

        file = self.list_file.currentItem().text()
        self.inputFile = file

        vid = cv2.VideoCapture(file)
        wid = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        hei = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        codec = vid.get(cv2.CAP_PROP_FOURCC)
        len = vid.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = vid.get(cv2.CAP_PROP_FPS)
        time = len/fps

        self.lb_file.setText("File : " + str(file))
        self.lb_size.setText("Size : " + str(int(wid)) + " , " + str(int(hei)))
        self.lb_codec.setText("Codec :" + str(codec))
        self.lb_len.setText("Length : " + str(math.trunc(time)) + " s")

        self.cap = vid
        self.wid = wid
        self.fps = fps

    def codecEdit(self):
        self.lb_done.setText(" ")
        outfile = os.path.splitext(self.inputFile)[0]+str('_cod.mp4')
        if self.radio_avc.isChecked():
            subprocess.run("ffmpeg -i " + str(self.inputFile) +
                           " -c:v libx264 " + outfile)
        print("Process Done.")
        self.lb_done.setText("Process Done.")

    def newName(self, output):
        uniq = 1
        while os.path.exists(output):
            output = os.path.splitext(output)[0] + str("(%d).mp4") % (uniq)
            uniq += 1
        print(output)
        return output

    # def sizeEdit(self):
    #     outfile = ""
    #     fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    #     wid_new = 1920
    #     hei_new = 1080

    #     if self.radio_960.isChecked():
    #         wid_new = 960
    #         hei_new = 540
    #     elif self.radio_1280.isChecked():
    #         wid_new = 1280
    #         hei_new = 720
    #     elif self.radio_3840.isChecked():
    #         wid_new = 3840
    #         hei_new = 2160

    #     outfile = os.path.splitext(self.inputFile)[
    #         0]+str('_%d.mp4') % (wid_new)
    #     outfile = self.newName(outfile)
    #     out = cv2.VideoWriter(outfile, fourcc, self.fps, (wid_new, hei_new))

    #     while True:
    #         ret, frame = self.cap.read()
    #         if ret == True:
    #             if self.wid > wid_new:
    #                 frame_rsz = cv2.resize(
    #                     frame, (wid_new, hei_new), fx=0, fy=0, interpolation=cv2.INTER_LINEAR)
    #             else:
    #                 frame_rsz = cv2.resize(
    #                     frame, (wid_new, hei_new), fx=0, fy=0, interpolation=cv2.INTER_LINEAR)
    #             out.write(frame_rsz)
    #         else:
    #             break
    #     self.cap.release()
    #     out.release()
    #     cv2.destroyAllWindows()

    #     print("Process Done.")
    #     self.lb_done.setText("Process Done.")

    def sizeEdit(self):
        self.lb_done.setText(" ")

        if self.radio_960.isChecked():
            outfile = os.path.splitext(self.inputFile)[0]+str('_960.mp4')
            outfile = self.newName(outfile)
            subprocess.run("ffmpeg -i " + str(self.inputFile) +
                           " -vf scale=960x540 -c:v libx264 -preset slow -crf 16 -c:a copy " + outfile)
        if self.radio_1280.isChecked():
            outfile = os.path.splitext(self.inputFile)[0]+str('_1280.mp4')
            outfile = self.newName(outfile)
            subprocess.run("ffmpeg -i " + str(self.inputFile) +
                           " -vf scale=1280:720 -c:v libx264 -preset slow -crf 17 -c:a copy " + outfile)
        if self.radio_1920.isChecked():
            outfile = os.path.splitext(self.inputFile)[0]+str('_1920.mp4')
            outfile = self.newName(outfile)
            subprocess.run("ffmpeg -i " + str(self.inputFile) +
                           " -vf scale=1920x1080 " + outfile)
        if self.radio_3840.isChecked():
            outfile = os.path.splitext(self.inputFile)[0]+str('_3840.mp4')
            outfile = self.newName(outfile)
            subprocess.run("ffmpeg -i " + str(self.inputFile) +
                           " -vf scale=3840x2160 " + outfile)

        print("Process Done.")
        self.lb_done.setText("Process Done.")

    def timeEdit(self):
        self.lb_done.setText(" ")
        outfile = os.path.splitext(self.inputFile)[0]+str('_timeCut.mp4')
        outfile = self.newName(outfile)
        start = self.line_start.text()
        end = self.line_end.text()
        if (start != "" and end != ""):
            subprocess.run("ffmpeg -i " + str(self.inputFile) + " -ss " +
                           str(start) + " -to " + str(end) + " " + outfile)
        print("Process Done.")
        self.lb_done.setText("Process Done.")

    def addFrameNum(self):
        self.lb_done.setText(" ")
        outfile = os.path.splitext(self.inputFile)[0]+str('_frame.mp4')
        subprocess.run("ffmpeg -i " + str(self.inputFile) +
                       " -vf \"drawtext=fontfile=Arial.ttf: text='%{frame_num}': start_number=0: x=(w-tw)/2: y=(h-lh)/3: fontcolor=black: fontsize=40: box=1: boxcolor=white: boxborderw=5\" -c:a copy " + str(outfile))
        self.lb_done.setText("Process Done.")

    def selectAuto(self):
        self.list_file.setCurrentRow(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.move(0, 0)
    myWindow.show()
    app.exec_()
