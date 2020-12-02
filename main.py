import os
import cv2
import nb
import blur
import dilate
import fnmatch

path = os.getcwd()
print ("The current working directory is %s" % path)



listOfFiles = os.listdir('Data/imgs')
pattern = "*.jpg"
pattern2 = "*.png"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            print (entry)
    elif fnmatch.fnmatch(entry,pattern2):
            print (entry)

path = "Data/output"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

nb.transnb()
blur.transblur(5)
# dilate.transdilate()

