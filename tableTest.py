# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
 
class MyTable(QTableWidget):
    def __init__(self,parent=None):
        super(MyTable,self).__init__(parent)
        self.setColumnCount(6)
        self.setRowCount(2)
        self.setItem(0,0,QTableWidgetItem(self.tr("Sex")))
        self.setItem(0,1,QTableWidgetItem(self.tr("Name")))
        self.setItem(0,2,QTableWidgetItem(self.tr("Birth")))
        self.setItem(0,3,QTableWidgetItem(self.tr("Role")))
        self.setItem(0,4,QTableWidgetItem(self.tr("Incoming")))
        self.setItem(0,5,QTableWidgetItem(self.tr("")))
        lbp1=QLabel()
        lbp1.setPixmap(QPixmap("image/4.gif"))
        self.setCellWidget(1,0,lbp1)
        twi1=QTableWidgetItem("Tom")
        self.setItem(1,1,twi1)
        dte1=QDateTimeEdit()
        dte1.setDateTime(QDateTime.currentDateTime())
        dte1.setDisplayFormat("yyyy/mm/dd")
        dte1.setCalendarPopup(True)
        self.setCellWidget(1,2,dte1)
        cbw=QComboBox()
        cbw.addItem("Worker")
        cbw.addItem("Famer")
        cbw.addItem("Doctor")
        cbw.addItem("Lawyer")
        cbw.addItem("Soldier")
        self.setCellWidget(1,3,cbw)
        sb1=QSpinBox()
        sb1.setRange(1000,10000)
        self.setCellWidget(1,4,sb1)
        btn=QPushButton()
        btn.setText("delete")
        self.setCellWidget(1,5,btn)
  
app=QApplication(sys.argv)
myqq=MyTable()
myqq.setWindowTitle("My Table")
myqq.show()
app.exec_()