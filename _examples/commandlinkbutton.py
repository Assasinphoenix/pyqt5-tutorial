#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        linkbutton1 = QCommandLinkButton()
        linkbutton1.setDescription("Command Link Button 1")
        layout.addWidget(linkbutton1, 0, 0)
        linkbutton2 = QCommandLinkButton()
        linkbutton2.setDescription("Command Link Button 2")
        layout.addWidget(linkbutton2, 1, 0)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
