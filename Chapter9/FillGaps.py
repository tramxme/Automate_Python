'''
This program find all files with a given prefix and locates any gaps in the numbering
(such as if there is spam001.txt and spam003.txt but no spam002.txt). This program will
rename all later files to fill this gap
'''

import os, re, shutil

def fillGaps(prefix, ext, path=""):
    if path == "":
        path = os.getcwd()

    os.chdir(path)

    reg = re.compile(r'^%s(\d+)' % prefix)
    numList = []

    for filename in os.listdir():
        if filename.endswith(ext):
            mo = reg.search(filename)
            if mo != None:
                numList.append(int(mo.group(1)))

    n = 1
    l = max(len(str(v)) for v in numList)
    if l < 3:
        l = 3

    for filename in os.listdir():
        if filename.endswith(ext):
            mo = reg.search(filename)
            if mo == None:
                while True:
                    if n not in numList:
                        numList.append(n)
                        break
                    else:
                        n += 1
                newName = prefix + str(n).zfill(l) + ext
                shutil.move(filename, os.path.join(os.getcwd(), newName))

path = "testFolder"
prefix = "spam"
ext = ".txt"
fillGaps(prefix, ext, path)

