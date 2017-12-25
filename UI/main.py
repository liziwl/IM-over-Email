from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from UI.login import Ui_Login


class mywindow(QtWidgets.QWidget, Ui_Login):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def try_login(self):
        pass


app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
