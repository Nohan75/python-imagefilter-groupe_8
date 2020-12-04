import os
import cv2
import nb
import blur
import dilate
import fnmatch
import sys
import read_help as help
import getopt
import log
import shutil
import conf






args = sys.argv


cf_file = 'imagefilter.ini'
if "--config-file" in args:
    i = args.index("--config-file")
    file = args[i+1]
    if os.path.exists(file):
        input = conf.input
        output = conf.output
        filters_list = conf.filters
    else:
        print('This file doesn\'t exist')

# input = 'input'
# output = 'output'

if "--h" in args:
    help.read()

if "--i" in args:
    x = args.index("--i")
    input = args[x+1]

if "--o" in args:
    y = args.index("--o")
    output = args[y+1]




if "--filter" in args:
    z = args.index("--filter")
    filters = args[z + 1]
    filters_list = filters.split('|')


if "--log-file" in args:
    y = args.index("--log-file")
    y += 1
    if args[y] == "image.log":
        log.dump_log()
    else:
        print("Incorrect file name")



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
    log.log("test")
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

    src_files = os.listdir(input)
    for file_name in src_files:
        full_file_name = os.path.join(input, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, output)

    for img in listOfFiles:
        out = output + img
        # nb.transnb(f'{input}/{img}', out)
        # blur.transblur(f'{output}/{img}', 5, out)
        # dilate.transdilate(f'{output}/{img}', out)

        for fltr in filters_list:
            if ':' in fltr:
                param = fltr.split(':')
                print(f'FLTR IS {fltr} ')
            if 'grayscale' in filters_list:
                print('GREY <--->')
                nb.transnb(f'{input}{img}', out)
                print(f'{input}{img}')
                input = output
                log.log(img + " grey")
            if 'blur' in fltr:
                param_blur = fltr.split(':')
                print(f'BLUR {img} ----->{param_blur}')
                nbr = int(param_blur[1])
                # print(f'BLURED <-----> {nbr}')
                blur.transblur(f'{input}{img}', int(nbr), out)
                print(f'{input}{img}')
                input = output
                log.log(img + " blured")
            if 'dilate' in fltr:
                param_dilate = fltr.split(':')
                print(f'DILATE ------> {param_dilate}')
                nbr = int(param_dilate[1])
                # print(f'<------> {nbr}')
                dilate.transdilate(f'{input}{img}', nbr, out)
                print(f'{input}{img}')
                input = output
                log.log(img + " dilated")

except FileNotFoundError:
    if "--h" not in args:
        print('Please enter an input path with -i <path>')



