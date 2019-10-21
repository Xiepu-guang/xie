import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
from Softwareshiyan import *
from Main_pushButton import *
from Main_pushButton_2 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase , QSqlQuery,QSqlTableModel
import cgitb
from la import DigitDelegate
cgitb.enable(format='text')
#继承主窗口
class parentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.retranslateUi(self)

    #建立tableView数据库
    def initializeModel(self,model):
        model.setTable('Basic_Information')
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.select()

    def createView(self,model):
        view = self.main_ui.tableView
        view.setModel(model)
        return view

    # 建立tableView_2数据库
    def initializeModel_2(self, model):
        model.setTable('Vital_Signs')
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.select()

    def createView_2(self, model):
        view = self.main_ui.tableView_2
        view.setModel(model)
        return view

    # 建立tableView_3数据库
    def initializeModel_3(self, model):
        model.setTable('TI')
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.select()

    def createView_3(self, model):
        view = self.main_ui.tableView_3
        view.setModel(model)
        return view

    # 建立tableView_4数据库
    def initializeModel_4(self, model):
        model.setTable('GCS')
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.select()

    def createView_4(self, model):
        view = self.main_ui.tableView_4
        view.setModel(model)
        return view

    # 建立tableView_5数据库
    def initializeModel_5(self, model):
        model.setTable('Time')
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.select()

    def createView_5(self, model):
        view = self.main_ui.tableView_5
        view.setModel(model)
        return view

    #添加一行
    def addrow(self):
        model.insertRows(model.rowCount(), 1)
        model_2.insertRows(model_2.rowCount(), 1)
        model_3.insertRows(model_3.rowCount(), 1)
        model_4.insertRows(model_4.rowCount(), 1)
        model_5.insertRows(model_5.rowCount(), 1)

    #删除一行
    def delrow(self):
        model.removeRow(view1.currentIndex().row())
        model_2.removeRow(view2.currentIndex().row())
        model_3.removeRow(view3.currentIndex().row())
        model_4.removeRow(view4.currentIndex().row())
        model_5.removeRow(view5.currentIndex().row())

    #清空所有表格的内容
    def qingkong(self):
        for i in range(10):
            model.removeRow(i)
            model_2.removeRow(i)
            model_3.removeRow(i)
            model_4.removeRow(i)
            model_5.removeRow(i)
            window.main_ui.label.clear()
            window.main_ui.label_2.clear()

     # 将表格所有内容上传到数据库
    def tijiao(self):
        model.submitAll()
        model_2.submitAll()
        model_3.submitAll()
        model_4.submitAll()
        model_5.submitAll()

    # 加载伤情图片
    def openimage(self):
        # 打开文件路径
        # 设置文件扩展名过滤,注意用双分号间隔
        imgName, imgType = QFileDialog.getOpenFileName(self,
                                                       "创伤",
                                                       "",
                                                       " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        print(imgName)
        # 利用qlabel显示图片
        jpg = QtGui.QPixmap(imgName).scaled(self.main_ui.label.width(), self.main_ui.label.height())
        self.main_ui.label.setPixmap(jpg)

    # 加载心电图
    def openimage_2(self):
        # 打开文件路径
        # 设置文件扩展名过滤,注意用双分号间隔
        imgName, imgType = QFileDialog.getOpenFileName(self,
                                                       "心电图",
                                                       "",
                                                       " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        print(imgName)
        # 利用qlabel显示图片
        jpg = QtGui.QPixmap(imgName).scaled(self.main_ui.label_2.width(), self.main_ui.label_2.height())
        self.main_ui.label_2.setPixmap(jpg)

    #当前时间
    def currenttime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.main_ui.label_3.setText(timeDisplay)

    #填入时间
    def tianru(self):
        r = view5.currentIndex().row()
        c = view5.currentIndex().column()
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        model_5.setData(model_5.index(r,c),timeDisplay)
        #print(model_5.index(0,0).data())
    #限制表中数据类型
    def jianyan(self):
        view1.setItemDelegateForColumn()
        #if model.itemData()

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
    btn_4.clicked.connect(window.tijiao)
    # 添加一行
    btn_5 = window.main_ui.pushButton_4
    btn_5.clicked.connect(window.addrow)
    # 删除一行
    btn_6 = window.main_ui.pushButton_3
    btn_6.clicked.connect(window.delrow)
    # 打开创伤图片
    btn_7 = window.main_ui.pushButton_5
    btn_7.clicked.connect(window.openimage)
    # 打开心电图
    btn_8 = window.main_ui.pushButton_6
    btn_8.clicked.connect(window.openimage_2)
    #当前时间
    timer = QTimer()
    timer.timeout.connect(window.currenttime)
    timer.start()
    # 填入时间
    btn_10 = window.main_ui.pushButton_8
    btn_10.clicked.connect(window.tianru)

    #打开数据库
    #将数据库中的数据同步到表中
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')
    model = QSqlTableModel()
    model_2 = QSqlTableModel()
    model_3 = QSqlTableModel()
    model_4 = QSqlTableModel()
    model_5 = QSqlTableModel()
    view1 = window.createView(model)
    view2 = window.createView_2(model_2)
    view3 = window.createView_3(model_3)
    view4 = window.createView_4(model_4)
    view5 = window.createView_5(model_5)
    window.initializeModel(model)
    window.createView(model)
    window.initializeModel_2(model_2)
    window.createView_2(model_2)
    window.initializeModel_3(model_3)
    window.createView_3(model_3)
    window.initializeModel_4(model_4)
    window.createView_4(model_4)
    window.initializeModel_5(model_5)
    window.createView_5(model_5)
    view1.setItemDelegateForColumn(1, DigitDelegate(view1))

    # 修改主窗体属性
    # _translate = QtCore.QCoreApplication.translate
    # window.main_ui.pushButton.setText(_translate("MainWindow", "111"))

    window.show()
    sys.exit(app.exec_())
