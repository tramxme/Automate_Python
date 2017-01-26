'''
This program goes to a photo-sharing site, searches for a category of photos
and then downloads all the resulting images
'''

import sys, re, os, requests, bs4

def downloadImage(siteURL, category):

    #Make a folder for the category
    os.makedirs(category, exist_ok=True)

    res = requests.get(siteURL + "/search?q=" + category)
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    reg = re.compile(r'(.*?)b(.jpg)$')
    #Find the list of all the images found
    images = soup.select('#imagelist img')
    for img in images:
        if img.get("alt") == "":
            src = img.get("src")
            mo = reg.search(src)
            if mo != None:
                newSrc = mo.group(1) + mo.group(2)
                newSrc = "https:" + newSrc

                #Save image to ./category
                imageFile = open(os.path.join(category, os.path.basename(newSrc)), "wb")
                res = requests.get(newSrc)
                res.raise_for_status
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()

    print("Done!!! =D")


url = "https://imgur.com/"
category = "progresspics"
downloadImage(url, category)
