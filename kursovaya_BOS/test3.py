import os
import struct
import random


os.chdir('D:/test/files/')
for i in range(0, 10):
    file_name = 'file' + str(i) + '.txt'

    op_file = open(file_name, "wb")
    op_file.close()
    op_file = open(file_name, "rb")
    fd = op_file.fileno()
    op_file.close()
    op_file = open(file_name, "wb")
    rand = random.randint(1, 10000)
    for j in range(rand):
        os.write(fd, struct.pack('b', 0))
    op_file.close()
