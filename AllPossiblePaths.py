#!/usr/bin/env python

"""Number of nonintersecting paths in an n X n grid from (0, 0) to (n, n)

1x1 = 1
2x2 = 2
3x3 = 12
4x4 = 184
5x5 = 8512

This pattern is OEIS A007764 - number of nonintersecting (or self-avoiding) rook paths joining opposite corners of an n X n grid
(according to OEIS):
6x6 = 1262816
7x7 = 575780564
"""

from copy import deepcopy

__author__ = "Dan Hackner"
__maintainer__ = "Dan Hackner"
__email__ = "dan.hackner@gmail.com"
__status__ = "Production"

gridSize = 4
debug = False#True

# DRH | Note to self: This line is equivalent to nesting the list comprehensions,
# but [['x'] * gridSize] * gridSize DOESN'T work because the outer array
# doesn't make deep copies of the inner array =-/.
grid = [(['x'] * gridSize) for x in range(gridSize)]

def num_paths(ingrid, x=0, y=0, step_counter=1):
    """Number of total nonintersecting paths from (0,0) to (n,n)."""
    ingrid[x][y] = step_counter
    if debug:
        print_grid(ingrid)
    if x == y == (gridSize-1):
        if debug:
            print_grid(ingrid, 1)
        return 1
    else:
        total_paths_cell = 0 # Number of combined paths from surrounding cells
        for (x2, y2) in get_steps(ingrid, x, y):
            total_paths_cell += num_paths(deepcopy(ingrid), x2, y2, step_counter + 1)
        return total_paths_cell

def get_steps(g, x, y):
    """Yield all steps from this position that haven't already been used."""
    if x-1 >= 0 and g[x-1][y] == 'x':
        yield (x-1, y)
    if x+1 < len(g) and g[x+1][y] == 'x':
        yield (x+1, y)
    if y-1 >= 0 and g[x][y-1] == 'x':
        yield (x, y-1)
    if y+1 < len(g[x]) and g[x][y+1] == 'x':
        yield (x, y+1)

def print_grid(g, success=0):
    if success:
        print '---SUCCESS---'
    for y in range(0, len(g[0])):
        for x in range(0, len(g)):
            print '%s ' % g[x][y],
        print ""
    if success:
        print '---SUCCESS---'
    print ""

print '=== Total number of paths: %s' % num_paths(grid)
