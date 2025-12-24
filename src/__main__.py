import sys
from veemosher import Mosher
from PySide6.QtWidgets import QApplication


def Main() -> None:
    app: QApplication = QApplication(sys.argv)

    mosher: Mosher = Mosher()
    mosher.show()
    app.exec()


if __name__ == "__main__":
    Main()
