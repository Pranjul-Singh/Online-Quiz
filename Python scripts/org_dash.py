# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'org_dash.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from create_test import Ui_MainWindowTst
import sys
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

class Ui_MainWindowLog(object):

    ###############################################################
    def ini1(self,uid1):
        print "Pranjul Singh"
        a = "http://localhost/quiz/createdtest.php?oid='"
        b = "'"
        url = str(a+uid1+b)
        values = {'oid':uid1}
        #data = urllib.urlencode(values)
        #req = urllib2.Request(url,data)
        x = urllib2.urlopen(url)
        c = json.loads(x.read())
        print len(c)
        i=0
        while i<len(c):
            print c[i][u'tid']
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i,0,QtGui.QTableWidgetItem(c[i][u'tid']))
            self.tableWidget.setItem(i,1,QtGui.QTableWidgetItem(c[i][u'tname']))
            self.tableWidget.setItem(i,2,QtGui.QTableWidgetItem(c[i][u'date']))
            self.tableWidget.setItem(i,3,QtGui.QTableWidgetItem(c[i][u'time']))
            self.tableWidget.setItem(i,4,QtGui.QTableWidgetItem(c[i][u'type']))
            self.tableWidget.setItem(i,5,QtGui.QTableWidgetItem(c[i][u'ques']))
            i+=1
    ###############################################################

    ######################executed by login window#######################
    def con(self,a,b):
        print "Everything is okay"
        self.id1 = a
        self.pas = b
        print self.id1
        print self.pas
    ######################################################################

    ############################################################################
    def chk(self):
        print "selecting table"
        #row = self.tableWidget.selectionModel().selectedRows()
        row = self.tableWidget.currentItem().row()
        print row
        print self.tableWidget.item(row,0).text()
    ###########################################################################

    ################################create Test################################
    def createtst(self,MainWindow):
        print "creating Test"
        app = QtGui.QApplication.instance()
        app.closeAllWindows()
        self.createwin = QtGui.QMainWindow()
        self.ui = Ui_MainWindowTst()
        self.ui.setupUiTst(self.createwin)
        self.ui.con(self.id1,self.pas)
        self.createwin.show()
    ###########################################################################
        
    def setupUiLog(self, MainWindow):
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
        self.label.setGeometry(QtCore.QRect(20, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 160, 761, 231))
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 410, 121, 31))
        ##############################create test#######################
        self.pushButton.clicked.connect(self.createtst)
        ################################################################
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 410, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 410, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 110, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuProfile = QtGui.QMenu(self.menubar)
        self.menuProfile.setObjectName(_fromUtf8("menuProfile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionEdit_Profile = QtGui.QAction(MainWindow)
        self.actionEdit_Profile.setObjectName(_fromUtf8("actionEdit_Profile"))
        self.actionLogout = QtGui.QAction(MainWindow)
        self.actionLogout.setObjectName(_fromUtf8("actionLogout"))
        self.actionLogout_2 = QtGui.QAction(MainWindow)
        self.actionLogout_2.setObjectName(_fromUtf8("actionLogout_2"))
        self.menuFile.addAction(self.actionExit)
        self.menuProfile.addAction(self.actionEdit_Profile)
        self.menuProfile.addAction(self.actionLogout_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProfile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Vision - Organiser Dashboard", None))
        self.label.setText(_translate("MainWindow", "Organised Tests By", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Test ID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Test Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Type", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Questions", None))
        self.pushButton.setText(_translate("MainWindow", "Create New Test", None))
        self.pushButton_2.setText(_translate("MainWindow", "Manage Test", None))
        self.pushButton_3.setText(_translate("MainWindow", "Results", None))
        self.label_2.setText(_translate("MainWindow", "Organiser Name", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuProfile.setTitle(_translate("MainWindow", "Profile", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionEdit_Profile.setText(_translate("MainWindow", "Edit Profile", None))
        self.actionLogout.setText(_translate("MainWindow", "Logout", None))
        self.actionLogout_2.setText(_translate("MainWindow", "Logout", None))


if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

