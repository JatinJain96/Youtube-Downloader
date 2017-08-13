import sys
from PyQt4 import QtCore, QtGui, uic
from pytube import YouTube

form_class = uic.loadUiType("downloader.ui")[0]


class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)


    def video_download(self):
        url = str(self.url_link.text())
        yt = YouTube(url)
        video = yt.get('mp4', '360p')
        output_loc = str(self.output_link.text())
        video.download(output_loc)

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
