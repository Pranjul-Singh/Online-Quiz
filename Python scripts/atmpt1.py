# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'atmpt.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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

class Ui_MainWindowAtmpt(object):

    ############################3init data######################################
    def indta(self,a,b,c,d):
        self.tid=a
        self.uid=b
        self.pwd=c
        self.ques=d
        print self.tid,self.uid,self.pwd
        url = 'http://localhost/quiz/questions.php'
        values = {'tid':self.tid}
        #          'uid':self.uid,
        #          'pass':self.pwd,
        #          'ques':self.ques}
        data = urllib.urlencode(values)
        req = urllib2.Request(url,data)
        x = urllib2.urlopen(req)
        c = json.loads(x.read())
        self.qtn = c
        self.qno = int(c[0][u'qno'])
        print c
        self.label.setText(str(c[0][u'qno']))
        self.textEdit.setText(c[0][u'ques'])
        self.textEdit_2.setText(c[0][u'op1'])
        self.textEdit_3.setText(c[0][u'op2'])
        self.textEdit_4.setText(c[0][u'op3'])
        self.textEdit_5.setText(c[0][u'op4'])
        self.label_9.setText(c[0][u'mrks'])


        url1 = 'http://localhost/quiz/logged.php'
        values1 = {'tid':self.tid,
                  'uid':self.uid}
        data1 = urllib.urlencode(values1)
        req1 = urllib2.Request(url1,data1)
        x1 = urllib2.urlopen(req1)
        print self.tid
        print self.uid
        
    ############################################################################

    ###################################3submit function#########################
    def sbmt(self):
        val = self.spinBox.value()
        url1 = 'http://localhost/quiz/markans.php'
        values1 = {'tid':self.tid,
                   'uid':self.uid,
                   'ans':val,
                   'qno':self.qno}
        data1 = urllib.urlencode(values1)
        req1 = urllib2.Request(url1,data1)
        x1 = urllib2.urlopen(req1)
        self.qno+=1
        if self.qno>int(self.ques):
            app = QtGui.QApplication.instance()
            app.closeAllWindows()
        else:
            self.label.setText(str(self.qtn[self.qno-1][u'qno']))
            self.textEdit.setText(self.qtn[self.qno-1][u'ques'])
            self.textEdit_2.setText(self.qtn[self.qno-1][u'op1'])
            self.textEdit_3.setText(self.qtn[self.qno-1][u'op2'])
            self.textEdit_4.setText(self.qtn[self.qno-1][u'op3'])
            self.textEdit_5.setText(self.qtn[self.qno-1][u'op4'])
            self.label_9.setText(self.qtn[self.qno-1][u'mrks'])
        
    ############################################################################

        
    def setupUiAtmpt(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 781, 91))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("logo.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 150, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 130, 701, 121))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 290, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 290, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 370, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 370, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 435, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 430, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(110, 430, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(540, 430, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 270, 321, 61))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(460, 270, 321, 61))
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(80, 340, 321, 61))
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.textEdit_5 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(460, 340, 321, 61))
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 440, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ##########################submit bbtn clicked#########################
        self.pushButton.clicked.connect(self.sbmt)
        #######################################################################
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Vision", None))
        self.label.setText(_translate("MainWindow", "Ques 1.", None))
        self.label_2.setText(_translate("MainWindow", "1.", None))
        self.label_3.setText(_translate("MainWindow", "2.", None))
        self.label_4.setText(_translate("MainWindow", "3.", None))
        self.label_6.setText(_translate("MainWindow", "4.", None))
        self.label_7.setText(_translate("MainWindow", "Marks", None))
        self.label_8.setText(_translate("MainWindow", "Answer", None))
        self.label_9.setText(_translate("MainWindow", "0.0", None))
        self.pushButton.setText(_translate("MainWindow", "Submit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

