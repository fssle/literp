# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

from producttable import ProductTable
from model import *

class ProductsWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(QtGui.QWidget, self).__init__(parent)

        self.setObjectName("tabProducts")

        mainLayout = QtGui.QHBoxLayout()
        
        vLayoutLeft = QtGui.QVBoxLayout()
        
        self.tableWidget = ProductTable(self)
        self.tableWidget.setGeometry(QtCore.QRect(320, 20, 261, 231))
        vLayoutLeft.addWidget(self.tableWidget)

        mainLayout.addLayout(vLayoutLeft)

        vLayoutRight = QtGui.QVBoxLayout()

        hLayoutSN = QtGui.QHBoxLayout()

        self.label_sn = QtGui.QLabel(self)
        hLayoutSN.addWidget(self.label_sn)

        self.lineEdit_sn = QtGui.QLineEdit(self)
        self.lineEdit_sn.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutSN.addWidget(self.lineEdit_sn)
        vLayoutRight.addLayout(hLayoutSN)

        hLayoutBrand = QtGui.QHBoxLayout()
        self.label_brand = QtGui.QLabel(self)
        hLayoutBrand.addWidget(self.label_brand)

        self.lineEdit_brand = QtGui.QLineEdit(self)
        self.lineEdit_brand.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutBrand.addWidget(self.lineEdit_brand)
        vLayoutRight.addLayout(hLayoutBrand)

        hLayoutPrice = QtGui.QHBoxLayout()
        self.label_price = QtGui.QLabel(self)
        hLayoutPrice.addWidget(self.label_price)

        self.lineEdit_price = QtGui.QLineEdit(self)
        self.lineEdit_price.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutPrice.addWidget(self.lineEdit_price)
        vLayoutRight.addLayout(hLayoutPrice)

        self.label_image = QtGui.QLabel(self)
        vLayoutRight.addWidget(self.label_image)

        self.label_msg = QtGui.QLabel(self)
        vLayoutRight.addWidget(self.label_msg)

        hLayoutCmd = QtGui.QHBoxLayout()

        self.pushButtonUpdate = QtGui.QPushButton(self)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(210, 0, 75, 23))
        hLayoutCmd.addWidget(self.pushButtonUpdate)

        self.pushButtonDel = QtGui.QPushButton(self)
        self.pushButtonDel.setGeometry(QtCore.QRect(210, 0, 75, 23))
        hLayoutCmd.addWidget(self.pushButtonDel)

        vLayoutRight.addLayout(hLayoutCmd)

        mainLayout.addLayout(vLayoutRight)

        self.setLayout(mainLayout)

        self.retranslateUi()

        self.tableWidget_selectionChanged()

        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("selectionChanged()"), self.tableWidget_selectionChanged)
        QtCore.QObject.connect(self.pushButtonUpdate, QtCore.SIGNAL("pressed()"), self.doCmdUpdate)
        QtCore.QObject.connect(self.pushButtonDel, QtCore.SIGNAL("pressed()"), self.doCmdDel)
        
    def retranslateUi(self):
        self.label_sn.setText(QtGui.QApplication.translate("MainWindow", "代码", None, QtGui.QApplication.UnicodeUTF8))
        self.label_price.setText(QtGui.QApplication.translate("MainWindow", "单价", None, QtGui.QApplication.UnicodeUTF8))
        self.label_brand.setText(QtGui.QApplication.translate("MainWindow", "品牌", None, QtGui.QApplication.UnicodeUTF8))
        self.label_image.setText(QtGui.QApplication.translate("MainWindow", "图片没找到", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUpdate.setText(QtGui.QApplication.translate("MainWindow", "更新", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDel.setText(QtGui.QApplication.translate("MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        
    def tableWidget_selectionChanged(self):
        print("called tblWidget_selectionChanged")
        row=self.tableWidget.currentRow()
        if row>=0:
            sn = str(self.tableWidget.item(row,0).text())
            print(sn)
            p = Product.query.filter_by(sn=sn).one()
            if p is None:
                self.label_msg = "did not found."
            else:
                self.lineEdit_sn.setText(sn)
                self.lineEdit_brand.setText(p.brand)
                self.lineEdit_price.setText("%.02f"%(p.price))
                self.label_image.setPixmap(QtGui.QPixmap("image/%s.jpg"%(sn)))
                
    def doCmdUpdate(self):
        print("called doCmdUpdate")
        sn = str(self.lineEdit_sn.text())
        p = Product.get_by(sn=sn)
        if p is None:
            price=float(self.lineEdit_price.text())
            brand=unicode(self.lineEdit_brand.text())
            Product(sn=sn, brand=brand, price=price)
            session.commit()
            self.label_msg.setText(QtGui.QApplication.translate("MainWindow", "产品添加成功", None, QtGui.QApplication.UnicodeUTF8))
        else:
            p.sn=sn
            p.brand=unicode(self.lineEdit_brand.text())
            p.price=float(self.lineEdit_price.text())
            session.commit()
            self.label_msg.setText(QtGui.QApplication.translate("MainWindow", "产品更新成功", None, QtGui.QApplication.UnicodeUTF8))
            
        self.tableWidget.query()

    def doCmdDel(self):
        print("called doCmdDel")
        sn = str(self.lineEdit_sn.text())
        p = Product.get_by(sn=sn)
        if p is None:
            self.label_msg.setText(QtGui.QApplication.translate("MainWindow", "没有找到该产品", None, QtGui.QApplication.UnicodeUTF8))
        else:
            p.delete()    
            session.commit()
            self.label_msg.setText(QtGui.QApplication.translate("MainWindow", "产品删除成功", None, QtGui.QApplication.UnicodeUTF8))
            
        self.tableWidget.query()

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