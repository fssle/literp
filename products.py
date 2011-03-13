# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

from querytable import QueryTableWidget

class ProductsWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(QtGui.QWidget, self).__init__(parent)

        self.setObjectName("tabProducts")

        mainLayout = QtGui.QHBoxLayout()
        
        vLayoutLeft = QtGui.QVBoxLayout()
        
        self.tableWidget = QtGui.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(320, 20, 261, 231))
        vLayoutLeft.addWidget(self.tableWidget)

        mainLayout.addLayout(vLayoutLeft)

        vLayoutRight = QtGui.QVBoxLayout()
        
        hLayoutSN = QtGui.QHBoxLayout()

        self.label_brand = QtGui.QLabel(self)
        hLayoutSN.addWidget(self.label_brand)

        self.lineEdit_brand = QtGui.QLineEdit(self)
        self.lineEdit_brand.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutSN.addWidget(self.lineEdit_brand)

        self.label_sn = QtGui.QLabel(self)
        hLayoutSN.addWidget(self.label_sn)

        self.lineEdit_sn = QtGui.QLineEdit(self)
        self.lineEdit_sn.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutSN.addWidget(self.lineEdit_sn)
        vLayoutRight.addLayout(hLayoutSN)

        hLayoutPrice = QtGui.QHBoxLayout()
        self.label_price = QtGui.QLabel(self)
        hLayoutPrice.addWidget(self.label_price)

        self.lineEdit_price = QtGui.QLineEdit(self)
        self.lineEdit_price.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutPrice.addWidget(self.lineEdit_price)
        vLayoutRight.addLayout(hLayoutPrice)

        self.label_image = QtGui.QLabel(self)
        vLayoutRight.addWidget(self.label_image)

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

        vLayoutRight.addLayout(hLayoutCmd)

        mainLayout.addLayout(vLayoutRight)

        self.setLayout(mainLayout)

        self.retranslateUi()

        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("selectionChanged()"), self.tableWidget_selectionChanged)
        QtCore.QObject.connect(self.pushButtonAdd, QtCore.SIGNAL("pressed()"), self.doCmdAdd)
        QtCore.QObject.connect(self.pushButtonEdit, QtCore.SIGNAL("pressed()"), self.doCmdEdit)
        QtCore.QObject.connect(self.pushButtonDel, QtCore.SIGNAL("pressed()"), self.doCmdDel)
        
    def retranslateUi(self):
        self.label_sn.setText(QtGui.QApplication.translate("MainWindow", "代码", None, QtGui.QApplication.UnicodeUTF8))
        self.label_price.setText(QtGui.QApplication.translate("MainWindow", "单价", None, QtGui.QApplication.UnicodeUTF8))
        self.label_brand.setText(QtGui.QApplication.translate("MainWindow", "品牌", None, QtGui.QApplication.UnicodeUTF8))
        self.label_image.setText(QtGui.QApplication.translate("MainWindow", "图片没找到", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdd.setText(QtGui.QApplication.translate("MainWindow", "加入", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEdit.setText(QtGui.QApplication.translate("MainWindow", "修改", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDel.setText(QtGui.QApplication.translate("MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        
    def doBrowser(self):
        print("called doBrowser")
        fn=QtGui.QFileDialog.getOpenFileName(self, 'Open file', '', '*.jpg')
        self.label_image.setPixmap(QtGui.QPixmap(fn))

    def tableWidget_selectionChanged(self):
        print("called tblWidget_selectionChanged")
        row=self.tblWidget.currentRow()
        code = str(self.tblWidget.item(row,2).text())
        print(code)
        #self.tblWidgetZS.query(u'select * from Suggestion where 股票代码=?'.encode('utf-8'), (code,))

    def doCmdAdd(self):
        print("called doCmdAdd")

    def doCmdEdit(self):
        print("called doCmdEdit")

    def doCmdDel(self):
        print("called doCmdDel")


#===============================================================================
#   Example
#===============================================================================
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QMainWindow, QApplication
    
    class ApplicationWindow(QMainWindow):
        def __init__(self):
            QMainWindow.__init__(self)
            self.widget = ProductsWidget(self)
            self.widget.setFocus()
            self.setCentralWidget(self.widget)
           
    app = QApplication(sys.argv)
    win = ApplicationWindow()
    win.show()
    sys.exit(app.exec_())