import google
from google import search
import urllib
from bs4 import BeautifulSoup

r = []
for url in search("who played batman?", tld='com', lang='en', stop = 10):
    r.append(url) ##gets urls

def txt(r):
    for x in r:
        url = x
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, "html5lib")
        for script in soup(["script", "style","meta", "li"]):
            script.extract()    # rip it out
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
    #    print text.encode('utf-8') + "\n_______________________________________________________________________________________\n"


print txt(r)
