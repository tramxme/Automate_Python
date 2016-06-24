import os, glob, re

def main(path, pattern):
    path += "*.txt"
    files = glob.glob(path)

    for i in range(len(files)):
        f = open(files[i])
        for line in f.readlines():
            text = re.findall(pattern, line)
            if (len(text) > 0):
                print("File " + os.path.basename(files[i]) + " - Match found: " + str(text))
        print()

path = "/Chapter8"
pattern = r'(\(?\d{3}\)?)(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})'
main(path, pattern)
