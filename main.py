from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('untitled.ui', self)
        # self.show()


app = QApplication([])
window = MyGUI()
app.exec_()
