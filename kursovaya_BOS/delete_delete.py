# coding=utf-8
import os
import random
import string
import struct
from PIL import Image, ImageDraw


def del_file(file_path):

    if os.path.isfile(file_path):
        if os.path.exists(file_path):
            op_file = open(file_path, "rb")
            fd = op_file.fileno()
            size = os.path.getsize(file_path)
            file_name = file_path.split('/')[-1]
            op_file.close()
            op_file = open(file_path, "wb")
            for i in range(0, int(size)):
                os.write(fd, struct.pack('b', 0))
                op_file.seek(1)
            op_file.close()
            new_name = ''
            for x in range(0, 255 - int(len(file_path))):
                new_name = new_name + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
            new_path = file_path.replace(file_name, file_name + new_name + '.' + file_name.split('.')[-1])
            os.rename(file_path, new_path)
            op_file = open(new_path, "w")
            op_file.truncate(0)
            op_file.close()
            for j in range(0, 7):
                op_file = open(new_path, "ab")
                for i in range(0, 512):
                    os.write(fd, struct.pack('b', 0))
                op_file.close()
            os.remove(new_path)


def del_img(img_path):
    if os.path.exists(img_path):
        image = Image.open(img_path)
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = a + b + c
                if (S > (((355)//2)*3)):
                    a, b, c = 255, 255, 255
                else:
                    a, b, c = 0, 0, 0
                draw.point((i, j), (a, b, c))
        for i in range(width):
            for j in range(height):
                rang = 1000
                rand = random.randint(-rang, rang)
                a = pix[i, j][0] + rand
                b = pix[i, j][1] + rand
                c = pix[i, j][2] + rand
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))
        image = image.resize((1, 1))
        image.save(img_path)
        del draw

        new_name = ''
        for x in range(0, 255 - int(len(img_path))):
            new_name = new_name + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        new_path = img_path.replace(img_path, img_path[:4] + new_name + '.' + img_path.split('.')[-1])
        os.rename(img_path, new_path)
        os.remove(new_path)


def del_dir(dir_path):
    if os.path.isdir(dir_path):
        if os.path.exists(dir_path):
            files_list = []
            dirs_list = []
            for d, dirs, files in os.walk(dir_path):
                for f in files:
                    files_list.append(os.path.join(d, f))
                for di in dirs:
                    dirs_list.append(os.path.join(d, di))
            if files_list:
                for f_file in files_list:
                    if f_file[-3:] == 'txt':
                        del_file(f_file)
                    if f_file.split('.')[-1] == 'jpeg' or f_file.split('.')[-1] == 'png' \
                            or f_file.split('.')[-1] == 'jpg' or f_file.split('.')[-1] == 'bmp':
                        del_img(f_file)
                    else:
                        os.remove(f_file)
            if dirs_list:
                for d_dir in dirs_list:
                    new = ''
                    for x in range(0, 256 - int(len(d_dir))):
                        new = new + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                    dir_name = d_dir.split('\\')[-1]
                    new_path = d_dir.replace(dir_name, dir_name + new)
                    os.rename(d_dir, new_path)
                    os.rmdir(new_path)
            new_add = ''
            for x in range(0, 256 - int(len(dir_path))):
                new_add = new_add + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
            dir_name = dir_path.split('\\')[-2]
            new_path = dir_path.replace('\\' + dir_name + '\\ ', '\\' + dir_name + new_add)
            os.rename(dir_path, new_path)
            os.rmdir(new_path)


while True:
    param = raw_input('If you want to delete file - enter f\n'
                      'If you want to delete directory - enter d\n'
                      'If you want to delete image - enter i\n'
                      'If you want to exit the program - enter e: ')
    if param == 'f' or param == 'd'or param == 'i':
        dir_or_file_path = raw_input("Input path : ")
        if param == 'f':
            try:
                del_file(dir_or_file_path)
                print 'Successful ! '
            except Exception:
                print 'Something wrong ! '
        elif param == 'd':
            try:
                del_dir(dir_or_file_path)
                print 'Successful ! '
            except Exception:
                print 'Something wrong ! '
        elif param == 'i':
            try:
                del_img(dir_or_file_path)
                print 'Successful ! '
            except Exception:
                print 'Something wrong ! '
    elif param == 'e':
        print 'Good bye ! '
        break
    else:
        print 'Wrong param'


        #D:\test\test.txt
        #D:\test\test\
        #D:\test\temp.jpg