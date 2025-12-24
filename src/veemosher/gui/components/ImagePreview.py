from typing import Callable
from PySide6.QtWidgets import QWidget, QPushButton, QBoxLayout
from PySide6 import QtCore
from veemosher.gui.FileDialog import FileDialog


class ImagePreview(QWidget):
    def __init__(self, acceptFileAction: Callable) -> None:
        super().__init__()

        self.l: QBoxLayout = QBoxLayout(QBoxLayout.Direction.BottomToTop)
        self.acceptFileAction: Callable = acceptFileAction
        self.openFileButton: QPushButton = QPushButton("No file selected")
        self.openFileButton.clicked.connect(self.openFileDialog)
        self.l.addWidget(self.openFileButton)
        self.openFileButton.show()
        self.setLayout(self.l)

    @QtCore.Slot()
    def openFileDialog(self) -> None:
        dialog: QWidget = FileDialog(self.acceptFileAction)
        dialog.show()
