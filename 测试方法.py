from sys import argv
from PyQt5.Qt import *


class MyUi(QWidget):
    def __init__(self):
        super(MyUi, self).__init__()
        self.resize(400, 300)

        self.view = QTableView(self)
        self.view.setGeometry(0, 50, 400, 200)
        model = QStandardItemModel()
        model.setItem(0, 0, QStandardItem("张三"))
        model.setHorizontalHeaderLabels(['一', '二', '三'])
        self.view.setModel(model)

        btn = QPushButton('添加', self)
        btn.clicked.connect(self.slot_btn)

    def slot_btn(self):
        self.view.model().setItem(1, 1, QStandardItem("李四"))

if __name__ == '__main__':
    app = QApplication(argv)
    window = MyUi()
    window.show()
    exit(app.exec_())