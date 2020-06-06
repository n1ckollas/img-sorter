import os
path = "c:\\Users\\n1cko\\Downloads\\"
for file in os.listdir(path):
    if os.path.isdir(path + file):
        print(file + " => is a directory")
    elif os.path.isfile(path + file):
        print(file + " => is a file")
    else:
        print("It is a special file (socket, FIFO, device file)")
