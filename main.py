import os
import cv2
import nb
import blur
import dilate
import fnmatch
import sys
import read_help as help

input = 'input'
output = 'output'


args = sys.argv


if "--h" in args:
    help.read()

if "--i" in args:
    x = args.index("--i")
    input = args[x+1]

if "--o" in args:
    y = args.index("--o")
    output = args[y+1]

#if "--filters" in args:
#    z = args.index("--filters")
#    filters = args[z+1]
#    if filters == nb:
#        nb.transnb(f'{input}/{img}', out)
#        z += 1






path = os.getcwd()
print ("The current working directory is %s" % path)


try:
    listOfFiles = os.listdir(input)
    pattern = "*.jpg"
    pattern2 = "*.png"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
        elif fnmatch.fnmatch(entry, pattern2):
            print(entry)
    path = output

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)

    for img in listOfFiles:
        print(img)
        out = path + img
        print(out)
        nb.transnb(f'{input}/{img}', out)
        blur.transblur(f'{output}/{img}', 5, out)
        dilate.transdilate(f'{output}/{img}', out)

except FileNotFoundError:
    if "--h" not in args:
        print('Please enter an input path with -i <path>')



