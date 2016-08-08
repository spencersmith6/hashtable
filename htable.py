"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

"""Return a list of nbuckets lists"""
def htable(nbuckets):
    NBuckets = nbuckets
    buckets = [[] for i in range(NBuckets)]
    return buckets


"""
Return a hashcode for strings and integers; all others return None
For integers, just return the integer value.
For strings, perform operation h = h*31 + ord(c) for all characters in the string
"""
def hashcode(o):
    h = 0
    if type(o) == type("String"):
        for c in range(len(o)):
            h =h * 31 + ord(o[c])
        return h
    elif type(o) == type(1):
        return o
    else:
        print "ERROR: Arg to hash not int or string"



def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the element within a specific bucket; the bucket is table[key].
    You have to linearly search the bucket.
    """


"""
Perform table[key] = value
Find the appropriate bucket indicated by key and then append value to the bucket.
If the bucket for key already has a key,value pair with that key then replace it.
Make sure that you are only adding (key,value) associations to the buckets.
"""

def htable_put(table, key, value):
    NBuckets = len(table)
    h = hashcode(key)
    b = h % NBuckets
    keyExist = False

    if table[b] != []:
        for x in range(len(table[b])):
            if table[b][x][0] == key:
                table[b][x] += (value,)
                keyExist = True
                break
        if keyExist == False:
            table[b].append((key, value))
    else:
        table[b].append((key, value))


"""
Return table[key].
Find the appropriate bucket indicated by the key and look for the association
with the key. Return the value (not the key and not the association!)
Return None if key not found.
"""
def htable_get(table, key):
    NBuckets = len(table)
    h = hashcode(key)
    b = h % NBuckets
    for assoc in table[b]:
        if key == assoc[0]:
            return assoc[1:]
    return None

    """
    Return a string representing the various buckets of this table. The output looks like:
	0000->
	0001->
	0002->
	0003->parrt:99
	0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """

def htable_buckets_str(table):
    returnString = ""
    for bucket in range(len(table)):
        returnString += str(bucket).zfill(3) +"->"
        for key in table[bucket]:
            returnString += " " + key[0] + ":"
            for value in range(1, len(key)):
                returnString += " " + str(key[value])
            returnString += ","
        returnString += "\n"
    return returnString



"""
Return what str(table) would return for a regular Python dict such as {parrt:99}.
The order should be bucket order and then insertion order in bucket.
The insertion order is guaranteed when you append to the buckets in htable_put().
"""
def htable_str(table):
    returnString = "{"
    for bucket in table:
        for key in bucket:
            returnString += " " + key[0] + ":"
            for value in range(1,len(key)):
                returnString += " " + str(key[value])
            returnString += ","
    return returnString







