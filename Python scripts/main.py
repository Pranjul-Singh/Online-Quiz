# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from signup import Ui_MainWindow1
from st_login import Ui_MainWindowStlog
from org_dash import Ui_MainWindowLog
from res_log import Ui_MainWindowRlog
import urllib2
import urllib, json

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
class Ui_MainWindow(object):
    ###############################################################
    def ini(self):
        print "Pranjul Singh"
        url = 'http://localhost/quiz/availtest.php'
        x = urllib2.urlopen(url)
        c = json.loads(x.read())
        print len(c)
        i=0
        while i<len(c):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i,0,QtGui.QTableWidgetItem(c[i][u'tid']))
            self.tableWidget.setItem(i,1,QtGui.QTableWidgetItem(c[i][u'tname']))
            self.tableWidget.setItem(i,2,QtGui.QTableWidgetItem(c[i][u'ques']))
            self.tableWidget.setItem(i,3,QtGui.QTableWidgetItem(c[i][u'type']))
            i+=1
    ###############################################################
    
    ##########################Signup btn clicked####################
    def sign(self):
        print "Pranjul Singh"
        MainWindow.hide()
        self.signinWin = QtGui.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi1(self.signinWin)
        self.signinWin.show()
######################################################################

        #############################login function#######################
    def login(self):
        print "loging in"
        uid = self.lineEdit.text()
        paswd = self.lineEdit_2.text()
        url = 'http://localhost/quiz/login.php'
        values = {'id':uid,
                  'pass':paswd}
        data = urllib.urlencode(values)
        req = urllib2.Request(url,data)
        x = urllib2.urlopen(req)
        c = x.read()
        if c=='0':
            MainWindow.hide()
            self.logwin = QtGui.QMainWindow()
            self.ui = Ui_MainWindowLog()
            self.ui.setupUiLog(self.logwin)
            self.logwin.show()
            self.ui.con(uid,paswd)
            self.ui.ini1(uid)
        else :
            print "Wrong ID or Password"
        ################################################################

    ##############################33give test###############################
    def gtest(self):
        print "Give Test Clicked"
        row = self.tableWidget.currentItem().row()
        tid = self.tableWidget.item(row,0).text()
        ques = self.tableWidget.item(row,2).text()
        MainWindow.hide()
        self.stlogwin = QtGui.QMainWindow()
        self.ui = Ui_MainWindowStlog()
        self.ui.setupUiStlog(self.stlogwin)
        self.stlogwin.show()
        self.ui.setdta(tid,ques)
    #########################################################################

    #####################################result function####################
    def rslt(self):
        print "Result clicked"
        MainWindow.hide()
        self.stlogwin = QtGui.QMainWindow()
        self.ui = Ui_MainWindowRlog()
        self.ui.setupUiRlog(self.stlogwin)
        self.stlogwin.show()
    #########################################################################
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(370, 180, 411, 261))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 150, 181, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cooper Black"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet(_fromUtf8("color:rgb(0,128,192);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #######################login##############################
        self.pushButton.clicked.connect(self.gtest)
        ##########################################################


        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 140, 110, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton"))
        #######################login##############################
        self.pushButton_4.clicked.connect(self.rslt)
        ##########################################################

        
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 191, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cooper Black"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(0,128,192);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setStyleSheet(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 210, 181, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 270, 181, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 320, 111, 31))
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        #######################login##############################
        self.pushButton_2.clicked.connect(self.login)
        ##########################################################
        
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 370, 111, 31))
        
        #####################signup#########################
        self.pushButton_3.clicked.connect(self.sign)
        #####################################################
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Constantia"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 781, 91))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("logo.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuResults = QtGui.QMenu(self.menubar)
        self.menuResults.setObjectName(_fromUtf8("menuResults"))
        ############################result menu##########################
        self.menuResults.triggered.connect(lambda: self.rslt())
        ##################################################################
        self.menuTests = QtGui.QMenu(self.menubar)
        self.menuTests.setObjectName(_fromUtf8("menuTests"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAvailable_Test = QtGui.QAction(MainWindow)
        self.actionAvailable_Test.setObjectName(_fromUtf8("actionAvailable_Test"))
        self.actionUpcoming_Test = QtGui.QAction(MainWindow)
        self.actionUpcoming_Test.setObjectName(_fromUtf8("actionUpcoming_Test"))
        self.menuFile.addAction(self.actionExit)
        self.menuTests.addAction(self.actionAvailable_Test)
        self.menuTests.addAction(self.actionUpcoming_Test)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuResults.menuAction())
        self.menubar.addAction(self.menuTests.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Vision-Online Quiz Organiser", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Test ID.", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Test Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Organiser", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Type", None))
        self.label.setText(_translate("MainWindow", "Available Tests", None))
        self.pushButton.setText(_translate("MainWindow", "Give Test", None))
        self.label_2.setText(_translate("MainWindow", "Organiser Login", None))
        self.label_3.setText(_translate("MainWindow", "Login ID", None))
        self.label_4.setText(_translate("MainWindow", "Password", None))
        self.pushButton_2.setText(_translate("MainWindow", "Login", None))
        self.pushButton_3.setText(_translate("MainWindow", "Signup", None))
        self.pushButton_4.setText(_translate("MainWindow", "Result", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuResults.setTitle(_translate("MainWindow", "Results", None))
        self.menuTests.setTitle(_translate("MainWindow", "Tests", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAvailable_Test.setText(_translate("MainWindow", "Available Test", None))
        self.actionUpcoming_Test.setText(_translate("MainWindow", "Upcoming Test", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.ini()
    sys.exit(app.exec_())

