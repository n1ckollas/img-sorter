import os
import exifread
from PIL import Image
import time
from datetime import datetime

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


def earliest_date(dates):
    date_objects = []
    for d in dates:
        if(len(d.split(" ")) > 1):
            do = datetime.strptime(d, "%Y:%m:%d %H:%M:%S")
            date_objects.append(do)

    return min(date_objects)


def get_img_dates(path):
    dates = []

    f = open(path, 'rb')
    meta_content = exifread.process_file(f) 
    pill = Image.open(path)._getexif();

    if(pill):
        for key in pill:
            if(key == 306):
                dates.append(str(pill[key]))
            elif(key == 36867):
                dates.append(str(pill[key]))
            elif(key == 36868):
                dates.append(str(pill[key]))
            elif(key == 29):
                dates.append(str(pill[key]))
            else:
                pass

    if(meta_content):
        for key in meta_content:
            if 'date' in str(key).lower():
                dates.append(str(meta_content[key]))

    mtime = os.path.getmtime( path )
    atime = os.path.getatime( path )
    ctime = os.path.getctime( path )
    m = datetime.fromtimestamp(mtime).strftime("%Y:%m:%d %H:%M:%S")
    a = datetime.fromtimestamp(atime).strftime("%Y:%m:%d %H:%M:%S")
    c = datetime.fromtimestamp(ctime).strftime("%Y:%m:%d %H:%M:%S")
    dates.append(m)
    dates.append(a)
    dates.append(c)
    
    return dates

def navigate_directories(path):
    for file in os.listdir(path):
        if os.path.isdir(path + "\\" +  file):
            print("navigating in to the directory => " + file )
            navigate_directories(path + "\\" + file)
            
        else:
            if is_supported_img(file):
                print(file + " => SUPPORTED file")
                dates = get_img_dates(path + "\\" + file)
                earliest_date(dates)
            else:
                print(file + " => NOT Accepted")
    else:
        print("Directory is empty")
        

navigate_directories(path)
