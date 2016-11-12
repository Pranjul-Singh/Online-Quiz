# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'st_entry.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import urllib2
import urllib
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

class Ui_MainWindowStent(object):
    ###########################load dta###################################
    def ldta(self,tid,typ):
        self.tid=tid
        self.typ=typ
    ######################################################################

    ###########################save dta###################################
    def savedta(self):
        tid = self.tid
        sname = self.lineEdit.text()
        sid = self.lineEdit_2.text()
        pwd = self.lineEdit_3.text()
        dob = self.dateEdit.date().toPyDate()
        if self.typ==0:
            print "added by organiser"
            url = 'http://localhost/quiz/addstudent.php'
            values = {'tid':tid,
                      'sname':sname,
                      'sid':sid,
                      'pwd':pwd,
                      'dob':dob}
            data = urllib.urlencode(values)
            req = urllib2.Request(url,data)
            x = urllib2.urlopen(req)
        else:
            print "open test"
            url = 'http://localhost/quiz/addstudent.php'
            values = {'tid':tid,
                      'sname':sname,
                      'sid':sid,
                      'pwd':pwd,
                      'dob':dob}
            data = urllib.urlencode(values)
            req = urllib2.Request(url,data)
            x = urllib2.urlopen(req)
            app = QtGui.QApplication.instance()
            app.closeAllWindows()
    ######################################################################

    ###########################close window###################################
    def closewin(self):
        app = QtGui.QApplication.instance()
        app.closeAllWindows()
    ######################################################################
    def setupUiStent(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 110, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 781, 91))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("logo.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 180, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 220, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 260, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 300, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 180, 251, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 220, 251, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 260, 251, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(360, 300, 110, 22))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 360, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #########################save button##########################
        self.pushButton.clicked.connect(self.savedta)
        ##############################################################
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 360, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        #########################close button##########################
        self.pushButton_2.clicked.connect(self.closewin)
        ##############################################################
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Vision - Student Entry", None))
        self.label.setText(_translate("MainWindow", "Student Entry", None))
        self.label_2.setText(_translate("MainWindow", "Name", None))
        self.label_3.setText(_translate("MainWindow", "Student ID", None))
        self.label_4.setText(_translate("MainWindow", "Password", None))
        self.label_6.setText(_translate("MainWindow", "Date of Birth", None))
        self.pushButton.setText(_translate("MainWindow", "Save", None))
        self.pushButton_2.setText(_translate("MainWindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

