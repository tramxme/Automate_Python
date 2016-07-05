'''
This program walks through a folder tree and searches for files with certain extension
(such as .pdf or .jpg). It copies these files from whatever location they are in to a new folder
'''

import os, shutil

def selectCopy(ext, path=""):

    if path == "":
        path = os.getcwd()

    #Create a new folder to copy to
    newFolder = "CopyFolder"
    os.makedirs(newFolder, exist_ok=True)

    for folder, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if os.path.basename(filename).endswith(ext):
                #Copy the file to a new location
                shutil.copy(os.path.join(folder, filename), newFolder)

selectCopy("pdf")
