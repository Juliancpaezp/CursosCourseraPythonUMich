# 7.1 Write a program that prompts for a file name, then opens
# that file and reads through the file, and print the contents
# of the file in upper case. Use the file words.txt to produce
# You can download the sample data at
# the output below.
# http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
FileName = input("Enter file name: ")
#FileName =  "words.txt"

FileHandle = open(FileName)

for line in FileHandle:
    line = line.upper()
    line = line.strip()
    print(line)
