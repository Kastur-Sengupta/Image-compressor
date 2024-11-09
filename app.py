import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel
from PyQt5 import QtGui,QtCore


class ClickableFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
           subprocess.run(["python","single_file.py"])

class ClickableFrame2(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
           subprocess.run(["python","multiple_file.py"])

app = QApplication(sys.argv)
windows =QWidget()

windows.resize(400,600)
windows.move(200,200)

windows.setFixedSize(400,600)
windows.setWindowTitle('Image Compressor')
windows.setStyleSheet("background-color: black;")
windows.setWindowIcon(QtGui.QIcon(r'C:\Users\LENOVO\Downloads\icon.png'))

frame1 = ClickableFrame(windows)
frame1.setFrameShape(QFrame.StyledPanel)
frame1.setGeometry(50, 100, 300, 160)
frame1.setLineWidth(3)
frame1.setStyleSheet("background-color: #202020; border-radius: 20px;")
single_heading=QLabel(frame1)
single_heading.setText('Single Image')
single_heading.setStyleSheet("color: white; font-weight:bold; font-size:20px;")
single_heading.move(87,25)

single_para=QLabel(frame1)
single_para.setText('Click here to compress single image')
single_para.setStyleSheet("color: white; font-size: 17px; padding-right:20px; ")
single_para.setWordWrap(True)
single_para.setFixedSize(260, 40)
single_para.move(30,70)
single_para.setAlignment(QtCore.Qt.AlignCenter)






frame2 = ClickableFrame2(windows)
frame2.setFrameShape(QFrame.StyledPanel)
frame2.setGeometry(50, 340, 300, 160)
frame2.setLineWidth(3)
frame2.setStyleSheet("background-color: #202020; border-radius: 20px")

multiple_heading=QLabel(frame2)
multiple_heading.setText('Multiple Image')
multiple_heading.setStyleSheet("color: white; font-weight:bold; font-size: 20px")
multiple_heading.move(77,25)
multiple_para=QLabel(frame2)
multiple_para.setText('Click here to compress multiple images')
multiple_para.setStyleSheet("color: white; font-size: 17px; padding-right:20px; ")
multiple_para.setWordWrap(True)
multiple_para.setAlignment(QtCore.Qt.AlignCenter)
multiple_para.setFixedSize(260, 40)
multiple_para.move(30,70)

windows.show()
sys.exit(app.exec_())
