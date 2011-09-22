#!/usr/bin/env python

'''Find the longest palindrome in a text file.'''

__author__ = "Dan Hackner"
__maintainer__ = "Dan Hackner"
__email__ = "dan.hackner@gmail.com"
__status__ = "Production"

def isPal(inputString):
    beg = 0
    end = len(inputString)
    while (beg < end):
        if (inputString[beg].lower() != inputString[end-1].lower()):
            return False
        beg += 1
        end -= 1
    return True

f = open('input.txt', 'r') # for a reasonably sized file
text = f.read()
length = len(text)

while (length > 0):
    beg = 0
    end = length    
    while (end <= len(text)):
        s = text[beg:end]
        if (isPal(s)):
            print(s)
            length = 0 # breaks out since we're going from the largest to smallest possible strings, thus nothing bigger will be found 
        beg += 1
        end += 1
    length -= 1
