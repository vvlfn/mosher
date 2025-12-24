from typing import Callable
from PySide6.QtWidgets import QFileDialog, QWidget


class FileDialog(QWidget):
    def __init__(self, action: Callable) -> None:
        super().__init__()

        self.setWindowTitle("Select a file")

        self.dialog: QFileDialog = QFileDialog(self)
        self.dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        self.dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")

        if self.dialog.exec():
            selectedFile: str = self.dialog.selectedFiles()[0]
            action(selectedFile)
