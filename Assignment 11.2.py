# In this assignment you will read through and parse a file
# with text and numbers. You will extract all the numbers in
# the file and compute the sum of the numbers.

# TestSample.txt -> 27486
# regex_sum_42.txt -> 445833
# regex_sum_1688702.txt -> __274__946

import os
os.system('cls')


import re

FileHandle = open("regex_sum_1688702.txt")

totalSum = 0

for linea in FileHandle:
    ListsOfNumbersFound = re.findall('[0-9]+',linea)
    #print(ListsOfNumbersFound)
    for number in ListsOfNumbersFound:
        #print(number)
        totalSum = totalSum + int(number)
print(totalSum)
