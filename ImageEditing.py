import os,time,datetime
from pathlib import Path

path = "C:/Users/Username/Pictures/folder" # Path to directory with images
paths = sorted(Path(path).iterdir(),key=os.path.getmtime)

def NameChange(): # Changes name by date of last modified
    for index,image in enumerate(paths,start=1):
        os.rename(image,path+"/"+str(index)+image.suffix)
    print("Done Changing names.")

def FormatChange(): # Changes images format to .jpg
    for image in paths:
        name ,ext = os.path.splitext(image)
        if ".mp4" not in ext and ".jpg" not in ext:
            os.rename(image,name+".jpg")
    print("Done Changing formates.")

def DateChange(): # Changes the date of last modified
    for name in [8,14]: # name of images (numbers)
        path1 = path+"/"+str(name-1)+".jpg"
        path0 = path+"/"+str(name)+".jpg"
        before = datetime.datetime.fromtimestamp(os.path.getmtime(path1))
        m = before.minute
        s = before.second
        if before.second == 59:
            if before.minute != 59:
                m += 1
        else:
            s += 1
        date = datetime.datetime(year=before.year, month=before.month, day=before.day, hour=before.hour, minute=m, second=s)
        modTime = time.mktime(date.timetuple())
        os.utime(path0, (modTime, modTime))
    print("Done changing modified dates.")

if __name__ == '__main__':
    DateChange()