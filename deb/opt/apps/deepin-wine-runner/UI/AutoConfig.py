# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoConfig.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchTips = QtWidgets.QLabel(self.centralwidget)
        self.searchTips.setObjectName("searchTips")
        self.horizontalLayout.addWidget(self.searchTips)
        self.searchThings = QtWidgets.QLineEdit(self.centralwidget)
        self.searchThings.setObjectName("searchThings")
        self.horizontalLayout.addWidget(self.searchThings)
        self.saerchBotton = QtWidgets.QPushButton(self.centralwidget)
        self.saerchBotton.setObjectName("saerchBotton")
        self.horizontalLayout.addWidget(self.saerchBotton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.searchList = QtWidgets.QListView(self.centralwidget)
        self.searchList.setObjectName("searchList")
        self.verticalLayout_3.addWidget(self.searchList)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.runBotton = QtWidgets.QPushButton(self.centralwidget)
        self.runBotton.setObjectName("runBotton")
        self.horizontalLayout_2.addWidget(self.runBotton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 36))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.exitProgram = QtWidgets.QAction(MainWindow)
        self.exitProgram.setObjectName("exitProgram")
        self.help = QtWidgets.QAction(MainWindow)
        self.help.setObjectName("help")
        self.openFile = QtWidgets.QAction(MainWindow)
        self.openFile.setObjectName("openFile")
        self.menu.addAction(self.openFile)
        self.menu.addSeparator()
        self.menu.addAction(self.exitProgram)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自动部署脚本"))
        self.searchTips.setText(_translate("MainWindow", "搜索内容（为空代表显示所有内容）："))
        self.saerchBotton.setText(_translate("MainWindow", "搜索"))
        self.runBotton.setText(_translate("MainWindow", "部署此方案"))
        self.menu.setTitle(_translate("MainWindow", "程序"))
        self.about.setText(_translate("MainWindow", "关于"))
        self.exitProgram.setText(_translate("MainWindow", "退出程序"))
        self.help.setText(_translate("MainWindow", "帮助"))
        self.openFile.setText(_translate("MainWindow", "打开本地部署脚本"))

