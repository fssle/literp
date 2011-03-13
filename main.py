# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from ziluolan import Ui_MainWindow
import os
import simplejson

class LoginWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setGeometry(QtCore.QRect(0, 0, 200, 120))
        
        mainLayout = QtGui.QVBoxLayout()
        
        hLayoutUser = QtGui.QHBoxLayout()
        self.label_user = QtGui.QLabel(self)
        hLayoutUser.addWidget(self.label_user)
        self.lineEdit_user = QtGui.QLineEdit(self)
        self.lineEdit_user.setText("admin")
        hLayoutUser.addWidget(self.lineEdit_user)
        mainLayout.addLayout(hLayoutUser)

        hLayoutPass = QtGui.QHBoxLayout()
        self.label_pass = QtGui.QLabel(self)
        hLayoutPass.addWidget(self.label_pass)
        self.lineEdit_pass = QtGui.QLineEdit(self)
        self.lineEdit_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_pass.setText("admin")
        hLayoutPass.addWidget(self.lineEdit_pass)
        mainLayout.addLayout(hLayoutPass)

        hLayoutCmd = QtGui.QHBoxLayout()
        self.pushButtonLogin = QtGui.QPushButton(self)
        hLayoutCmd.addWidget(self.pushButtonLogin)
        self.pushButtonExit = QtGui.QPushButton(self)
        hLayoutCmd.addWidget(self.pushButtonExit)
        
        self.label_msg = QtGui.QLabel(self)
        mainLayout.addWidget(self.label_msg)
        
        self.progbar = QtGui.QProgressBar(self) 
        self.progbar.setProperty("value",QtCore.QVariant(0)) 
        mainLayout.addWidget(self.progbar)
        
        mainLayout.addLayout(hLayoutCmd)

        widget = QtGui.QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)
        
        self.retranslateUi()
        QtCore.QObject.connect(self.pushButtonExit, QtCore.SIGNAL("pressed()"), self.doExit)
        QtCore.QObject.connect(self.pushButtonLogin, QtCore.SIGNAL("pressed()"), self.doLogin)

        self.progbar.hide()
        self.center()
        
    def retranslateUi(self):
        self.label_user.setText(QtGui.QApplication.translate("MainWindow", "用户:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pass.setText(QtGui.QApplication.translate("MainWindow", "密码:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLogin.setText(QtGui.QApplication.translate("MainWindow", "登入", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonExit.setText(QtGui.QApplication.translate("MainWindow", "退出", None, QtGui.QApplication.UnicodeUTF8))
        
    def doExit(self):
        print("called doExit")
        self.close()
    
    def doLogin(self):
        print("called doLogin")
        usr=str(self.lineEdit_user.text())
        pwd=str(self.lineEdit_pass.text())
        if self.checkPass(usr, pwd):
            self.showZLL()
        else:
            self.label_msg.setText("user can not login.")
            
    def showZLL(self):
        self.main = Ui_MainWindow()
        self.main.showFullScreen()
        self.main.show()
        self.close()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        print(screen, size)
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) /2)

    def checkPass(self, usr, pwd):
        print(usr, pwd)
        #return ret
        if usr == "admin" and pwd == "admin":
            return True
        return False

#===============================================================================
#   Example
#===============================================================================
if __name__ == '__main__':
    import sys
    
    app = QtGui.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())