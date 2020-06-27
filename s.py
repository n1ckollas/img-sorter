import os
import exifread
from PIL import Image
import time

path = "D:\\testPics"
test_file = "336053_4339577334193_1631752716_o.jpg"
supported_img_formats = ['jpg']

def is_supported_img(file):
    split_file_name = file.rsplit('.')
    if len(split_file_name) > 0:
        ext = str(split_file_name[len(split_file_name) - 1]).lower()
        if ext != "" and split_file_name[0] != '' and ext in supported_img_formats:
            return True
        else:
            return False
    return False


def string_to_date(date_string):
    print(date_string.split(" "))


def get_img_dates(path):
    dates = []

    f = open(path, 'rb')
    meta_content = exifread.process_file(f) 
    pill = Image.open(path)._getexif();

    if(pill):
        print("PIL")
        for key in pill:
            if(key == 306):
                string_to_date(pill[key])
            elif(key == 36867):
                string_to_date(pill[key])
            elif(key == 36868):
                string_to_date(pill[key])
            elif(key == 29):
                string_to_date(pill[key])
            else:
                pass
    elif(meta_content):
        print("EXIFREAD")
        for key in meta_content:
            if 'date' in str(key).lower():
                string_to_date(meta_content[key])
    else:
        print("OS.PATH")
        mtime = os.path.getmtime( path )
        atime = os.path.getatime( path )
        ctime = os.path.getctime( path )
        
        print(time.ctime(mtime))
        print(time.ctime(atime))
        print(time.ctime(ctime))
    return "DONE"

def navigate_directories(path):
    for file in os.listdir(path):
        if os.path.isdir(path + "\\" +  file):
            # navigate in directory.
            print(file + " => is a directory")
            print("navigating in to the directory => " + file )
            navigate_directories(path + "\\" + file)
            
        else:
            if is_supported_img(file):
                print(file + " => SUPPORTED file")
                print(get_img_dates(path + "\\" + file))
            else:
                print(file + " => NOT Accepted")
    else:
        print("Directory is empty")
        

navigate_directories(path)
