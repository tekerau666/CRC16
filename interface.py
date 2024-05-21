# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(606, 464)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chatGroupBox = QGroupBox(self.centralwidget)
        self.chatGroupBox.setObjectName(u"chatGroupBox")
        self.chatGroupBox.setEnabled(True)
        self.chatGroupBox.setGeometry(QRect(0, 0, 601, 431))
        self.sendButton = QPushButton(self.chatGroupBox)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(190, 280, 181, 81))
        self.messageLineEdit = QLineEdit(self.chatGroupBox)
        self.messageLineEdit.setObjectName(u"messageLineEdit")
        self.messageLineEdit.setGeometry(QRect(20, 100, 221, 41))
        self.kolliziaLineEdit = QLineEdit(self.chatGroupBox)
        self.kolliziaLineEdit.setObjectName(u"kolliziaLineEdit")
        self.kolliziaLineEdit.setGeometry(QRect(20, 200, 221, 41))
        self.crcLineEdit = QLineEdit(self.chatGroupBox)
        self.crcLineEdit.setObjectName(u"crcLineEdit")
        self.crcLineEdit.setGeometry(QRect(310, 100, 221, 41))
        self.crcLineEdit_2 = QLineEdit(self.chatGroupBox)
        self.crcLineEdit_2.setObjectName(u"crcLineEdit_2")
        self.crcLineEdit_2.setGeometry(QRect(310, 200, 221, 41))
        self.label_5 = QLabel(self.chatGroupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 80, 91, 16))
        self.label_6 = QLabel(self.chatGroupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(310, 80, 49, 16))
        self.label_7 = QLabel(self.chatGroupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(310, 180, 49, 16))
        self.label_8 = QLabel(self.chatGroupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 180, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 606, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.chatGroupBox.setTitle("")
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c CRC \u0438 \u043a\u043e\u043b\u0438\u0437\u0438\u044e", None))
        self.messageLineEdit.setText("")
        self.messageLineEdit.setPlaceholderText("")
        self.kolliziaLineEdit.setText("")
        self.kolliziaLineEdit.setPlaceholderText("")
        self.crcLineEdit.setText("")
        self.crcLineEdit.setPlaceholderText("")
        self.crcLineEdit_2.setText("")
        self.crcLineEdit_2.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CRC16", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CRC16", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0437\u0438\u044f", None))
    # retranslateUi

