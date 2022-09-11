# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.

#  http://data.pr4e.org/mbox-short.txt for test


import urllib.request

try:
    url = input('Enter a URL: ').lower()
    fhand = urllib.request.urlopen(url)
    dataTotal = ''
    for line in fhand:
        dataTotal += line.decode()
    print(dataTotal[:3000])
    print(len(dataTotal[:3000]))
except:
    print("an improperly formatted or non-existent URL")
