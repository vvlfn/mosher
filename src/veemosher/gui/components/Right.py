from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout
from PySide6.QtCore import Qt


class RightWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.mainLayout.setSpacing(5)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setMaximumHeight(400)
        self.options: list[QPushButton] = []
        self.addButtons()
        self.setLayout(self.mainLayout)
        self.show()

    def addButtons(self) -> None:
        for i in range(5):
            button: QPushButton = QPushButton(f"Button #{i}")
            self.options.append(button)
            self.mainLayout.addWidget(button)
