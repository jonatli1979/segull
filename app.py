from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('magnetorui.ui', self)
        self.button = self.findChild(QtWidgets.QPushButton, 'Record')
        self.button.clicked.connect(self.RecordButtonPressed)
        self.gps = self.findChild(QtWidgets.QCheckBox, 'GPS')
        self.gps.stateChanged.connect(self.GPSPressed)
        self.nemar = self.findChild(QtWidgets.QCheckBox, 'Nemar')
        self.nemar.stateChanged.connect(self.NemarPressed)
        self.tb = self.findChild(QtWidgets.QTextBrowser, 'textBrowser')
        self.gpsInfo = self.findChild(QtWidgets.QTextBrowser, 'GPS_info')
        self.plot = self.findChild(QtWidgets.QGraphicsView, 'Plot')
        pix = QPixmap('resources/pic.jpg')
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtGraphicsScene(0,0,400,200)
        scene.addItem(item)
        
        
        self.show()
    def RecordButtonPressed(self):
        print('Record pressed')
        self.Record.setText('Stop Recording')
        self.tb.append('Recording started')
    
    def GPSPressed(self):
        GPS_checked =self.gps.isChecked()
        if GPS_checked == True:
            self.tb.append('GPS Starting up')
            self.gpsInfo.clear()
        if GPS_checked == False:
            self.tb.append('GPS Off')
            self.gpsInfo.clear()
            self.gpsInfo.append('GPS Off')
            
    def NemarPressed(self):
        Nemar_checked =self.nemar.isChecked()
        print(Nemar_checked)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()