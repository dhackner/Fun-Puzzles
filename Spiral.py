'''
Created on Nov 12, 2011

@author: dhackner
'''
m0 = [[]]
m1 = [[ 1, 14, 13, 12],
          [ 2, 15, 20, 11],
          [ 3, 16, 19, 10],
          [ 4, 17, 18,  9],
          [ 5,  6,  7,  8]]
m2 = [[ 1, 16, 15, 14],
          [ 2, 17, 24, 13],
          [ 3, 18, 23, 12],
          [ 4, 19, 22, 11],
          [ 5, 20, 21, 10],
          [ 6,  7,  8,  9]]

# DRH | Prefer iterating through the matrix vs. destructing it on each pass
#     | also, this would be a good opportunity for a generator
def consumeRectangle((sX, sY), (eX, eY), matrix):
    if sX <= eX and sY <= eY:
        for x in range(sX, eX):
            print matrix[x][sY]
        for y in range(sY, eY):
            print matrix[eX][y]
        for x in range(eX, sX, -1):
            print matrix[x][eY]
        for y in range(eY, sY, -1):
            print matrix[sX][y]
        consumeRectangle((sX+1,sY+1), (eX-1,eY-1), matrix)



matrix = m0
length = len(matrix)
if length == 0:
    exit() # Nothing to print

height = len(matrix[0])
consumeRectangle((0,0), (length-1,height-1), matrix)

matrix = m1
length = len(matrix)
if length == 0:
    exit() # Nothing to print

height = len(matrix[0])
consumeRectangle((0,0), (length-1,height-1), matrix)

matrix = m2
length = len(matrix)
if length == 0:
    exit() # Nothing to print

height = len(matrix[0])
consumeRectangle((0,0), (length-1,height-1), matrix)



"""
This can definitely be rewritten somehow using matrix transposes. It'd be trivial using a language like Octave...
matrix[:,0]
matrix[length-1][1:]
matrix[1:-1,height-1][::-1]
matrix[0,1:][::-1]
matrix[1:,1][:-1]
matrix[length-2][2:-1]
matrix[1:-2,height-2][::-1]
matrix[0,1:][::-1]
"""