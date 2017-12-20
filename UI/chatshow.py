import sys
from PyQt5 import QtWebChannel
from PyQt5.QtWidgets import *
from chat import *


class chatwin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.map_ui = Ui_MainWindow()  # The name of my top level object is MainWindow
        self.map_ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = chatwin()
    ex.show()
    sys.exit(app.exec_())