from PySide6.QtWidgets import QApplication, QPushButton, QFileDialog
from PySide6 import QtCore

class App(QApplication):
    def __init__(self, argv) -> None:
        super().__init__(argv)
        # TODO: selecting a file dialog :3
        
    #     self.button = QPushButton("test")
    #     self.button.show()
    #     self.button.clicked.connect(self.openFileDialog)
        
    #     self.imagePath: str = ""
        
    # def openFileDialog(self) -> None:
    #     dialog: QFileDialog = QFileDialog()
    #     dialog.fileSelected.connect(self.setImagePath)
        
    # def setImagePath(self, path: str) -> None:
    #     print(path)
    #     self.imagePath = path
    