# coding=utf-8

import os


files_list = []
dirs_list = []
for d, dirs, files in os.walk('D:/test'):
    for f in files:
        print os.path.join(d, f)


print dirs_list
'''
for dir in dirs_list:
    os.chdir('D:/test'+'/'+dir)
    for d, dirs, files in os.walk('D:/test'+'/'+dir):
        for file_name in files:
            files_list.append( os.path.abspath(file_name))
print(files_list)
'''

files_list_ = []


def find_full_path(dir_path):

    os.chdir(dir_path)
    dirs_list = []

    for d in os.listdir(dir_path):
        if os.path.isfile(dir_path+'/'+d):
            files_list_.append(os.path.abspath(d))
        if os.path.isdir(dir_path+'/'+d):
            dirs_list.append(dir_path+'/'+d)

    for d in dirs_list:
        find_full_path(d)


os.rmdir('D:\\test\\ttt')

'''
os.remove(path, *, dir_fd=None)# - удаляет путь к файлу.

os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)# - переименовывает файл или директорию из src в dst.
os.truncate(path, length)# - обрезает файл до длины length.

def rem(path):
   if os.path.isfile(path):
     os.remove(path)
os.path.walk('c:\\path\\',rem)
'''
#print os.path.isdir('c:\\python26\\LICENSE.txt')

#print os.path.isfile('c:\\python26\\LICENSE.txt')

#print os.path.exists('c:\\python26\\LICENSE2.txt')

#print os.path.getsize('c:\\python26\\LICENSE.txt')

#dir_path, file_path = os.path.split(r'C:\temp\data.txt')
#print dir_path, file_path
#('C:\\temp', 'data.txt')

#os.path.join(r'C:\temp', 'output.txt')
#C:\\temp\\output.txt



#os.chdir(r'C:\Users')
#print os.getcwd()
#'C:\\Users'

#print os.path.abspath('')      # пустая строка означает тек. раб. каталог (cwd)
#'C:\\Users'
#print os.path.abspath('temp')  # расширяет до полного пути к файлу в тек. кат.
#'C:\\Users\\temp'
#os.path.abspath(r'PP4E\dev') # частичный путь относительно тек. раб. кат.
#'C:\\Users\\PP4E\\dev'
#os.path.abspath('.')     # расширяет относительные пути
#'C:\\Users'
#os.path.abspath('..')
#'C:\\'


#os.system('start cmd')



#listing = os.popen('dir /B').readlines()
#print listing
#['helloshell.py\n', 'more.py\n', 'more.pyc\n', 'spam.txt\n', '__init__.py\n']


#os.remove(), os.rename, os.mkfifo, os.mkdir,
#os.rmdir
