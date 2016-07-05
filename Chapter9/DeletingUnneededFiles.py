'''
This program walks through a folder tree and searches for execptionally large file (file size > 100MB)
'''
import os, send2trash

MaxSize = 1024*1024*100 #100MB

def deleteFile(path):
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            filePath = os.path.join(foldername, filename)
            if os.path.getsize(filePath) > MaxSize:
                print(filename + " is more than 100MB")
                send2trash.send2trash(filePath)

path = os.getcwd()
deleteFile(path)
