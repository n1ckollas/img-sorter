import os
import exifread

path = "D:\\testPics\\"
supported_img_formats = ['jpg']

def is_supported_img(file):
    file_name, ext = os.path.splitext(file)
    if ext != "" and file_name[0] != '.':
        ext = str(ext).lower().strip('.')
        if ext in supported_img_formats:
            return True
    return False

def get_img_dates(path):
    f = open(path, 'rb')
    meta_content = exifread.process_file(f) 
    if(meta_content != None):
        for key in meta_content:
            if 'date' in str(key).lower():
                print(key)
                print(meta_content[key])
    return "DONE"

for file in os.listdir(path):
    if os.path.isdir(path + file):
        # navigate in directory.
        print(file + " => is a directory")
    elif os.path.isfile(path + file):
        print(file + " => is a file")
        if is_supported_img(file):
            print(get_img_dates(path + file))
        else:
            print("NO")
    else:
        print("It is a special file (socket, FIFO, device file)")

