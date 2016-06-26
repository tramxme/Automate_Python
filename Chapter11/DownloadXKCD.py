import requests, bs4, os

def main():
    url = "http://xkcd.com/"
    os.makedirs('xkcd', exist_ok=True)
    #load the XKCD homepage
    while not url.endswith("#"):
        #Download the page.
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)

        # TODO: Find the URL of the comic image.
        comic = soup.select("#comic img")
        if comic == []:
            print("Could not find the comic image")
        else:
            try:
                # TODO: Download the image.
                comicURL = "http:" + comic[0].get("src")
                print("Beginning downloading...." + url)
                res = requests.get(comicURL)
                res.raise_for_status()
            except requests.exceptions.MissingSchema:
                #Skip this comic
                prevLink = soup.select('a[rel="prev"]')[0]
                url = "http://xkcd.com/" + prevLink.get("href")
                continue

        # TODO: Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        # TODO: Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = "http://xkcd.com/" + prevLink.get("href")

    print('Done.')


main()


