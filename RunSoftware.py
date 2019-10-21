import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
from Software import *
from Main_pushButton import *
from Main_pushButton_2 import *


#继承主窗口
class parentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.retranslateUi(self)
#清空主窗口的内容
    def qingkong(self):
        self.main_ui.tableWidget.clearContents()
        self.main_ui.tableWidget_2.clearContents()
        self.main_ui.tableWidget_3.clearContents()
        self.main_ui.tableWidget_4.clearContents()
        self.main_ui.tableWidget_5.clearContents()

#主窗口清空按钮字窗口
class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog()
        self.child.setupUi(self)
        self.child.retranslateUi(self)

#主窗口提交按钮字窗口
class childWindow_2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child_2=Ui_Dialog_2()
        self.child_2.setupUi(self)
        self.child_2.retranslateUi(self)

if __name__=='__main__':

    app=QApplication(sys.argv)
    # 调用窗口
    window = parentWindow()
    child = childWindow()
    child_2 = childWindow_2()
    shuju = []
    def dayin(self):
        for i in range(2):
            for j in range(1):
            item = window.main_ui.tableWidget_3.item(i, 0).text()


    # 通过pushButton将窗体关联
    # 主窗口清空按钮
    btn = window.main_ui.pushButton
    btn.clicked.connect(child.show)
    # 主窗口提交按钮
    btn_2 = window.main_ui.pushButton_2
    btn_2.clicked.connect(child_2.show)
    # 字窗口确认清空按钮
    btn_3 = child.child.pushButton
    btn_3.clicked.connect(window.qingkong)
    btn_4 = child_2.child_2.pushButton
    btn_4.clicked.connect(dayin)
    # 字窗口确认提交按钮


    # 修改主窗体属性
    # _translate = QtCore.QCoreApplication.translate
    # window.main_ui.pushButton.setText(_translate("MainWindow", "111"))

    window.show()
    sys.exit(app.exec_())

