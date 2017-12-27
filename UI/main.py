from UI.login import *
from UI.chat import *


class loginwin(QtWidgets.QWidget, Ui_Login):
    def __init__(self):
        super(loginwin, self).__init__()
        self.setupUi(self)
        self.chat_win = chatwin()

    def try_login(self):
        if not self.chat_win.isVisible():
            self.chat_win.show()
            self.close()

app = QtWidgets.QApplication(sys.argv)
ex = loginwin()
ex.show()
sys.exit(app.exec_())
