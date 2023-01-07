import sys
import os
import shutil
from threading import Thread
import time

from PySide6 import QtCore,QtWidgets,QtGui

import ui_untitled
from config import Config

class AutoSaveThread(QtCore.QObject):
    autoSave = QtCore.Signal(str,bool,int)

    def __init__(self):
        super().__init__()

    def autoSaveSignal(self):
        config = Config()
        if not config.config[config.config['default']['game']]['path'] == "":
            while True:
                self.autoSave.emit(QtCore.QTime.currentTime().toString('hh:mm'),True,300)
                for step in range(299):
                    self.autoSave.emit(QtCore.QTime.currentTime().toString('hh:mm'),False,step)
                    time.sleep(1)
class SaveManager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_untitled.Ui_MainWindow()
        self.ui.setupUi(self)
        self.config = Config()

        self.game = self.config.config['default']['game']
        self.gameSavePath = self.config.config[self.game]['path']
        self.localSave = os.path.join("saves",self.game)
        self.saveName = self.config.config[self.game]['savename']

        self.ui.lineEdit_path.setText(self.config.config[self.game]['path'])
        self.setupThread()
        #初始备份
        try:
            if not self.gameSavePath == "":
                self.backupSave(name="origin")
        except:
            pass
        self.init_listWidget()

        #备份存档
        self.ui.pushButton_createSave.clicked.connect(self.backupSave)
        #存档名
        self.ui.listWidget_saveFile.itemSelectionChanged.connect(self.currentSelectSave)
        #重命名
        self.ui.pushButton_renameSave.clicked.connect(self.renameSave)
        #删除
        self.ui.pushButton_delectSave.clicked.connect(self.removeSave)
        #恢复存档
        self.ui.pushButton_replaceSave.clicked.connect(self.recoverySave)
        #恢复初始存档
        self.ui.pushButton_replaceSave_origin.clicked.connect(lambda name:self.recoverySave(name="origin"))
        #打开游戏存档文件夹
        self.ui.pushButton_openPath.clicked.connect(lambda path:self.openDir(self.gameSavePath))
        #打开本地备份存档文件夹
        self.ui.pushButton_openLocalSave.clicked.connect(lambda path:self.openDir(os.path.join("saves",self.game)))
        #进度条/自动保存
        self.ui.progressBar_autoSave.setValue(0)
        self.ui.progressBar_autoSave.setMaximum(300)
        self.ui.progressBar_autoSave.setMinimum(0)
        #恢复自动保存
        self.ui.pushButton_replaceSave_auto.clicked.connect(lambda name:self.recoverySave(name="autosave"))
        #切换游戏
        self.ui.actionDS1.triggered.connect(self.selectDs1)
        self.ui.actionDS2.triggered.connect(self.selectDs2)
        self.ui.actionDS3.triggered.connect(self.selectDs3)
        self.ui.actionER.triggered.connect(self.selectER)

    #切换魂1
    def selectDs1(self):
        self.game = "darksouls1"
        self.config.config['default']['game'] = self.game
        self.localSave = os.path.join("saves",self.game)
        self.saveName = self.config.config[self.game]['savename']
        self.config.writeReplace()

        self.ui.lineEdit_path.clear()
        self.init_listWidget()

    #切换魂2
    def selectDs2(self):
        self.game = "darksouls2"
        self.config.config['default']['game'] = self.game
        self.localSave = os.path.join("saves",self.game)
        self.saveName = self.config.config[self.game]['savename']
        self.config.writeReplace()

        self.ui.lineEdit_path.clear()
        self.init_listWidget()

    #切换魂3
    def selectDs3(self):
        self.game = "darksouls3"
        self.config.config['default']['game'] = self.game
        self.localSave = os.path.join("saves",self.game)
        self.saveName = self.config.config[self.game]['savename']
        self.config.writeReplace()

        self.ui.lineEdit_path.clear()
        self.init_listWidget()

    #切换埃尔登法环
    def selectER(self):
        self.game = "eldenring"
        self.config.config['default']['game'] = self.game
        self.localSave = os.path.join("saves",self.game)
        self.saveName = self.config.config[self.game]['savename']
        self.config.writeReplace()

        self.ui.lineEdit_path.clear()
        self.init_listWidget()

    #自动备份线程
    def autoSave_slot(self,time,save,step):
        try:
            if save is True:
                self.backupSave(name="autosave")
                self.ui.lcdNumber_autosave.display(time)
                self.ui.progressBar_autoSave.setValue(step)
            else:
                self.ui.progressBar_autoSave.setValue(step)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,"开启自动备份失败",str(e))
    def setupThread(self):
        self.thread1 = QtCore.QThread(self)
        self.autoSaveThread = AutoSaveThread()
        self.autoSaveThread.moveToThread(self.thread1)

        self.autoSaveThread.autoSave.connect(self.autoSave_slot)
        self.ui.pushButton_startAutoSave.clicked.connect(self.startAutoSave)
        self.ui.pushButton_startAutoSave.clicked.connect(self.autoSaveThread.autoSaveSignal)
    def startAutoSave(self):
        self.thread1.start()



    #初始化存档显示框
    def init_listWidget(self):
        self.ui.listWidget_saveFile.clear()
        local_save_dir = QtCore.QDir(os.path.join("saves",self.game))
        self.ui.listWidget_saveFile.addItems(local_save_dir.entryList(["*.sl2"]))

    #备份存档
    def backupSave(self,name=""):
        try:
            if name is False:
                name = self.ui.textEdit_saveName.toPlainText()
            shutil.copyfile(os.path.join(self.gameSavePath,self.saveName),os.path.join(self.localSave,name+".sl2"))
            self.init_listWidget()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,"备份文件失败",str(e))

    #当前选择存档
    def currentSelectSave(self):
        try:
            savename = self.ui.listWidget_saveFile.selectedItems()[0].text().split(".sl2")[0]
            self.ui.textEdit_saveName.setText(savename)
        except:
            pass

    #选择存档文件目录
    def select_save_directory(self):
        save_path = QtWidgets.QFileDialog.getExistingDirectory(self)
        if not save_path == "":
            self.config.config[self.game]['path'] = save_path
            self.gameSavePath = save_path
            self.config.writeReplace()
            self.ui.lineEdit_path.setText(save_path)
            self.backupSave(name="origin")
    #重命名
    def renameSave(self):
        try:
            newName = self.ui.textEdit_saveName.toPlainText()
            oldName = self.ui.listWidget_saveFile.currentItem().text()
            shutil.move(os.path.join(self.localSave,oldName),os.path.join(self.localSave,newName+".sl2"))
            self.init_listWidget()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,"重命名失败",str(e))

    #删除
    def removeSave(self):
        try:
            name = self.ui.textEdit_saveName.toPlainText()
            os.remove(os.path.join(self.localSave,name+".sl2"))
            self.init_listWidget()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,"删除失败",str(e))

    #恢复
    def recoverySave(self,name=""):
        try:
            if name is False:
                name = self.ui.textEdit_saveName.toPlainText()
            shutil.copyfile(os.path.join(self.localSave,name+".sl2"),os.path.join(self.gameSavePath,self.saveName))
            self.init_listWidget()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,"备份文件失败",str(e))

    #打开文件地址
    def openDir(self,path):
        try:
            os.startfile(path)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,"打开文件夹失败",str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = SaveManager()
    widget.show()
    sys.exit(app.exec())