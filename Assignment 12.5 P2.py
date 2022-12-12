# In this assignment you will write a Python program that expands on
# http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files
# below, extract the href= vaues from the anchor tags, scan for a
# tag that is in a particular position relative to the first name
# in the list, follow that link and repeat the process a number of
# times and report the last name you find.

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link.
# Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah

# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Daryl.html
# Find the link at position 18 (the first name is 1). Follow that link.
# Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: C

#######################################################

# From Julian to Julian, remember to run "py -m pip install beautifulsoup4"
# and "py -m pip install soupsieve" if shows errors

# Just ant attempt to clear the CMD console
import os
os.system('cls')

#######################################################

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# (Better last version from https://pypi.org/project/beautifulsoup4/)
# and unzip it in the same directory as this file

#import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Variables to complete the assigment
Position = 18
Repetitions = 7
url = "http://py4e-data.dr-chuck.net/known_by_Daryl.html"#input('Enter - ')

for repetition in range(0, Repetitions):

    html = urlopen(url, context=ctx).read() # Plan A
    #html = urllib.request.urlopen(url, context=ctx).read() # Plan B
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')

    # Espacio de testeo
    #print(html)
    #print("\n")
    #print(soup)
    #print("\n")
    #print(tags)
    #print("\n")

    print("Retrieving: " + url)

    # <li style="margin-top: 7px;"><a href="http://py4e-data.dr-chuck.net/known_by_Montgomery.html">Montgomery</a></li>

    i = 1
    for tag in tags:
        # Look at the parts of a tag
        #print(tag.get('href', None))
        #print('TAG:', tag)
        #print('Contents:', tag.contents[0]) #This is the data we need
        #print('Attrs:', tag.attrs)

        if i == Position:
            url = tag.get('href', None)
            newName = tag.contents[0]
            break
        i = i + 1

    #print(newName)
print("Required name is: " + newName)
