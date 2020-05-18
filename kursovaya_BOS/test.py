# coding=utf-8
import os
import random
import string
import struct
'''
dir_path = 'D:/test/test/'

name_size = len(a)
diff = 256 - int(name_size)
res = a
for x in range(0, diff-1):
    res = res + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
print a
print res



dir_name = dir_path[:len(dir_path)].split('\\')[-1]
dir_ = dir_path.split('/')

for i in range(0,len(dir_)):
    print dir_[-2]


print dir_name, dir_


op_file = open(a, "rb")
fd = op_file.fileno()
size = os.path.getsize(a)
file_name = a.split('/')[-1]
op_file.close()

#string_s = os.urandom(size)

for j in range(0, 7):
    op_file = open(a, "ab")
    for i in range(0, 512):
        os.write(fd, struct.pack('b', 0))
    op_file.close()

files_list = []
dirs_list = []

for d, dirs, files in os.walk('D:\\test'):
                for f in files:
                    files_list.append(os.path.join(d, f))
                for di in dirs:
                    dirs_list.append(os.path.join(d, di))

print files_list
print dirs_list'''

from Tkinter import *

root = Tk()

but = Button(root,
          text="Это кнопка", #надпись на кнопке
          width=30,height=5, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи

but.pack()
root.mainloop()

#!/usr/bin/python

import Tkinter
top = Tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()



from Tkinter import *

class But_print:
     def __init__(self):
          self.but = Button(root)
          self.but["text"] = "Печать"
          self.but.bind("<Button-1>",self.printer)
          self.but.pack()
     def printer(self,event):
          print ("Как всегда очередной 'Hello World!'")

root = Tk()
lab = Label(root, text="Это метка! \n Из двух строк.", font="Arial 18")
obj = But_print()
root.mainloop()

