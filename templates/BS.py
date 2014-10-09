import google
from google import search
import urllib2
from bs4 import BeautifulSoup

r = []
for url in search("who played batman?", tld="com", num = 30, pause=0):
    r.append(url)
html = []
for x in r:
    response = urllib2.urlopen(x)
    print response.info()
   # soup = BeautifulSoup(response)
    #print(soup.prettify())
    
    
