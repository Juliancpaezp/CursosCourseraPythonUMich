# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL
# using urllib and then parse and extract the comment counts from the
# XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where
# we give you the sum for your testing and the other is the actual data
# you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1688706.xml (Sum = 2710)

#######################################################

# From Julian to Julian, remember to run "py -m pip install beautifulsoup4"
# and "py -m pip install soupsieve" if shows errors

# Just ant attempt to clear the CMD console
import os
os.system('cls')

#######################################################

#import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1688706.xml"#input('Enter - ')

print('Retrieving', url)
url = urllib.request.urlopen(url, context=ctx)

data = url.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())

tree = ET.fromstring(data)
# print(tree)

results = tree.findall('.//count')#.text
# print(results)

total = 0
for result in results:
    #print(result.text)
    total = total + int(result.text)

print("Sum:", total)
