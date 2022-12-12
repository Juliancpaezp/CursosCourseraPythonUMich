# In this assignment you will write a Python program to use urllib to read the
# HTML from the data files below, and parse the data, extracting numbers and
# compute the sum of the numbers in the file

# Sample data:
# http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data:
# http://py4e-data.dr-chuck.net/comments_1688704.html (Sum ends with 20)

# From Julian to Julian, remember to run "py -m pip install beautifulsoup4"
# and "py -m pip install soupsieve" if shows errors

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

url = "http://py4e-data.dr-chuck.net/comments_1688704.html"#input('Enter - ')
html = urlopen(url, context=ctx).read() # Plan A
#html = urllib.request.urlopen(url, context=ctx).read() # Plan B
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')

# Espacio de testeo
#print(html)
#print("\n")
#print(soup)
#print("\n")
#print(tags)
#print("\n")

total = 0

for tag in tags:
    # Look at the parts of a tag
    #print(tag.get('href', None))
    #print('TAG:', tag)
    #print('Contents:', tag.contents[0]) #This is the data we need
    #print('Attrs:', tag.attrs)

    total = total + int(tag.contents[0])

print(total)
