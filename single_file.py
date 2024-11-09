import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel, QLineEdit, QPushButton, QComboBox,QFileDialog, QInputDialog 
from PyQt5 import QtGui
import PIL
from PIL import Image

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
frame1.setGeometry(50, 100, 300, 400)
frame1.setLineWidth(3)
frame1.setStyleSheet("background-color: #202020; border-radius: 20px;")

single_Title=QLabel(frame1)
single_Title.setText('Single Image Compression')
single_Title.setStyleSheet("color: white; font-weight:bold; font-size: 20px")
single_Title.move(18,30)

single_Quality=QLabel(frame1)
single_Quality.setText('Enter Path of the image')
single_Quality.setStyleSheet("color: white; font-size: 18px")
single_Quality.move(30,100)

image_path=QLineEdit(frame1)
image_path.move(30,150)
image_path.setStyleSheet("background-color: white ;color: black; font-size: 18px; width:150px ")

src=QPushButton(frame1)
src.setText('...')
src.setStyleSheet("""
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

src.move(200,146)

def select_file():
   fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;JPEG (*.jpg);;PNG(*.png);;JPG(*.jpg)")
   if fileName:
    print(fileName)
    image_path.setText(fileName)

src.clicked.connect(select_file) 



single_Quality=QLabel(frame1)
single_Quality.setText('Quality: ')
single_Quality.setStyleSheet("color: white; font-size: 18px")
single_Quality.move(30,200)

quality=QLineEdit(frame1)
quality.move(30,240)
quality.setStyleSheet("background-color: white ;color: black; font-size: 18px; width:100px ")
quality.setText('High')

combo=QComboBox(frame1)
combo.addItem('High')
combo.addItem('Medium')
combo.addItem('Low')
combo.move(150,237)
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
      image_width=0.50
   if combo.currentText()=='Low':
      image_width=0.25

combo.currentIndexChanged.connect(combo_box)

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

compress.move(105,320)

def image_compress():
  img = Image.open(image_path.text())
  mywidth=int(img.width*image_width)
  wpercent = (mywidth/float(img.size[0]))
  hsize = int((float(img.size[1])*float(wpercent)))
  img = img.resize((mywidth,hsize), PIL.Image.LANCZOS)
  input=QInputDialog
  new_pic, okPressed = input.getText(None, "Image Name","Enter Image name:", QLineEdit.Normal, "")
  if okPressed and new_pic != '':
    img.save(r'C:\Users\LENOVO\Desktop\\'+new_pic+'.jpg')
  print('Done')
  windows.close()
  
compress.clicked.connect(image_compress)

windows.show()
sys.exit(app.exec_())
