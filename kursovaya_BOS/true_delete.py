# coding=utf-8
import os


def del_file(file_path, overwrite):

    if os.path.isfile(file_path):

        if os.path.exists(file_path):

            op_file = open(file_path, "rb")
            fd = op_file.fileno()
            size = os.path.getsize(file_path)
            file_name = file_path.split('/')[-1]
            op_file.close()

            for i in range(0, int(overwrite)):
                op_file = open(file_path, "wb")
                string_s = os.urandom(size)
                os.write(fd, string_s)
                op_file.close()

            new_path = file_path.replace(file_name, file_name[0] + file_name.split('.')[-1])
            os.rename(file_path, new_path)
            os.remove(new_path)


def del_dir(dir_path, overwrite):

    if os.path.isdir(dir_path):
        if os.path.exists(dir_path):

            files_list = []
            dirs_list = []

            for d, dirs, files in os.walk(dir_path):
                for f in files:
                    files_list.append(os.path.join(d, f))
                for di in dirs:
                    dirs_list.append(os.path.join(d, di))
            #print dirs_list

            if files_list:

                for f_file in files_list:
                    if f_file[:3] == 'txt':
                        del_file(f_file, overwrite)
                    else:
                        os.remove(f_file)

            if dirs_list:

                for d_dir in dirs_list:
                    dir_name = d_dir.split('\\')[-1]
                    new_path = d_dir.replace(dir_name, dir_name[0])
                    os.rename(d_dir, new_path)
                    os.rmdir(new_path)

            os.rmdir(dir_path)


while True:

    param = raw_input('If you want to delete file - enter f\n'
                      'If you want to delete directory - enter d\n'
                      'If you want to exit the program - enter e: ')

    if param == 'f' or param == 'd':

        dir_or_file_path = raw_input("Input path : ")
        count_of_overwrite = raw_input("Enter the number of overwriting: ")

        if param == 'f':

            try:
                del_file(dir_or_file_path, count_of_overwrite)
                print 'Successful ! '

            except Exception:
                print 'Something wrong ! '

        elif param == 'd':

            try:
                del_dir(dir_or_file_path, count_of_overwrite)
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