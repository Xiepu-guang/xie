from sys import argv
from PyQt5.Qt import *
import cgitb

cgitb.enable(format='text')


class DigitDelegate(QItemDelegate):
    def __init__(self, parent):
        super(DigitDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        value = index.data(Qt.EditRole)
        if value != None and value.isdigit():
            painter.drawText(option.rect, Qt.AlignVCenter, value)


class Table(QWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        # 设置标题与初始大小
        self.setWindowTitle('QTableView表格视图的例子')
        self.resize(500, 300)

        # 设置数据层次结构，4行4列
        self.model = QStandardItemModel(4, 4)
        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3', '标题4'])

        # 实例化表格视图，设置模型为自定义的模型
        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        self.tableView.setItemDelegateForColumn(1, DigitDelegate(self.tableView))

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(argv)
    table = Table()
    table.show()
    exit(app.exec_())
