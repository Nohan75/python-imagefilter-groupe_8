import os
import cv2
import nb
import blur
import dilate

path = os.getcwd()
print ("The current working directory is %s" % path)

path = "Data/output"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

# nb.transnb()
blur.transblur(4)
# dilate.transdilate()

