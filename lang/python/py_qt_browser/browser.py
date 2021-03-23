from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):
    def __init__ (self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.setCentralWidget(self.browser)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        back_btn = QAction(QIcon(), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(), "Next", self)
        next_btn.setStatusTip("Back to previous page")
        navtb.addAction(next_btn)

        self.show()

        self.setWindowTitle("Maz Browser")


app = QApplication(sys.argv)
app.setApplicationName("Maz Browser")
app.setOrganizationName("Maz")
app.setOrganizationDomain("mazpy@protonmail.ch")

window = MainWindow()
window.show()

app.exec_()