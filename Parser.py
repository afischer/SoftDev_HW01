import enchant, re, collections, types, urllib
from bs4 import BeautifulSoup

#name parser, accepts a string or list of strings and returns a counter of the names. Later on I'll
#probably replace the Counter with something easier to deal with.
def findNames(text):
    names = [ ]
    if isinstance(text, collections.Iterable) and not isinstance(text, types.StringTypes):
        for elem in text:
            names.extend(findNames(elem))
    if isinstance(text, str):
        d = enchant.Dict("en_us")
        pattern = "[^The]((([A-Z][a-z]+)|M([rs]|rs)\.|Dr\.)((\s[A-Z]\.)?\s[A-Z][a-z]+-?[A-Z]?[a-z]+)+)"
        result = [name[0] for name in re.findall(pattern, text)]
        inDict = lambda(word): any([d.check(part) for part in word.split(' ')])
        names.extend([name for name in result if not inDict(name)])
    return collections.Counter(names)

#quick method to help get text from sites
def getSites(url):
    bs = BeautifulSoup(urllib.urlopen(url))
    return bs.get_text()

if __name__ == '__main__':
    test = str(getSites("http://en.wikipedia.org/wiki/Grigori_Perelman").encode('ascii', 'ignore').replace('\n', ''))
    test2 = str(getSites("http://en.wikipedia.org/wiki/Grigori_Perelman").encode('ascii', 'ignore').replace('\n', ''))
    testList = [test, test2]
    print "\n\n"
    print findNames(test)
    print "\n\n"
    print findNames(testList)

    
