# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter_ques.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from st_entry import Ui_MainWindowStent
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

class Ui_MainWindowEques(object):
    
    ##############################init enter ques###############################
    def setdta(self,oid,opas,tid,ques,typ):
        self.oid = oid
        self.opas = opas
        self.tid = tid
        self.ques = ques
        self.qno =1
        self.typ=typ
        
    ##########################################################################

    ################################enter questions###########################
    def entques(self):
        ques = self.textEdit.toPlainText()
        op1 = self.textEdit_2.toPlainText()
        op2 = self.textEdit_3.toPlainText()
        op3 = self.textEdit_4.toPlainText()
        op4 = self.textEdit_5.toPlainText()
        mrks = self.spinBox.value()
        ans = self.spinBox_2.value()
        tid = self.tid
        if self.qno<=self.ques:
            url = 'http://localhost/quiz/enterques.php'
            values = {'tid':tid,
                      'qno':self.qno,
                      'ques':ques,
                      'op1':op1,
                      'op2':op2,
                      'op3':op3,
                      'op4':op4,
                      'ans':ans,
                      'mrks':mrks}
            data = urllib.urlencode(values)
            req = urllib2.Request(url,data)
            x = urllib2.urlopen(req)
            print "Saved Question",self.qno
            self.qno+=1
        else :
            print "Questions completed"
            styp = self.typ
            if self.typ==0:
                print "enter students"
                url = 'http://localhost/quiz/createtable.php'
                values = {'tid':tid,
                          'ques':self.ques}
                data = urllib.urlencode(values)
                req = urllib2.Request(url,data)
                x = urllib2.urlopen(req)
                print x.read()
                
                app = QtGui.QApplication.instance()
                app.closeAllWindows()
                self.stwin = QtGui.QMainWindow()
                self.ui = Ui_MainWindowStent()
                self.ui.setupUiStent(self.stwin)
                self.ui.ldta(tid,styp)
                self.stwin.show()
                
                
            else:
                url = 'http://localhost/quiz/createtable.php'
                values = {'tid':tid,
                          'ques':ques}
                data = urllib.urlencode(values)
                req = urllib2.Request(url,data)
                x = urllib2.urlopen(req)
                print x.read()
                app = QtGui.QApplication.instance()
                app.closeAllWindows()
    ##########################################################################
    
    def setupUiEques(self, MainWindow):
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
        self.label_2.setGeometry(QtCore.QRect(20, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 260, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 330, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 330, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 400, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 400, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 430, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ###########################save ques##################################
        self.pushButton.clicked.connect(self.entques)
        ######################################################################
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 150, 681, 81))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 250, 301, 51))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(470, 250, 301, 51))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(90, 320, 301, 51))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.textEdit_5 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(470, 320, 301, 51))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(90, 400, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(530, 400, 42, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Vision - Enter Questions", None))
        self.label.setText(_translate("MainWindow", "Enter Questions", None))
        self.label_2.setText(_translate("MainWindow", "Question", None))
        self.label_3.setText(_translate("MainWindow", "Option 1", None))
        self.label_4.setText(_translate("MainWindow", "Option 2", None))
        self.label_6.setText(_translate("MainWindow", "Option 3", None))
        self.label_7.setText(_translate("MainWindow", "Option 4", None))
        self.label_8.setText(_translate("MainWindow", "Marks", None))
        self.label_9.setText(_translate("MainWindow", "Correct Option", None))
        self.pushButton.setText(_translate("MainWindow", "Next", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

