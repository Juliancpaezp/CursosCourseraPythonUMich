# In this assignment you will write a Python program that will
# prompt for a URL, read the JSON data from that URL using
# urllib and then parse and extract the comment counts from
# the JSON data, compute the sum of the numbers in the file
# and enter the sum below:
# We provide two files for this assignment. One is a sample
# file where we give you the sum for your testing and the
# other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1688707.json (Sum ends with 20)

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

import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://py4e-data.dr-chuck.net/comments_1688707.json"#input('Enter - ')

print('Retrieving', url)
urlHandler = urllib.request.urlopen(url, context=ctx)

data = urlHandler.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

info = json.loads(data)

print(info['note'])

# Line necesary to acces comments in JSON file and discard the note
info = info['comments']

print('Count:', len(info))
total = 0

for item in info:
    #print(item)
    #print('Name', item['name'])
    #print('Count', item['count'])
    total = total + int(item['count'])

print("Sum:",total)
