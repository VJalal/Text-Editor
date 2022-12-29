
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.show()

        # Connect text change function
        self.TextBox.textChanged.connect(self.textChange)

        # Set number bar to read only
        self.Numbers.setReadOnly(True)

        # Connect the scrolling of numbers to scrolling of text to keep position
        self.TextBox.verticalScrollBar().valueChanged.connect(
            self.Numbers.verticalScrollBar().setValue)

        # Connecting tool bar options
        self.actionSave.triggered.connect(self.saver)
        self.actionOpen.triggered.connect(self.opener)
        self.actionFont.triggered.connect(self.fontDialog)
        self.actionColor.triggered.connect(self.colorDialog)
        self.actionBold.triggered.connect(self.boldDialog)
        self.actionItalic.triggered.connect(self.italicDialog)
        self.actionUnderline.triggered.connect(self.underlineDialog)

        # Set up for font
        self.font = QFont()

        # Shortcut for save
        self.ctrlS = QShortcut(QKeySequence("Ctrl+S"), self)
        self.ctrlS.activated.connect(self.saver)

        # Shortcut for open
        self.ctrlO = QShortcut(QKeySequence("Ctrl+O"), self)
        self.ctrlO.activated.connect(self.opener)

        self.statusbar.showMessage('hi')

    # Function to save the file
    def saver(self):
        filename = QFileDialog.getSaveFileName(self, 'Save')  # save file
        if filename[0]:

            with open(filename[0], 'w') as f:
                # Whatever text written in TextBox will be saved
                text = self.TextBox.toPlainText()
                f.write(text)
                QMessageBox.about(self, "Save", "File saved successfully")

    # Function to open a new file using the file explorer

    def opener(self):
        filename = QFileDialog.getOpenFileName(self, 'Open')  # save file
        if filename[0]:
            # f = open(filename[0], 'w')  # in right mode (w mode)

            with open(filename[0], 'r') as f:
                # Whatever text written in TextBox will be saved
                text = f.read()
                self.TextBox.clear()
                self.TextBox.insertPlainText(text)
                QMessageBox.about(self, "Open", "File opened successfully")

    def fontDialog(self):
        self.font, ok = QFontDialog.getFont()

        if ok:
            self.TextBox.setFont(self.font)
            self.Numbers.setFont(self.font)

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.TextBox.setTextColor(color)

    def boldDialog(self):

        self.font.setBold(True)
        self.TextBox.setFont(self.font)

    def italicDialog(self):

        self.font.setItalic(True)
        self.TextBox.setFont(self.font)

    def underlineDialog(self):

        self.font.setUnderline(True)
        self.TextBox.setFont(self.font)

    # Function called whenever text on screen is modified
    def textChange(self):
        self.lineNum()

    def lineNum(self):
        self.Numbers.clear()
        self.Numbers.setAlignment(Qt.AlignRight)

        # Counting the number of '\n' in the text and writing numbers on the left matching the number of lines
        for i in range(1, self.TextBox.toPlainText().count('\n') + 2):

            self.Numbers.insertPlainText(str(i)+'\n')

        # Sets the scrolling of numbers to match the text
        self.Numbers.verticalScrollBar().setValue(
            self.TextBox.verticalScrollBar().value())


app = QApplication([])
window = MyGUI()
app.exec_()
