import PIL
from PIL import Image
import os
from os import listdir

old_pic=r'C:\Users\LENOVO\Downloads\cat.jpg'
new_pic=r'C:\Users\LENOVO\Downloads\cat_resized.jpg'
old_folder=r'C:\Users\LENOVO\Desktop\cats'
new_folder=r'C:\Users\LENOVO\Desktop\cats_resize'

def single_image(old_pic,new_pic):
  img = Image.open( old_pic)
  mywidth=img.width
  wpercent = (mywidth/float(img.size[0]))
  hsize = int((float(img.size[1])*float(wpercent)))
  img = img.resize((mywidth,hsize), PIL.Image.LANCZOS)
  img.save(new_pic)

def directory_image(old_folder, new_folder):
  files=os.listdir(old_folder)
  for file in files:
    old_pic=old_folder+ '\\' + file
    new_pic=new_folder+'\\'+file
    single_image(old_pic,new_pic)

    
  

directory_image(old_folder,new_folder)