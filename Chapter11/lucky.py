import sys, webbrowser, requests, pyperclip, bs4

#Read command line arguments from sys.argv
if (len(sys.argv) > 1):
    search = " ".join(sys.argv[1:])
else:
    search = pyperclip.paste()
res = requests.get("https://www.google.com/search?q=" + search)
try:
    res.raise_for_status()
except Exception as ex:
    print("There was a problem: %s" % ex)

#Fetch the search result page with the requests module
soup = bs4.BeautifulSoup(res.text)

#Find the links to each search result
linkElems = soup.select(".r a")

#Open the web browser
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open("https://google.com" + linkElems[i].get('href'))
