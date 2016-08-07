# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from words import get_text, words

"""
Given a list of fully-qualified filenames, return a list of them
whose file contents has all words in terms as normalized by your words() function.
Parameter terms is a list of strings.
Perform a linear search, looking at each file one after the other.
"""
def linear_search(files, terms):
    returnFiles = []
    searchTerms = set(terms)
    for item in files:
        fileWords = set(words(get_text(item)))
        if(searchTerms < fileWords):
            returnFiles.append(item)


    return returnFiles






