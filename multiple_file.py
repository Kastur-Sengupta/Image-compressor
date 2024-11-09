import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog
from PyQt5 import QtGui
import PIL
from PIL import Image
import os

image_width=0.75

app = QApplication(sys.argv)
windows =QWidget()

windows.resize(400,600)
windows.move(200,200)

windows.setFixedSize(400,600)
windows.setWindowTitle('Image Compressor')
windows.setStyleSheet("background-color: black;")
windows.setWindowIcon(QtGui.QIcon(r'C:\Users\LENOVO\Downloads\icon.png'))

frame1 = QFrame(windows)
frame1.setFrameShape(QFrame.StyledPanel)
frame1.setGeometry(50, 85, 300, 420)
frame1.setLineWidth(3)
frame1.setStyleSheet("background-color: #202020; border-radius: 20px;")

Multiple_Title=QLabel(frame1)
Multiple_Title.setText('Multiple Image')
Multiple_Title.setStyleSheet("color: white; font-weight:bold; font-size: 20px")
Multiple_Title.move(80,30)

Multiple_Title2=QLabel(frame1)
Multiple_Title2.setText('Compression')
Multiple_Title2.setStyleSheet("color: white; font-weight:bold; font-size: 20px")
Multiple_Title2.move(90,57)

Multiple_source=QLabel(frame1)
Multiple_source.setText('Enter source of the folder')
Multiple_source.setStyleSheet("color: white; font-size: 18px")
Multiple_source.move(30,100)

image_path=QLineEdit(frame1)
image_path.move(30,140)
image_path.setStyleSheet("background-color: white ;color: black; font-size: 18px; width:150px ")

dtr_src=QPushButton(frame1)
dtr_src.setText('...')
dtr_src.setStyleSheet("""
    QPushButton {
        color: white;
        background-color: #202020;
        border: 1px solid white;
        padding: 5px;
        border-radius: 8px;
        width:25px               
    }
    QPushButton:hover {
        background-color: white;
        color:#202020
    }
""")
dtr_src.move(200,136)
def select_file():
   file=QFileDialog.getExistingDirectory(None,'Select Source Directory')
   image_path.setText(file)

dtr_src.clicked.connect(select_file) 

Multiple_Quality=QLabel(frame1)
Multiple_Quality.setText('Quality: ')
Multiple_Quality.setStyleSheet("color: white; font-size: 18px")
Multiple_Quality.move(30,180)

quality=QLineEdit(frame1)
quality.move(30,215)
quality.setStyleSheet("background-color: white ;color: black; font-size: 18px; width:100px ")
quality.setText('High')

combo=QComboBox(frame1)
combo.addItem('High')
combo.addItem('Medium')
combo.addItem('Low')
combo.move(150,211)
combo.setStyleSheet("""
    QComboBox {
        color: white;
        background-color: #202020;
        border: 1px solid white;
        padding: 5px;    
        height:20px;   
        width:65px;
    }
    QComboBox:hover {
        background-color: white;
        color:#202020
    }
    QComboBox QAbstractItemView {
        height:30px;
        background-color: #202020;
        color: white;
        selection-background-color: white; /* Background color when an item is selected */
        selection-color: #202020; /* Text color when an item is selected */
    }"""
    
)
def combo_box():
   quality.setText(combo.currentText())
   global image_width
   if (combo.currentText()=='High'):
      image_width=0.75
   if combo.currentText()=='Medium':
      image_width=0.5
   if combo.currentText()=='Low':
      image_width=0.25

combo.currentIndexChanged.connect(combo_box)

Multiple_destination=QLabel(frame1)
Multiple_destination.setText('Enter destination of the folder')
Multiple_destination.setStyleSheet("color: white; font-size: 18px")
Multiple_destination.move(30,260)

image_dst=QLineEdit(frame1)
image_dst.move(30,300)
image_dst.setStyleSheet("background-color: white ;color: black; font-size: 18px; width:150px ")

dtr_dst=QPushButton(frame1)
dtr_dst.setText('...')
dtr_dst.setStyleSheet("""
    QPushButton {
        color: white;
        background-color: #202020;
        border: 1px solid white;
        padding: 5px;
        border-radius: 8px;
        width:25px               
    }
    QPushButton:hover {
        background-color: white;
        color:#202020
    }
""")
dtr_dst.move(200,296)

def select_file2():
   file=QFileDialog.getExistingDirectory(None,'Select Destination Directory')
   image_dst.setText(file)

dtr_dst.clicked.connect(select_file2)

compress=QPushButton(frame1)
compress.setText('Compress')
compress.setStyleSheet("""
    QPushButton {
        color: white;
        background-color: #202020;
        border: 1px solid white;
        padding: 8px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: white;
        color:#202020
    }
""")
compress.move(105,350)
def image_compress():
  files=os.listdir(image_path.text())
  for file in files:
    old_pic=image_path.text()+ '\\' + file
    new_pic=image_dst.text()+'\\'+file
    img = Image.open(old_pic)
    mywidth=int(img.width*image_width)
    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((mywidth,hsize), PIL.Image.LANCZOS)
    img.save(new_pic)
  
  print('Done')
  windows.close()
  
compress.clicked.connect(image_compress)

def image_compress():
   print()
compress.clicked.connect(image_compress)





windows.show()
sys.exit(app.exec_())
