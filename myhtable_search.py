# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words

"""
Build an index from word to set of document indexes
This does the exact same thing as create_index() except that it uses
your htable.  As a number of htable buckets, use 4011.
Returns a list-of-buckets hashtable representation.
"""
def myhtable_create_index(files):
    wordBook = htable(4011)

    fileIndex = 0
    for item in files:
        fileWords = set(words(get_text(item)))
        for word in fileWords:
            htable_put(wordBook,word, fileIndex)
        fileIndex += 1
    return wordBook


"""
This does the exact same thing as index_search() except that it uses your htable.
I.e., use htable_get(index, w) not index[w].
"""


def myhtable_index_search(files, index, terms):
    validTerms = []
    for term in terms:
        if htable_get(index, term)!= None:
            validTerms += [term]

    if len(validTerms)==0:
        return []

    overlap = set(htable_get(index, validTerms[0]))
    for word in validTerms:
        overlap = set(htable_get(index, word)) & overlap

    searchResults = []
    for i in list(overlap):
        searchResults += [list(files)[i]]

    return  searchResults