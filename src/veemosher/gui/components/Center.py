from typing import Callable
from PySide6.QtWidgets import QWidget, QPushButton, QBoxLayout, QLabel
from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from veemosher.gui.FileDialog import FileDialog


class CenterWidget(QWidget):
    def __init__(self, getFile: Callable, setFile: Callable) -> None:
        super().__init__()

        self.l: QBoxLayout = QBoxLayout(QBoxLayout.Direction.BottomToTop)
        self.setFile: Callable = setFile
        self.getFile: Callable = getFile

        self.updateDisplay()

        self.setLayout(self.l)

    def updateDisplay(self) -> None:
        if not self.getFile():
            self.openFileButton: QPushButton = QPushButton("No file selected")
            self.openFileButton.clicked.connect(self.openFileDialog)
            self.l.addWidget(self.openFileButton)
            self.openFileButton.show()
        else:
            self.label: QLabel = QLabel()
            self.img: QPixmap = QPixmap()
            with open(self.getFile(), "rb") as f:
                data: bytes = f.read()
            self.img.loadFromData(data)
            self.label.setPixmap(self.img)
            self.l.removeWidget(self.openFileButton)
            self.l.addWidget(self.label)
            self.label.setMaximumSize(400, 400)
            self.label.show()

    @QtCore.Slot()
    def openFileDialog(self) -> None:
        dialog: QWidget = FileDialog(self.setFile)
        dialog.show()
