
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.show()
        self.TextBox.textChanged.connect(self.textChange)
        self.Numbers.setReadOnly(True)
        self.TextBox.verticalScrollBar().valueChanged.connect(
            self.Numbers.verticalScrollBar().setValue)
        self.actionSave.triggered.connect(self.saver)
        self.actionFont.triggered.connect(self.fontDialog)
        self.actionColor.triggered.connect(self.colorDialog)
        self.actionBold.triggered.connect(self.boldDialog)
        self.actionItalic.triggered.connect(self.italicDialog)
        self.actionUnderline.triggered.connect(self.underlineDialog)
    
    def saver(self):
        filename = QFileDialog.getSaveFileName(self, 'Save') #save file
        if filename[0]:
            f = open(filename[0], 'w') #in right mode (w mode)

            with f:
                text = self.TextBox.toPlainText() #Whatever text written in TextBox will be saved
                f.write(text)
                QMessageBox.about(self, "Save", "File saved successfully")


    def fontDialog(self):
        font, ok = QFontDialog.getFont()

        if ok: 
            self.TextBox.setFont(font)

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.TextBox.setTextColor(color)

    def boldDialog(self):
        font = QFont()
        font.setBold(True)
        self.TextBox.setFont(font)

    def italicDialog(self):
        font = QFont()
        font.setItalic(True)
        self.TextBox.setFont(font)

    def underlineDialog(self):
        font = QFont()
        font.setUnderline(True)
        self.TextBox.setFont(font)

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
