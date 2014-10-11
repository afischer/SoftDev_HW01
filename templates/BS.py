import google
from google import search
import urllib 
from bs4 import BeautifulSoup
from sgmllib import SGMLParser

r = []
for url in search("who played batman?", tld='com', lang='en', stop = 10):
    r.append(url)


#html = []
#for x in r:

sock = urllib.urlopen("http://www.biography.com/people/groups/actors-who-played-batman") 
htmlSource = sock.read()  
sock.close()       
print htmlSource     
    


    
    
