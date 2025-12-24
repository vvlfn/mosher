from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QHBoxLayout,
)

from veemosher.gui.components import ImagePreview, FilterList


class Mosher(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Vee's Mosher")
        self.resize(400, 300)
        self.imagePath: str = ""

        self.root: QWidget = QWidget()
        self.mainLayout: QHBoxLayout = QHBoxLayout()

        self.center: ImagePreview = ImagePreview(self.setImagePath)
        self.center.show()

        self.right: FilterList = FilterList()
        self.right.show()

        self.mainLayout.addWidget(self.center)
        self.mainLayout.addWidget(self.right)

        self.root.setLayout(self.mainLayout)
        self.setCentralWidget(self.root)
        self.show()

    def setImagePath(self, path: str) -> None:
        self.imagePath = path
