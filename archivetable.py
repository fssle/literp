# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from model import Archive
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class ArchiveTable(QTableWidget):
    def __init__(self,parent=None):
        super(ArchiveTable,self).__init__(parent)

        self.horizontalHeader().setStretchLastSection(True)
        self.setSortingEnabled(True)
        self.sortByColumn(0, Qt.AscendingOrder)
        self.setShowGrid(True)
        self.verticalHeader().hide()
        self.verticalHeader().setDefaultSectionSize(20)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setAlternatingRowColors(True)
        self.verticalHeader().setResizeMode(QHeaderView.Fixed)

        self.setColumnCount(4)
        self.setHorizontalHeaderItem(0,QTableWidgetItem(self.tr("代码")))
        self.setHorizontalHeaderItem(1,QTableWidgetItem(self.tr("日期")))
        self.setHorizontalHeaderItem(2,QTableWidgetItem(self.tr("价格")))
        self.setHorizontalHeaderItem(3,QTableWidgetItem(self.tr("数量")))

        self.total_number = 0
        self.total_incoming = 0.0

    def selectionChanged(self, new, old):
        print("selectionChanged", new, old)
        self.emit(SIGNAL("selectionChanged()"))
        QTableWidget.selectionChanged(self, new, old)

    def query(self, cond):
        self.clear()

        self.setColumnCount(4)
        self.setHorizontalHeaderItem(0,QTableWidgetItem(self.tr("代码")))
        self.setHorizontalHeaderItem(1,QTableWidgetItem(self.tr("日期")))
        self.setHorizontalHeaderItem(2,QTableWidgetItem(self.tr("价格")))
        self.setHorizontalHeaderItem(3,QTableWidgetItem(self.tr("数量")))

        archives = Archive.query.filter(cond).all()
        self.setRowCount(len(archives))
        row_id = 0
        self.total_number = 0
        self.total_incoming = 0.0
        for ar in archives:
            item_sn = QTableWidgetItem(ar.sn)
            item_sn.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.setItem(row_id,0, item_sn)
            
            item_date = QTableWidgetItem(ar.date.strftime("%Y-%m-%d %H:%M:%S"))
            item_date.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.setItem(row_id,1,item_date)
            
            item_price = QTableWidgetItem("%.02f"%(ar.price))
            item_price.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.setItem(row_id,2, item_price)

            item_number = QTableWidgetItem("%.d"%(ar.number))
            item_number.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.setItem(row_id,3, item_number)
            
            row_id += 1
            if ar.price >0:
                self.total_number += ar.number
            self.total_incoming += ar.number * ar.price
 
        
if __name__ == '__main__':
    import os
    
    app=QApplication(sys.argv)
    myqq=ArchiveTable()
    myqq.setWindowTitle("Products")
    myqq.query("sn='REDUCE'")
    myqq.show()
    app.exec_()