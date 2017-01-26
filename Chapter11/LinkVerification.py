'''
This program takes in a URL of a web page. It will attempt to download every linked page
on the page. The program will flag any pages that have a 404 "Not Found" status code and
print them out as broken links
'''
import sys, webbrowser, requests, bs4, re, os
def verify():
    url = sys.argv[1]

    #Go to the provided url
    res = requests.get(url)
    if res.status_code != requests.codes.ok:
        print("There was a problem")
    else:
        #Fetch the page
        soup = bs4.BeautifulSoup(res.text)

        #Get all the links on the page
        linkElems = soup.select("a")
        #print(linkElems)
        for i in range(len(linkElems)):
            link = linkElems[i].get("href")
            if link != None:
                if link.startswith("//"):
                    link = "https:" + link
                elif link.startswith("#"):
                    link = url + link
                elif not link.startswith("http"):
                    g = re.search("^(http(.*?)\.(.*?)\/)", url)
                    link = g.group(1) + link

                res = requests.get(link)

                try:
                    res.raise_for_status()
                    print(link + " - " + linkElems[i].getText())
                except Exception as ex:
                    print(ex)


verify()
