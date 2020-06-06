import os
from PIL import Image
import exifread

path = "D:\\testPics\\"
supported_img_formats = ['jpg', 'png', 'mov', 'm4v']

def is_supported_img(file):
    file_name, ext = os.path.splitext(file)
    if ext != "" and file_name[0] != '.':
        ext = str(ext).lower().strip('.')
        if ext in supported_img_formats:
            return True
    return False

def get_date_taken(path):
    # return Image.open(path)._getexif()
    f = open(path, 'rb')
    meta_content = exifread.process_file(f) 
    for key in meta_content:
        if 'date' in str(key).lower():
            print(key)
            print(meta_content[key])


for file in os.listdir(path):
    if os.path.isdir(path + file):
        print(file + " => is a directory")
    elif os.path.isfile(path + file):
        print(file + " => is a file")
        if is_supported_img(file):
            print(get_date_taken(path + file))
        else:
            print("NO")
    else:
        print("It is a special file (socket, FIFO, device file)")

