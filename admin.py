# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

from archivetable import ArchiveTable
from datetime import *

class AdminWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(QtGui.QWidget, self).__init__(parent)

        self.setObjectName("tabSector")

        mainLayout = QtGui.QVBoxLayout()
        
        hLayoutRange = QtGui.QHBoxLayout()

        self.label_sdate = QtGui.QLabel(self)
        hLayoutRange.addWidget(self.label_sdate)

        self.dateEdit_sdate = QtGui.QDateEdit(self)
        self.dateEdit_sdate.setCalendarPopup(True)
        self.dateEdit_sdate.setDisplayFormat(QtCore.QString("yyyy-MM-dd"))
        self.dateEdit_sdate.setDate(QtCore.QDate.currentDate().addMonths(-1))

        hLayoutRange.addWidget(self.dateEdit_sdate)
  
        self.label_edate = QtGui.QLabel(self)
        hLayoutRange.addWidget(self.label_edate)
  
        self.dateEdit_edate = QtGui.QDateEdit(self)
        self.dateEdit_edate.setCalendarPopup(True)
        self.dateEdit_edate.setDisplayFormat(QtCore.QString("yyyy-MM-dd"))
        self.dateEdit_edate.setDate(QtCore.QDate.currentDate())
        hLayoutRange.addWidget(self.dateEdit_edate)
  
        mainLayout.addLayout(hLayoutRange)

        hLayoutQuery = QtGui.QHBoxLayout()

        self.label_sn = QtGui.QLabel(self)
        hLayoutQuery.addWidget(self.label_sn)

        self.lineEdit_sn = QtGui.QLineEdit(self)
        self.lineEdit_sn.setGeometry(QtCore.QRect(80, 0, 113, 20))
        hLayoutQuery.addWidget(self.lineEdit_sn)

        self.pushButtonQuery = QtGui.QPushButton(self)
        self.pushButtonQuery.setGeometry(QtCore.QRect(210, 0, 75, 23))
        hLayoutQuery.addWidget(self.pushButtonQuery)
    
        mainLayout.addLayout(hLayoutQuery)

        self.tableWidget = ArchiveTable(self)
        self.tableWidget.setGeometry(QtCore.QRect(320, 20, 261, 231))
        mainLayout.addWidget(self.tableWidget)

        hLayoutSummary = QtGui.QHBoxLayout()
        self.label_number = QtGui.QLabel(self)
        hLayoutSummary.addWidget(self.label_number)
        self.label_pay = QtGui.QLabel(self)
        hLayoutSummary.addWidget(self.label_pay)
        self.label_each = QtGui.QLabel(self)
        hLayoutSummary.addWidget(self.label_each)
        mainLayout.addLayout(hLayoutSummary)

        self.setLayout(mainLayout)

        self.retranslateUi()

        QtCore.QObject.connect(self.pushButtonQuery, QtCore.SIGNAL("pressed()"), self.doQuery)
        
    def retranslateUi(self):
        self.label_sdate.setText(QtGui.QApplication.translate("MainWindow", "开始日期", None, QtGui.QApplication.UnicodeUTF8))
        self.label_edate.setText(QtGui.QApplication.translate("MainWindow", "结束日期", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sn.setText(QtGui.QApplication.translate("MainWindow", "代码", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonQuery.setText(QtGui.QApplication.translate("MainWindow", "查询", None, QtGui.QApplication.UnicodeUTF8))
        self.label_number.setText(QtGui.QApplication.translate("MainWindow", "数量", None, QtGui.QApplication.UnicodeUTF8))
        self.label_each.setText(QtGui.QApplication.translate("MainWindow", "均价", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pay.setText(QtGui.QApplication.translate("MainWindow", "总价", None, QtGui.QApplication.UnicodeUTF8))
        
    def doQuery(self):
        print("called doQuery")
        sdate = self.dateEdit_sdate.dateTime().toPyDateTime()
        edate = self.dateEdit_edate.dateTime().toPyDateTime()
        sn = str(self.lineEdit_sn.text())
        """
        #date<=DateTime("2011-03-18 23:59:59") and
        #date>=DateTime("2011-02-18 00:00:00") and
        #sn="REDUCE"
        """
        cond = " date<=DateTime(\"" + edate.strftime("%Y-%m-%d") + " 23:59:59\") "
        cond += " and date>=DateTime(\"" + sdate.strftime("%Y-%m-%d") + " 00:00:00\") "
        if len(sn) >0:
            cond += " and sn=\"" + sn + "\" ";
        self.tableWidget.query(cond)

        self.label_number.setText(QtGui.QApplication.translate("MainWindow", "数量:"+str(self.tableWidget.total_number), None, QtGui.QApplication.UnicodeUTF8))
        self.label_each.setText(QtGui.QApplication.translate("MainWindow", "均价:%.02f"%(self.tableWidget.total_incoming/self.tableWidget.total_number), None, QtGui.QApplication.UnicodeUTF8))
        self.label_pay.setText(QtGui.QApplication.translate("MainWindow", "总价:%.02f"%(self.tableWidget.total_incoming), None, QtGui.QApplication.UnicodeUTF8))
        
#===============================================================================
#   Example
#===============================================================================
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QMainWindow, QApplication
    
    class ApplicationWindow(QMainWindow):
        def __init__(self):
            QMainWindow.__init__(self)
            self.widget = AdminWidget(self)
            self.widget.setFocus()
            self.setCentralWidget(self.widget)
           
    app = QApplication(sys.argv)
    win = ApplicationWindow()
    win.show()
    sys.exit(app.exec_())