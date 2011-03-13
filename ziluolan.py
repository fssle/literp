# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import ziluolan_rc

from trading import TradingWidget
from products import ProductsWidget
from admin import AdminWidget

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        
        self.setObjectName("MainWindow")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
        self.setDocumentMode(False)
        
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setObjectName("menubar")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(self)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        self.actionTrading = QtGui.QAction(self)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/image/icons/terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTrading.setIcon(icon3)
        
        self.actionProducts = QtGui.QAction(self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/image/icons/kchart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProducts.setIcon(icon2)

        self.actionAdmin = QtGui.QAction(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/image/icons/misc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdmin.setIcon(icon1)

        self.actionQuit = QtGui.QAction(self)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/image/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon5)
        
        self.actionQuit.setObjectName("actionQuit")
        self.menuView.addAction(self.actionTrading)
        self.menuView.addAction(self.actionProducts)
        self.menuView.addAction(self.actionAdmin)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionQuit)
        self.menubar.addAction(self.menuView.menuAction())
        self.toolBar.addAction(self.actionTrading)
        self.toolBar.addAction(self.actionProducts)
        self.toolBar.addAction(self.actionAdmin)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQuit)
        
        self.connect(self.actionTrading, QtCore.SIGNAL("triggered()"), self.doTabTrading)
        self.connect(self.actionProducts, QtCore.SIGNAL("triggered()"), self.doTabProducts)
        self.connect(self.actionAdmin, QtCore.SIGNAL("triggered()"), self.doTabAdmin)
        self.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), self.doQuit)

        self.tabWidget = QtGui.QTabWidget(self)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        
        self.tabTrading = TradingWidget(self.tabWidget)
        self.tabWidget.addTab(self.tabTrading, "")

        self.tabProducts = ProductsWidget(self.tabWidget)
        self.tabWidget.addTab(self.tabProducts, "")

        self.tabAdmin = AdminWidget(self.tabWidget)
        self.tabWidget.addTab(self.tabAdmin, "")
        self.tabWidget.setCurrentIndex(0)
        
        self.setCentralWidget(self.tabWidget)
    
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ziluolan", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "功能", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "工具条", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTrading.setText(QtGui.QApplication.translate("MainWindow", "交易", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProducts.setText(QtGui.QApplication.translate("MainWindow", "产品", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdmin.setText(QtGui.QApplication.translate("MainWindow", "后台", None, QtGui.QApplication.UnicodeUTF8))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTrading), QtGui.QApplication.translate("MainWindow", "交易", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProducts), QtGui.QApplication.translate("MainWindow", "产品", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAdmin), QtGui.QApplication.translate("MainWindow", "后台", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "退出", None, QtGui.QApplication.UnicodeUTF8))
        
    def doTabTrading(self):
        print("called doTabTrading")
        self.tabWidget.setCurrentIndex(0)

    def doTabProducts(self):
        print("called doTabProducts")
        self.tabWidget.setCurrentIndex(1)

    def doTabAdmin(self):
        print("called doTabAdmin")
        self.tabWidget.setCurrentIndex(2)

    def doQuit(self):
        print("called doQuit")
        self.close()

#===============================================================================
#   Example
#===============================================================================
if __name__ == "__main__":
    import sys
    
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    #window.showFullScreen()
    window.show()
    sys.exit(app.exec_())
