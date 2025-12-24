import sys
from veemosher.gui.App import App 


def RunApp() -> None:
    app: App = App(sys.argv)
    app.exec_()