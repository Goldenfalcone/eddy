#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eddy_pitmaster.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import smbus
import time
import datetime
from subprocess import call
import sys
from PyQt4 import QtCore, QtGui

bus = smbus.SMBus(1)


#I2C addres

address = 0x4d
#this will tell how low will go until the heater starts again below the set point
P = 3
I = .05
B = 0
isHeating = True

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def get_current_temp():
	data = bus.read_i2c_block_data(address, 1,2)
	val = (data[0] << 8) + data[1]
	return val/5.00*9.00/5.00+32.00

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(575, 526)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 75))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.currentTemplcd = QtGui.QLCDNumber(self.centralwidget)
        self.currentTemplcd.setEnabled(True)
        self.currentTemplcd.setAutoFillBackground(True)
        self.currentTemplcd.setDigitCount(3)
        self.currentTemplcd.setObjectName(_fromUtf8("currentTemplcd"))
        self.horizontalLayout.addWidget(self.currentTemplcd)
        self.cookTemplcd = QtGui.QLCDNumber(self.centralwidget)
        self.cookTemplcd.setAutoFillBackground(True)
        self.cookTemplcd.setDigitCount(3)
        self.cookTemplcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.cookTemplcd.setObjectName(_fromUtf8("cookTemplcd"))
        self.horizontalLayout.addWidget(self.cookTemplcd)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setAutoFillBackground(True)
        self.horizontalSlider.setMinimum(100)
        self.horizontalSlider.setMaximum(500)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setPageStep(25)
        self.horizontalSlider.setSliderPosition(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.igniteButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.igniteButton.sizePolicy().hasHeightForWidth())
        self.igniteButton.setSizePolicy(sizePolicy)
        self.igniteButton.setObjectName(_fromUtf8("igniteButton"))
        self.horizontalLayout_4.addWidget(self.igniteButton)
        self.cookTempSet = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cookTempSet.sizePolicy().hasHeightForWidth())
        self.cookTempSet.setSizePolicy(sizePolicy)
        self.cookTempSet.setObjectName(_fromUtf8("cookTempSet"))
        self.horizontalLayout_4.addWidget(self.cookTempSet)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.cookTemplcd.display)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.cookTemplcd.display)
        self.cookTempSet.clicked.connect(self.setcookingtemp)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.igniteButton.clicked.connect(execfile('ignition.py'))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Eddy Pitmaster", None))
        self.label_2.setText(_translate("MainWindow", "Current Temperature", None))
        self.label.setText(_translate("MainWindow", "Cooking Temp", None))
        self.igniteButton.setText(_translate("MainWindow", "Ignition", None))
        self.cookTempSet.setText(_translate("MainWindow", "Set Temp", None))

    def setcookingtemp(self):
        setcookingtemp = self.horizontalSlider.value()
        print (setcookingtemp)

    previous_temp = int(get_current_temp())
    #Trying to prevent misreadings from groundloops from messing up temp swings
    while True:
        current_temp = int(get_current_temp())
        if current_temp > (109) and current_temp < (111):
            current_temp = previous_temp
        #Allowing for initial ramp up before setting the alerting
        if cooking_temp_met == False and current_temp >= target_temp:
            cooking_temp_met = True
        print ("You are in PID timer-while loop: Current Temp is %d and target temp is %d and INTERROR is %d") % (current_temp, target_temp, interror)
        error = (target_temp) - (current_temp)
        # Trying to prevent INTERROR from jumping too much when lid lifts, etc.  #autotune
        if error < 10 and error > 0:
            interror = interror + error
        power = B + ((P * error) + ((I * interror)))
        print ("power is %d" % power)
        previous_temp = current_temp
        for x in range(1,10):
            print (x)
            if (power > x**2): #May need tuning, still overshoots by power of 30, holds steady after that though
                if (heater_state=="off"):
                    heater_state = "on"
                    print ("State = ON")
                    print (current_temp)
                    turn_heat_on()
                else:
                    print ("Leaving the Heat ON")
            else:
                if (heater_state=="on"):
                    heater_state="off"
                    print ("State is OFF")
                    turn_heat_off()
            sleep(1)
        if (power < 10):
            sleep(10)
        #if prev_power < power - 1000 OR prev_power > power + 1000: #lid must be off??
            #sleep(180)
def main(argv):

	if len (self.horizontalSlider.value) < 2 :
		print ("Usage: temperature_hold  [temperature] ")
		sys.exit (1)
	target_temp=setcookingtemp
	try:
		target_temp=float(setcookingtemp)
	except ValueError:
		print ("the argument is not a number")
		sys.exit (1)
	print ("target temp =" , target_temp)
PID_Control_Loop(target_temp)
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
