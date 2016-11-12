# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import urllib2
import urllib
from enter_ques import Ui_MainWindowEques
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

class Ui_MainWindowTst(object):

    ##############################set id and pass#############################
    def con(self,a,b):
        self.id = a
        self.pas = b
    ##########################################################################

    ##############################to enter ques###############################
    def eques(self,oid,opas,tid,ques,typ):
        app = QtGui.QApplication.instance()
        app.closeAllWindows()
        self.eqwin = QtGui.QMainWindow()
        self.ui = Ui_MainWindowEques()
        self.ui.setupUiEques(self.eqwin)
        self.eqwin.show()
        self.ui.setdta(oid,opas,tid,ques,typ)
        
    ##########################################################################
    

    #############################33create test function########################
    def createtst(self):
        print "creating test"
        tname = self.lineEdit.text()
        tid = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            typ = 1
        else:
            typ = 0
        tdate = self.dateEdit.date().toPyDate()
        time = self.timeEdit.time().toPyTime()
        dur = self.timeEdit_2.time().toPyTime()
        ques = self.spinBox.value()
        oid = self.id;
        print tname,tid,typ,tdate,time,dur,ques,oid
        url = 'http://localhost/quiz/createtest.php'
        values = {'tid':tid,
                  'tname':tname,
                  'oid':oid,
                  'type':typ,
                  'tdate':tdate,
                  'ttime':time,
                  'dur':dur,
                  'ques':ques}
        data = urllib.urlencode(values)
        req = urllib2.Request(url,data)
        x = urllib2.urlopen(req)
        self.eques(oid,self.pas,tid,ques,typ)
        
    ##########################################################################
    def setupUiTst(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 781, 91))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("logo.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 110, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 150, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 190, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 230, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(350, 230, 82, 21))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(570, 230, 82, 21))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 270, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 310, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 350, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(160, 390, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 150, 301, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 190, 301, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(350, 270, 110, 22))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.timeEdit = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(350, 310, 118, 22))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.timeEdit_2 = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setGeometry(QtCore.QRect(350, 350, 118, 22))
        self.timeEdit_2.setObjectName(_fromUtf8("timeEdit_2"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(350, 390, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 430, 91, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ##########################create test clicked##########################
        self.pushButton.clicked.connect(self.createtst)
        ######################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Vision- Create New Test", None))
        self.label.setText(_translate("MainWindow", "Create New Test", None))
        self.label_2.setText(_translate("MainWindow", "Test Name", None))
        self.label_3.setText(_translate("MainWindow", "Test ID", None))
        self.label_4.setText(_translate("MainWindow", "Type", None))
        self.radioButton.setText(_translate("MainWindow", "Open for all", None))
        self.radioButton_2.setText(_translate("MainWindow", "Closed Type", None))
        self.label_6.setText(_translate("MainWindow", "Date", None))
        self.label_7.setText(_translate("MainWindow", "Time to Start Test", None))
        self.label_8.setText(_translate("MainWindow", "Duration", None))
        self.label_9.setText(_translate("MainWindow", "Number of Questions", None))
        self.pushButton.setText(_translate("MainWindow", "Create Test", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

