# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

from carttable import CartTable
from model import *
from datetime import *

class TradingWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(QtGui.QWidget, self).__init__(parent)

        self.setObjectName("tabTrading")

        mainLayout = QtGui.QHBoxLayout()
        
        vLayoutLeft = QtGui.QVBoxLayout()

        hLayoutSN = QtGui.QHBoxLayout()

        self.label_sn = QtGui.QLabel(self)
        hLayoutSN.addWidget(self.label_sn)

        self.lineEdit_sn = QtGui.QLineEdit(self)
        self.lineEdit_sn.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutSN.addWidget(self.lineEdit_sn)

        self.pushButtonQuery = QtGui.QPushButton(self)
        self.pushButtonQuery.setGeometry(QtCore.QRect(210, 0, 75, 23))
        hLayoutSN.addWidget(self.pushButtonQuery)
    
        vLayoutLeft.addLayout(hLayoutSN)
        
        self.label_brand = QtGui.QLabel(self)
        vLayoutLeft.addWidget(self.label_brand)

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

        self.label_msg = QtGui.QLabel(self)
        vLayoutLeft.addWidget(self.label_msg)

        hLayoutCmd = QtGui.QHBoxLayout()
        
        self.pushButtonUpdate = QtGui.QPushButton(self)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(210, 0, 75, 23))
        hLayoutCmd.addWidget(self.pushButtonUpdate)

        self.pushButtonDel = QtGui.QPushButton(self)
        self.pushButtonDel.setGeometry(QtCore.QRect(210, 0, 75, 23))
        hLayoutCmd.addWidget(self.pushButtonDel)

        vLayoutLeft.addLayout(hLayoutCmd)

        mainLayout.addLayout(vLayoutLeft)

        vLayoutRight = QtGui.QVBoxLayout()

        self.pushButtonEmpty = QtGui.QPushButton(self)
        self.pushButtonEmpty.setGeometry(QtCore.QRect(210, 0, 75, 23))
        vLayoutRight.addWidget(self.pushButtonEmpty)

        self.tableWidget = CartTable(self)
        self.tableWidget.setGeometry(QtCore.QRect(320, 20, 261, 231))
        vLayoutRight.addWidget(self.tableWidget)

        
        hLayoutPay = QtGui.QHBoxLayout()
        
        self.label_pay = QtGui.QLabel(self)
        hLayoutPay.addWidget(self.label_pay)

        self.label_pay_number = QtGui.QLabel(self)
        hLayoutPay.addWidget(self.label_pay_number)

        vLayoutRight.addLayout(hLayoutPay) 

        hLayoutReduce = QtGui.QHBoxLayout()
        self.label_cash = QtGui.QLabel(self)
        hLayoutReduce.addWidget(self.label_cash)

        self.lineEdit_cash = QtGui.QLineEdit(self)
        self.lineEdit_cash.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutReduce.addWidget(self.lineEdit_cash)

        self.label_reduce = QtGui.QLabel(self)
        hLayoutReduce.addWidget(self.label_reduce)

        self.lineEdit_reduce = QtGui.QLineEdit(self)
        self.lineEdit_reduce.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutReduce.addWidget(self.lineEdit_reduce)

        vLayoutRight.addLayout(hLayoutReduce) 

        hLayoutChange = QtGui.QHBoxLayout()
        
        self.pushButtonCheckout = QtGui.QPushButton(self)
        self.pushButtonCheckout.setGeometry(QtCore.QRect(210, 0, 75, 23))
        hLayoutChange.addWidget(self.pushButtonCheckout)

        self.label_change = QtGui.QLabel(self)
        hLayoutChange.addWidget(self.label_change)

        self.label_change_number = QtGui.QLabel(self)
        hLayoutChange.addWidget(self.label_change_number)

        vLayoutRight.addLayout(hLayoutChange) 

        self.pushButtonArchive = QtGui.QPushButton(self)
        self.pushButtonArchive.setGeometry(QtCore.QRect(210, 0, 75, 23))
        vLayoutRight.addWidget(self.pushButtonArchive)

        mainLayout.addLayout(vLayoutRight)

        self.setLayout(mainLayout)

        self.retranslateUi()

        self.label_pay_number.setText("0.00")
        self.lineEdit_cash.setText("0.00")
        self.lineEdit_reduce.setText("0.00")
        self.label_change_number.setText("0.00")

        QtCore.QObject.connect(self.pushButtonQuery, QtCore.SIGNAL("pressed()"), self.doQuery)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("selectionChanged()"), self.tableWidget_selectionChanged)
        QtCore.QObject.connect(self.pushButtonUpdate, QtCore.SIGNAL("pressed()"), self.doCmdUpdate)
        QtCore.QObject.connect(self.pushButtonDel, QtCore.SIGNAL("pressed()"), self.doCmdDel)
        QtCore.QObject.connect(self.pushButtonCheckout, QtCore.SIGNAL("pressed()"), self.doCmdCheckout)
        QtCore.QObject.connect(self.pushButtonArchive, QtCore.SIGNAL("pressed()"), self.doCmdArchive)
        QtCore.QObject.connect(self.pushButtonEmpty, QtCore.SIGNAL("pressed()"), self.doCmdEmpty)

    def retranslateUi(self):
        self.label_brand.setText(QtGui.QApplication.translate("MainWindow", "品牌", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sn.setText(QtGui.QApplication.translate("MainWindow", "代码", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonQuery.setText(QtGui.QApplication.translate("MainWindow", "查询", None, QtGui.QApplication.UnicodeUTF8))
        self.label_image.setText(QtGui.QApplication.translate("MainWindow", "图片没找到", None, QtGui.QApplication.UnicodeUTF8))
        self.label_price.setText(QtGui.QApplication.translate("MainWindow", "单价", None, QtGui.QApplication.UnicodeUTF8))
        self.label_number.setText(QtGui.QApplication.translate("MainWindow", "数量", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUpdate.setText(QtGui.QApplication.translate("MainWindow", "更新", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDel.setText(QtGui.QApplication.translate("MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pay.setText(QtGui.QApplication.translate("MainWindow", "总款", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cash.setText(QtGui.QApplication.translate("MainWindow", "已付", None, QtGui.QApplication.UnicodeUTF8))
        self.label_reduce.setText(QtGui.QApplication.translate("MainWindow", "折扣", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCheckout.setText(QtGui.QApplication.translate("MainWindow", "结账", None, QtGui.QApplication.UnicodeUTF8))
        self.label_change.setText(QtGui.QApplication.translate("MainWindow", "找零:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonArchive.setText(QtGui.QApplication.translate("MainWindow", "存档", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEmpty.setText(QtGui.QApplication.translate("MainWindow", "清空", None, QtGui.QApplication.UnicodeUTF8))
        
    def doQuery(self):
        print("called doQuery")
        sn = str(self.lineEdit_sn.text())
        p = Product.query.filter_by(sn=sn).one()
        if p is None:
            self.lineEdit_price.setText("0.00")
            self.label_brand.setText("")
            self.label_msg.setText(QtGui.QApplication.translate("MainWindow", "没有找到该产品", None, QtGui.QApplication.UnicodeUTF8))
        else:
            self.lineEdit_price.setText("%0.2f"%(p.price))
            self.label_brand.setText(p.brand)
            self.label_image.setPixmap(QtGui.QPixmap("image/%s.jpg"%(sn)))
        
    def doCmdUpdate(self):
        print("called doCmdUpdate")
        sn = str(self.lineEdit_sn.text())
        t = Cart.get_by(sn=sn)
        if t is None:
            price=float(self.lineEdit_price.text())
            number=int(self.lineEdit_number.text())
            Cart(sn=sn, price=price, number=number)
            session.commit()
            self.label_msg.setText(QtGui.QApplication.translate("MainWindow", "物品添加成功", None, QtGui.QApplication.UnicodeUTF8))
        else:
            t.sn=sn
            t.price=float(self.lineEdit_price.text())
            t.number=int(self.lineEdit_number.text())
            session.commit()
            self.label_msg.setText(QtGui.QApplication.translate("MainWindow", "物品更新成功", None, QtGui.QApplication.UnicodeUTF8))
            
        self.tableWidget.query()
        self.doCmdCheckout()
        
    def doCmdDel(self):
        print("called doCmdDel")
        sn = str(self.lineEdit_sn.text())
        t = Cart.get_by(sn=sn)
        if t is None:
            self.label_msg.setText(QtGui.QApplication.translate("MainWindow", "没有找到该物品", None, QtGui.QApplication.UnicodeUTF8))
            
        else:
            t.delete()    
            session.commit()
            self.label_msg.setText(QtGui.QApplication.translate("MainWindow", "物品删除成功", None, QtGui.QApplication.UnicodeUTF8))
            
        self.tableWidget.query()
        self.doCmdCheckout()
        
    def doCmdCheckout(self):
        print("called doCmdCheckout")
        items = Cart.query.all()
        total = 0.0
        for t in items:
            print(repr(t), t.price, t.number)
            total += t.price*t.number
        self.label_pay_number.setText("%.02f"%(total))
        cash = float(self.lineEdit_cash.text())
        reduce = float(self.lineEdit_reduce.text())
        change = cash-reduce-total
        self.label_change_number.setText("%.02f"%(change))
   
    def doCmdArchive(self):
        print("called doCmdArchive")
        items = Cart.query.all()
        dt_now = datetime.now()
        total = 0.0
        for t in items:
            Archive(sn=t.sn, price=t.price, number=t.number, date = dt_now)
            t.delete()
            total += t.price*t.number
        if total > 0:
            reduce = float(self.lineEdit_reduce.text())
            if reduce > 0:
                Archive(sn="REDUCE", price=-reduce, number=1, date = dt_now)
            session.commit()
        else:
            self.label_msg.setText(QtGui.QApplication.translate("MainWindow", "没有任何物品", None, QtGui.QApplication.UnicodeUTF8))  
        
    def doCmdEmpty(self):
        print("called doCmdEmpty")
        items = Cart.query.all()
        for t in items:
            t.delete()
        session.commit()
        self.tableWidget.query()
        self.doCmdCheckout()
             
    def tableWidget_selectionChanged(self):
        print("called tblWidget_selectionChanged")
        row=self.tableWidget.currentRow()
        sn = str(self.tableWidget.item(row,0).text())
        print(sn)
        t = Cart.get_by(sn=sn)
        if t is None:
            self.label_msg.setText(QtGui.QApplication.translate("MainWindow", "没有找到该物品", None, QtGui.QApplication.UnicodeUTF8))  
        else:
            self.lineEdit_sn.setText(t.sn)
            self.lineEdit_price.setText("%.02f"%(t.price))
            self.lineEdit_number.setText("%d"%(t.number))
            
            
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