# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rv4.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
import recursos2
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(522, 399)
        MainWindow.setStyleSheet(_fromUtf8("background: rgb(170, 170, 127)"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.layoutWidget)
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.verticalLayout_2.addWidget(self.videoPlayer)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.open = QtGui.QPushButton(self.layoutWidget)
        self.open.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.open.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open.setIcon(icon)
        self.open.setIconSize(QtCore.QSize(25, 25))
        self.open.setObjectName(_fromUtf8("open"))
        self.horizontalLayout.addWidget(self.open)
        self.agregar = QtGui.QPushButton(self.layoutWidget)
        self.agregar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.agregar.setIcon(icon1)
        self.agregar.setIconSize(QtCore.QSize(25, 25))
        self.agregar.setObjectName(_fromUtf8("agregar"))
        self.horizontalLayout.addWidget(self.agregar)
        self.p2 = QtGui.QPushButton(self.layoutWidget)
        self.p2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.p2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p2.setIcon(icon2)
        self.p2.setIconSize(QtCore.QSize(25, 25))
        self.p2.setObjectName(_fromUtf8("p2"))
        self.horizontalLayout.addWidget(self.p2)
        self.p3 = QtGui.QPushButton(self.layoutWidget)
        self.p3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.p3.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p3.setIcon(icon3)
        self.p3.setIconSize(QtCore.QSize(25, 25))
        self.p3.setObjectName(_fromUtf8("p3"))
        self.horizontalLayout.addWidget(self.p3)
        self.p4 = QtGui.QPushButton(self.layoutWidget)
        self.p4.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p4.setIcon(icon4)
        self.p4.setIconSize(QtCore.QSize(25, 25))
        self.p4.setObjectName(_fromUtf8("p4"))
        self.horizontalLayout.addWidget(self.p4)
        self.p5 = QtGui.QPushButton(self.layoutWidget)
        self.p5.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/next2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p5.setIcon(icon5)
        self.p5.setIconSize(QtCore.QSize(25, 25))
        self.p5.setObjectName(_fromUtf8("p5"))
        self.horizontalLayout.addWidget(self.p5)
        self.p6=QtGui.QPushButton(self.layoutWidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/random2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p6.setIcon(icon6)
        self.p6.setIconSize(QtCore.QSize(25, 25))
        self.p6.setObjectName(_fromUtf8("p6"))
        self.horizontalLayout.addWidget(self.p6)

        self.volumeSlider = phonon.Phonon.VolumeSlider(self.layoutWidget)
        self.volumeSlider.setMaximumSize(QtCore.QSize(16777215, 23))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.horizontalLayout.addWidget(self.volumeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.seekSlider = phonon.Phonon.SeekSlider(self.layoutWidget)
        self.seekSlider.setMaximumSize(QtCore.QSize(16777215, 23))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.verticalLayout.addWidget(self.seekSlider)
        self.checkBox = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cooper Black"))
        font.setPointSize(8)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("background: rgb(200, 200, 200)")
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.listWidget = QtGui.QListWidget(self.splitter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Showcard Gothic"))
        font.setPointSize(8)
        font.setItalic(False)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet(_fromUtf8("background: rgb(200, 200, 200)"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Reproductor de Video", None))
        self.checkBox.setText(_translate("MainWindow", "Mostrar lista de reproducción", None))

from PyQt4 import phonon

