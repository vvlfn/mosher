from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QHBoxLayout,
)

from veemosher.gui.components import CenterWidget, RightWidget


class Mosher(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Vee's Mosher")
        self.resize(400, 300)
        self.imagePath: str | None = None

        self.root: QWidget = QWidget()
        self.mainLayout: QHBoxLayout = QHBoxLayout()

        self.center: CenterWidget = CenterWidget(self.getImagePath, self.setImagePath)
        self.right: RightWidget = RightWidget()

        self.mainLayout.addWidget(self.center)
        self.mainLayout.addWidget(self.right)

        self.root.setLayout(self.mainLayout)
        self.setCentralWidget(self.root)
        self.show()

    def setImagePath(self, path: str) -> None:
        self.imagePath = path
        print(self.imagePath)
        self.center.updateDisplay()

    def getImagePath(self) -> str | None:
        return self.imagePath
