# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class TradingWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(QtGui.QWidget, self).__init__(parent)

        self.setObjectName("tabTrading")

        mainLayout = QtGui.QHBoxLayout()
        
        vLayoutLeft = QtGui.QVBoxLayout()

        hLayoutQuery = QtGui.QHBoxLayout()
        self.label_brand = QtGui.QLabel(self)
        hLayoutQuery.addWidget(self.label_brand)

        self.lineEdit_brand = QtGui.QLineEdit(self)
        self.lineEdit_brand.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutQuery.addWidget(self.lineEdit_brand)

        self.label_sn = QtGui.QLabel(self)
        hLayoutQuery.addWidget(self.label_sn)

        self.lineEdit_sn = QtGui.QLineEdit(self)
        self.lineEdit_sn.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutQuery.addWidget(self.lineEdit_sn)

        self.pushButtonQuery = QtGui.QPushButton(self)
        self.pushButtonQuery.setGeometry(QtCore.QRect(210, 0, 75, 23))
        hLayoutQuery.addWidget(self.pushButtonQuery)
    
        vLayoutLeft.addLayout(hLayoutQuery)
        
        self.label_image = QtGui.QLabel(self)
        vLayoutLeft.addWidget(self.label_image)

        hLayoutPrice = QtGui.QHBoxLayout()
        self.label_price = QtGui.QLabel(self)
        hLayoutPrice.addWidget(self.label_price)

        self.lineEdit_price = QtGui.QLineEdit(self)
        self.lineEdit_price.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutPrice.addWidget(self.lineEdit_price)
        vLayoutLeft.addLayout(hLayoutPrice)

        hLayoutNumber = QtGui.QHBoxLayout()
        self.label_number = QtGui.QLabel(self)
        hLayoutNumber.addWidget(self.label_number)

        self.lineEdit_number = QtGui.QLineEdit(self)
        self.lineEdit_number.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutNumber.addWidget(self.lineEdit_number)

        vLayoutLeft.addLayout(hLayoutNumber)

        hLayoutCmd = QtGui.QHBoxLayout()
        
        self.pushButtonAdd = QtGui.QPushButton(self)
        self.pushButtonAdd.setGeometry(QtCore.QRect(210, 0, 75, 23))
        hLayoutCmd.addWidget(self.pushButtonAdd)

        self.pushButtonEdit = QtGui.QPushButton(self)
        self.pushButtonEdit.setGeometry(QtCore.QRect(210, 0, 75, 23))
        hLayoutCmd.addWidget(self.pushButtonEdit)

        self.pushButtonDel = QtGui.QPushButton(self)
        self.pushButtonDel.setGeometry(QtCore.QRect(210, 0, 75, 23))
        hLayoutCmd.addWidget(self.pushButtonDel)

        vLayoutLeft.addLayout(hLayoutCmd)

        mainLayout.addLayout(vLayoutLeft)

        vLayoutRight = QtGui.QVBoxLayout()
        
        self.tableWidget = QtGui.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(320, 20, 261, 231))
        vLayoutRight.addWidget(self.tableWidget)

        self.label_pay = QtGui.QLabel(self)
        vLayoutRight.addWidget(self.label_pay)

        hLayoutChange = QtGui.QHBoxLayout()
        self.label_total = QtGui.QLabel(self)
        hLayoutChange.addWidget(self.label_total)

        self.lineEdit_total = QtGui.QLineEdit(self)
        self.lineEdit_total.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutChange.addWidget(self.lineEdit_total)

        self.label_change = QtGui.QLabel(self)
        hLayoutChange.addWidget(self.label_change)

        vLayoutRight.addLayout(hLayoutChange) 

        self.pushButtonSave = QtGui.QPushButton(self)
        self.pushButtonSave.setGeometry(QtCore.QRect(210, 0, 75, 23))
        vLayoutRight.addWidget(self.pushButtonSave)

        mainLayout.addLayout(vLayoutRight)

        self.setLayout(mainLayout)

        self.retranslateUi()

        QtCore.QObject.connect(self.pushButtonQuery, QtCore.SIGNAL("pressed()"), self.doQuery)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("selectionChanged()"), self.tableWidget_selectionChanged)
        QtCore.QObject.connect(self.pushButtonAdd, QtCore.SIGNAL("pressed()"), self.doCmdAdd)
        QtCore.QObject.connect(self.pushButtonEdit, QtCore.SIGNAL("pressed()"), self.doCmdEdit)
        QtCore.QObject.connect(self.pushButtonDel, QtCore.SIGNAL("pressed()"), self.doCmdDel)
        QtCore.QObject.connect(self.pushButtonSave, QtCore.SIGNAL("pressed()"), self.doCmdSave)

    def retranslateUi(self):
        self.label_brand.setText(QtGui.QApplication.translate("MainWindow", "品牌", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sn.setText(QtGui.QApplication.translate("MainWindow", "代码", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonQuery.setText(QtGui.QApplication.translate("MainWindow", "查询", None, QtGui.QApplication.UnicodeUTF8))
        self.label_image.setText(QtGui.QApplication.translate("MainWindow", "图片没找到", None, QtGui.QApplication.UnicodeUTF8))
        self.label_price.setText(QtGui.QApplication.translate("MainWindow", "单价", None, QtGui.QApplication.UnicodeUTF8))
        self.label_number.setText(QtGui.QApplication.translate("MainWindow", "数量", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdd.setText(QtGui.QApplication.translate("MainWindow", "加入", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEdit.setText(QtGui.QApplication.translate("MainWindow", "修改", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDel.setText(QtGui.QApplication.translate("MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pay.setText(QtGui.QApplication.translate("MainWindow", "总款", None, QtGui.QApplication.UnicodeUTF8))
        self.label_total.setText(QtGui.QApplication.translate("MainWindow", "已付", None, QtGui.QApplication.UnicodeUTF8))
        self.label_change.setText(QtGui.QApplication.translate("MainWindow", "找零:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSave.setText(QtGui.QApplication.translate("MainWindow", "保存", None, QtGui.QApplication.UnicodeUTF8))
        
    def doQuery(self):
        print("called doQuery")
        sn = str(self.lineEdit_sn.text())
        self.label_image.setPixmap(QtGui.QPixmap("image/%s.jpg"%(sn)))

    def doCmdAdd(self):
        print("called doCmdAdd")
        date = str(self.lineEdit.text())

    def doCmdEdit(self):
        print("called doCmdEdit")
        date = str(self.lineEdit.text())

    def doCmdDel(self):
        print("called doCmdDel")
        date = str(self.lineEdit.text())

    def doCmdSave(self):
        print("called doCmdSave")
        date = str(self.lineEdit.text())

    def tableWidget_selectionChanged(self):
        print("called tblWidget_selectionChanged")
        row=self.tblWidget.currentRow()
        code = str(self.tblWidget.item(row,2).text())
        print(code)
        #self.tblWidgetZS.query(u'select * from Suggestion where 股票代码=?'.encode('utf-8'), (code,))
        
#===============================================================================
#   Example
#===============================================================================
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QMainWindow, QApplication
    
    class ApplicationWindow(QMainWindow):
        def __init__(self):
            QMainWindow.__init__(self)
            self.widget = TradingWidget(self)
            self.widget.setFocus()
            self.setCentralWidget(self.widget)
           
    app = QApplication(sys.argv)
    win = ApplicationWindow()
    win.show()
    sys.exit(app.exec_())