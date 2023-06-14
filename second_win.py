from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *
class secwin(QWidget):
    def __init__(self):
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()


def set_appear(self):
    self.SetWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)


def initUI(self):
    self.v_line1 = QVBoxLayout()
    self.v_line2 = QVBoxLayout()
    self.h_line = QVBoxLayout()
    self.btn_next = QPushButton(txt_sendresults, self)
    self.btn_test1 = QPushButton(txt_starttest1, self)
    self.btn_test2 = QPushButton(txt_starttest2, self)
    self.btn_test3 = QPushButton(txt_starttest3, self)
    self.text_name = QLabel(txt_name, self)
    self.text_age = QLabel(txt_age, self)
    self.text_test1 = QLabel(txt_test1, self)
    self.text_test2 = QLavel(txt_test2, self)
    self.text_test3 = QLabel(txt_test3, self)
    self.l_line.addWidget(self.text_name, aligment = Qt.AlignLeft)
    self.l_line.addWidget(self.v_line1, aligment = Qt.AlignLeft)



def connects(self):
    self.btn_next.clicked.connect(self.next_click)

app = QApplication([])
app.exec_()
