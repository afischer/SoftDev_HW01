from Parser import altFindNames
import google
from google import search
import urllib 
from bs4 import BeautifulSoup


r = []
for url in search("When was the us created?", tld='com', lang='en', stop = 20):
    r.append(url)

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
        return text.encode('utf-8')

print altFindNames(txt(r))
#txt(r)




   
