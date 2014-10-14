import re, collections, types, urllib
from collections import Counter
from operator import itemgetter 

def findNames(text, iterating = False):
    import enchant
    """
    Finds the frequency of full names in text.
    Takes ~1.2 seconds to parse a string of length 6488634 (http://norvig.com/big.txt)

    Args:
      text (string): string object or iterable composed of strings
      iterating (boolean, optional): changes depending on whether text is a string or iterable, do not change.

    Returns:
      List: made of tuples. First element of tuple is the name, second element is the frequency. The list is ordered by frequency.

    Raises:
      TypeError: If 'text' is not a string or iterable of strings.

    """
    convert = lambda(lst): sorted(list(Counter(lst).items()), key = itemgetter(1), reverse = True)

    if isinstance(text, collections.Iterable) and not isinstance(text, types.StringTypes):
        names = []
        for elem in text:
            names.extend(findNames(elem, iterating = True))
        return convert(names)

    if isinstance(text, str):
        d = enchant.Dict("en_us")
        pattern = "[^The]((([A-Z][a-z]+)|M([rs]|rs)\.|Dr\.)((\s[A-Z]\.)?\s[A-Z][a-z]+-?[A-Z]?[a-z]+)+)"
        result = [name[0] for name in re.findall(pattern, text)]
        inDict = lambda(word): any([d.check(part) for part in word.split(' ')])
        nameList = [name for name in result if not inDict(name)]
        if iterating:
            return nameList
        return convert(nameList)

    raise TypeError("Input must a string or an iterable object composed of strings.")


###################################################
## If you can't install enchant, use this. It will return a far longer list because it
## probably doesn't filter as well, so just trim it down a bit
##################################################

def altFindNames(text, iterating = False):
    convert = lambda(lst): sorted(list(Counter(lst).items()), key = itemgetter(1), reverse = True)

    if isinstance(text, collections.Iterable) and not isinstance(text, types.StringTypes):
        names = []
        for elem in text:
            names.extend(findNames(elem, iterating = True))
        return convert(names)

    if isinstance(text, str):
        pattern = "[^The]((([A-Z][a-z]+)|M([rs]|rs)\.|Dr\.)((\s[A-Z]\.)?\s[A-Z][a-z]+-?[A-Z]?[a-z]+)+)"
        result = [name[0] for name in re.findall(pattern, text)]
        if iterating:
            return result
        return convert(result)

    raise TypeError("Input must a string or an iterable object composed of strings.")

##################################################
##################################################

def inDict(name):
    text2 = open("/usr/share/dict/words", "r")
    words = text2.read()
    dicte = words.split("\n")
    text2.close()
    parts = name.split(' ')
    for part in parts:
        if part.lower() in dicte:
            continue
        else: 
            return False
    return True

    



