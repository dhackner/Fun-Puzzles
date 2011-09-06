'''
@author: Dan Hackner <dhackner>

1x1 = 1
2x2 = 2
3x3 = 12
4x4 = 184
5x5 = 8512

This pattern is OEIS A007764 - number of nonintersecting (or self-avoiding) rook paths joining opposite corners of an n X n grid
(according to OEIS):
6x6 = 1262816
7x7 = 575780564
'''

from copy import deepcopy

gridSize = 4
gridDebug = False#True

# DRH | Note to self: This line is equivalent to nesting the list comprehensions,
# but [['x'] * gridSize] * gridSize DOESN'T work because the outer array
# doesn't make deep copies of the inner array =-/.
grid = [(['x'] * gridSize) for x in range(gridSize)]

def numPathsWithPathStepsInEachCell(ingrid, x=0, y=0, stepCounter=1):
    ingrid[x][y] = stepCounter
    if gridDebug:
        printGrid(ingrid)
    if x == y == (gridSize-1):
        if gridDebug:
            printGrid(ingrid, 1)
        return 1
    else:
        numCombinedPathsFromSurroundingCells = 0
        for (x2, y2) in getAvailableNextSteps(ingrid, x, y):
            numCombinedPathsFromSurroundingCells += numPathsWithPathStepsInEachCell(deepcopy(ingrid), x2, y2, stepCounter + 1)
	return numCombinedPathsFromSurroundingCells

def getAvailableNextSteps(g, x, y):
    if x-1 >= 0 and g[x-1][y] == 'x':
        yield (x-1, y)
    if x+1 < len(g) and g[x+1][y] == 'x':
        yield (x+1, y)
    if y-1 >= 0 and g[x][y-1] == 'x':
        yield (x, y-1)
    if y+1 < len(g[x]) and g[x][y+1] == 'x':
        yield (x, y+1)

def printGrid(g, success=0):
    if success:
	print '---SUCCESS---'
    for y in range(0, len(g[0])):
        for x in range(0, len(g)):
            print '%s ' % g[x][y],
        print ""
    if success:
	print '---SUCCESS---'
    print ""

print '=== Total number of paths: %s' % numPathsWithPathStepsInEachCell(grid)
