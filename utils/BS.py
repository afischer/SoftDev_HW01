from Parser import altFindNames, findDates
import google
from google import search
import urllib 
from bs4 import BeautifulSoup

def txt(question):
    
    r = []
    for url in search(question, tld='com', lang='en', stop = 20):
        r.append(url)

    allText = ""
    for x in r: #gets the urls
        url = x
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, "html5lib")
        for script in soup(["script", "style","meta", "li"]):
            script.extract()    # rip it out
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        allText = allText + text.encode('utf-8') #this is all of the text in the websites

    results= []
    if question[:4] == "when":
        results = findDates(allText)
    else:
        results = altFindNames(allText)
    final = results[0]
    return final




   





   
