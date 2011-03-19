# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from model import Cart
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class CartTable(QTableWidget):
    def __init__(self,parent=None):
        super(CartTable,self).__init__(parent)

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

        self.query()

    def selectionChanged(self, new, old):
        print("selectionChanged", new, old)
        self.emit(SIGNAL("selectionChanged()"))
        QTableWidget.selectionChanged(self, new, old)

    def query(self):
        self.clear()
    
        self.setColumnCount(3)
        self.setHorizontalHeaderItem(0,QTableWidgetItem(self.tr("代码")))
        self.setHorizontalHeaderItem(1,QTableWidgetItem(self.tr("价格")))
        self.setHorizontalHeaderItem(2,QTableWidgetItem(self.tr("数量")))

        items = Cart.query.all()
        self.setRowCount(len(items))
        row_id = 0
        for t in items:
            item_sn = QTableWidgetItem(t.sn)
            item_sn.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.setItem(row_id,0, item_sn)
            
            item_price = QTableWidgetItem("%.02f"%(t.price))
            item_price.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.setItem(row_id,1, item_price)

            item_number = QTableWidgetItem("%d"%(t.number))
            item_number.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.setItem(row_id,2,item_number)
            
            row_id += 1
 
        self.setCurrentItem(self.item(0,0))

if __name__ == '__main__':
    import os
    
    app=QApplication(sys.argv)
    myqq=CartTable()
    myqq.setWindowTitle("Products")
    myqq.query()
    myqq.show()
    app.exec_()