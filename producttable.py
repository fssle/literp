# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from model import Product
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class ProductTable(QTableWidget):
    def __init__(self,parent=None):
        super(ProductTable,self).__init__(parent)

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
        self.setHorizontalHeaderItem(1,QTableWidgetItem(self.tr("品牌")))
        self.setHorizontalHeaderItem(2,QTableWidgetItem(self.tr("价格")))

        products = Product.query.all()
        self.setRowCount(len(products))
        row_id = 0
        for p in products:
            item_sn = QTableWidgetItem(p.sn)
            item_sn.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.setItem(row_id,0, item_sn)
            
            item_brand = QTableWidgetItem(p.brand)
            item_brand.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.setItem(row_id,1,item_brand)
            
            item_price = QTableWidgetItem("%.02f"%(p.price))
            item_price.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.setItem(row_id,2, item_price)
            
            row_id += 1
 
        self.setCurrentItem(self.item(0,0))

if __name__ == '__main__':
    import os
    
    app=QApplication(sys.argv)
    myqq=ProductTable()
    myqq.setWindowTitle("Products")
    myqq.query()
    myqq.show()
    app.exec_()