def isPal( str ):
    beg = 0
    end = len(str)
    while (beg < end):
        if (str[beg].lower() != str[end-1].lower()):
            return False;
        beg += 1
        end -= 1
    return True

f = open('input.txt', 'r')
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
