#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton("PushButton")
        button.setToolTip("ToolTip for a PushButton")
        layout.addWidget(button, 0, 0)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
