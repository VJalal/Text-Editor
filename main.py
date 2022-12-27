
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.show()
        self.TextBox.textChanged.connect(self.textChange)
        self.Numbers.setReadOnly(True)
        self.TextBox.verticalScrollBar().valueChanged.connect(
            self.Numbers.verticalScrollBar().setValue)

    def textChange(self):
        self.lineNum()

    def lineNum(self):
        self.Numbers.clear()
        self.Numbers.setAlignment(Qt.AlignRight)
        for i in range(1, self.TextBox.toPlainText().count('\n') + 2):

            self.Numbers.insertPlainText(str(i)+'\n')


app = QApplication([])
window = MyGUI()
app.exec_()
