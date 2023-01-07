# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(656, 639)
        self.actionDS1 = QAction(MainWindow)
        self.actionDS1.setObjectName(u"actionDS1")
        self.actionDS2 = QAction(MainWindow)
        self.actionDS2.setObjectName(u"actionDS2")
        self.actionDS3 = QAction(MainWindow)
        self.actionDS3.setObjectName(u"actionDS3")
        self.actionER = QAction(MainWindow)
        self.actionER.setObjectName(u"actionER")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_selectPath = QPushButton(self.centralwidget)
        self.pushButton_selectPath.setObjectName(u"pushButton_selectPath")
        self.pushButton_selectPath.setGeometry(QRect(520, 10, 91, 24))
        self.lineEdit_path = QLineEdit(self.centralwidget)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setGeometry(QRect(20, 10, 491, 21))
        self.pushButton_createSave = QPushButton(self.centralwidget)
        self.pushButton_createSave.setObjectName(u"pushButton_createSave")
        self.pushButton_createSave.setGeometry(QRect(290, 120, 101, 51))
        self.textEdit_saveName = QTextEdit(self.centralwidget)
        self.textEdit_saveName.setObjectName(u"textEdit_saveName")
        self.textEdit_saveName.setGeometry(QRect(290, 60, 361, 51))
        font = QFont()
        font.setPointSize(26)
        self.textEdit_saveName.setFont(font)
        self.pushButton_delectSave = QPushButton(self.centralwidget)
        self.pushButton_delectSave.setObjectName(u"pushButton_delectSave")
        self.pushButton_delectSave.setGeometry(QRect(560, 120, 91, 51))
        self.listWidget_saveFile = QListWidget(self.centralwidget)
        self.listWidget_saveFile.setObjectName(u"listWidget_saveFile")
        self.listWidget_saveFile.setGeometry(QRect(20, 60, 256, 531))
        self.pushButton_replaceSave = QPushButton(self.centralwidget)
        self.pushButton_replaceSave.setObjectName(u"pushButton_replaceSave")
        self.pushButton_replaceSave.setGeometry(QRect(290, 180, 361, 61))
        font1 = QFont()
        font1.setPointSize(18)
        self.pushButton_replaceSave.setFont(font1)
        self.pushButton_replaceSave.setStyleSheet(u"")
        self.progressBar_autoSave = QProgressBar(self.centralwidget)
        self.progressBar_autoSave.setObjectName(u"progressBar_autoSave")
        self.progressBar_autoSave.setGeometry(QRect(290, 260, 361, 23))
        self.progressBar_autoSave.setValue(24)
        self.pushButton_replaceSave_auto = QPushButton(self.centralwidget)
        self.pushButton_replaceSave_auto.setObjectName(u"pushButton_replaceSave_auto")
        self.pushButton_replaceSave_auto.setGeometry(QRect(290, 410, 361, 61))
        self.pushButton_replaceSave_auto.setFont(font1)
        self.pushButton_replaceSave_auto.setStyleSheet(u"")
        self.pushButton_replaceSave_origin = QPushButton(self.centralwidget)
        self.pushButton_replaceSave_origin.setObjectName(u"pushButton_replaceSave_origin")
        self.pushButton_replaceSave_origin.setGeometry(QRect(290, 480, 361, 61))
        self.pushButton_replaceSave_origin.setFont(font1)
        self.pushButton_replaceSave_origin.setStyleSheet(u"")
        self.pushButton_openLocalSave = QPushButton(self.centralwidget)
        self.pushButton_openLocalSave.setObjectName(u"pushButton_openLocalSave")
        self.pushButton_openLocalSave.setGeometry(QRect(290, 550, 361, 61))
        self.pushButton_openLocalSave.setFont(font1)
        self.pushButton_openLocalSave.setStyleSheet(u"")
        self.pushButton_renameSave = QPushButton(self.centralwidget)
        self.pushButton_renameSave.setObjectName(u"pushButton_renameSave")
        self.pushButton_renameSave.setGeometry(QRect(430, 120, 101, 51))
        self.pushButton_openPath = QPushButton(self.centralwidget)
        self.pushButton_openPath.setObjectName(u"pushButton_openPath")
        self.pushButton_openPath.setGeometry(QRect(620, 10, 31, 24))
        self.lcdNumber_autosave = QLCDNumber(self.centralwidget)
        self.lcdNumber_autosave.setObjectName(u"lcdNumber_autosave")
        self.lcdNumber_autosave.setGeometry(QRect(290, 290, 351, 41))
        self.pushButton_startAutoSave = QPushButton(self.centralwidget)
        self.pushButton_startAutoSave.setObjectName(u"pushButton_startAutoSave")
        self.pushButton_startAutoSave.setGeometry(QRect(290, 340, 361, 61))
        self.pushButton_startAutoSave.setFont(font1)
        self.pushButton_startAutoSave.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 656, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionDS1)
        self.menu.addAction(self.actionDS2)
        self.menu.addAction(self.actionDS3)
        self.menu.addAction(self.actionER)

        self.retranslateUi(MainWindow)
        self.pushButton_selectPath.clicked.connect(MainWindow.select_save_directory)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Souls\u5b58\u6863\u7ba1\u7406\u5de5\u5177", None))
        self.actionDS1.setText(QCoreApplication.translate("MainWindow", u"DarkSouls1", None))
        self.actionDS2.setText(QCoreApplication.translate("MainWindow", u"DarkSouls2", None))
        self.actionDS3.setText(QCoreApplication.translate("MainWindow", u"DarkSouls3", None))
        self.actionER.setText(QCoreApplication.translate("MainWindow", u"EldenRing", None))
        self.pushButton_selectPath.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5b58\u6863\u4f4d\u7f6e", None))
        self.pushButton_createSave.setText(QCoreApplication.translate("MainWindow", u"\u5907\u4efd\u5b58\u6863", None))
        self.textEdit_saveName.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
        self.pushButton_delectSave.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5b58\u6863", None))
#if QT_CONFIG(tooltip)
        self.pushButton_replaceSave.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton_replaceSave.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_replaceSave.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u5b58\u6863", None))
#if QT_CONFIG(tooltip)
        self.progressBar_autoSave.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u81ea\u52a8\u5b58\u6863\u8fdb\u5ea6\u6761</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_replaceSave_auto.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton_replaceSave_auto.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_replaceSave_auto.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u81ea\u52a8\u5b58\u6863", None))
#if QT_CONFIG(tooltip)
        self.pushButton_replaceSave_origin.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u66ff\u6362\u4e3a\u6253\u5f00\u8f6f\u4ef6\u65f6\u81ea\u52a8\u5907\u4efd\u7684\u5b58\u6863</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton_replaceSave_origin.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_replaceSave_origin.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u521d\u59cb\u5b58\u6863", None))
#if QT_CONFIG(tooltip)
        self.pushButton_openLocalSave.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u66ff\u6362\u4e3a\u6253\u5f00\u8f6f\u4ef6\u65f6\u81ea\u52a8\u5907\u4efd\u7684\u5b58\u6863</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton_openLocalSave.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_openLocalSave.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5b58\u6863\u6587\u4ef6\u5939", None))
        self.pushButton_renameSave.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u547d\u540d", None))
        self.pushButton_openPath.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(tooltip)
        self.lcdNumber_autosave.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u81ea\u52a8\u4fdd\u5b58\u7684\u65f6\u95f4</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_startAutoSave.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton_startAutoSave.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_startAutoSave.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u81ea\u52a8\u5b58\u6863", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5207\u6362", None))
    # retranslateUi

