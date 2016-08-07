import os
import re
import string
import sys, os



def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    fileReturn = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            fileReturn.append(os.path.join(path, name))
    return fileReturn


def get_text(fileName):
    f = open(fileName)
    s = f.read()
    f.close()
    return s


"""
Given a string, return a list of words normalized as follows.
Split the string to make words first by using regex compile() function
and string.punctuation + '0-9\\r\\t\\n]' to replace all those
char with a space character.
Split on space to get word list.
Ignore words < 3 char long.
Lowercase all words
"""
def words(text):

    regex = re.compile('[' + string.punctuation + '0-9\\r\\t\\n' + ']')
    clean = regex.sub(' ', text)
    clean = clean.split()
    clean = [word for word in clean if len(word)>3]
    clean = [w.lower() for w in clean]
    return clean



def preview(qfile):
    f = open(qfile)
    text = f.read()
    lines = text.splitlines()
    finaltext = lines[6:11]

    return "\n".join(finaltext)




"""
Given a list of fully-qualifed filenames, return an HTML file
that displays the results and up to 2 lines from the file.
Return at most 100 results.  Arg terms is a list of string terms.
"""

def results(docs, terms):
    docCount = len(docs)

    templateTop ="""
    <html>
    <body>
    <h2>Search results for <u> %s </u> in %d files</h2>
    """

    templateMid ="""
        <p><a href='%s' >%s</a><br> %s <br><br>
    """


    htmlBottom = """
        </body>
    </html>
    """

    htmlTop = templateTop % (" ".join(terms), docCount)

    htmlMid = ""
    for i in range(len(docs)):
        currentDoc = docs[i]
        sample = preview(docs[i])
        htmlMid += templateMid % (currentDoc, currentDoc, sample)

    htmlCode = htmlTop + htmlMid + htmlBottom
    htmlFile = open("/tmp/results.html", "w")
    htmlFile.write(htmlCode)

    return htmlCode





def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]




#####################################################
################## PLAYGROUND ########################
#####################################################
#path = "/Users/spencersmith/data/berlitz1"

#afile = filelist("/Users/spencersmith/data")[15]
#allFiles = filelist("/Users/spencersmith/data")
#onlyfilenames = filenames(onlyfiles)
#results(afile, "test")




#print(words(get_text(afile)))
#print words("hello")

#get_text("/Users/spencersmith/testfile.txt")

