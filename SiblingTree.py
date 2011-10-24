#!/usr/bin/env python

"""Give each node a pointer to the next node to the right (null if to the end) for a balanced binary tree using const memory."""

__author__ = "Dan Hackner"
__maintainer__ = "Dan Hackner"
__email__ = "dan.hackner@gmail.com"
__status__ = "Production"

from collections import deque
from pprint import pprint

class Node:
    def __init__(self, val, l, r):
        self.value = val
        self.left = l
        self.right = r
        self.r_sibling = None

    def __str__(self):
        return_string = self.value
        if self.r_sibling != None:
            return_string += ' ->'+self.r_sibling.value
        return_string += ' /'
        if self.left != None:
            return_string += self.left.value
        return_string += ' \\'
        if self.right != None: 
            return_string += self.right.value
        return return_string + '\n' + self.left.__str__() + '\n' + self.right.__str__();

"""Example:

        A
    /      \
  B          C
    \       /  \
      D    E    F
            \
              G

Becomes:

        A
    /      \
  B     ->   C
    \       /  \
      D -> E -> F
            \
              G
"""

root = Node('A', Node('B', None, Node('D', None, None)), Node('C', Node('E', None, Node('G', None, None)), Node('F', None, None)))
q = [root, None]

while q:
    print [x.value if x else 'None' for x in q ]
    curr = q.pop(0)
    if curr != None:
        q.append(curr.left)
        q.append(curr.right)
        curr.r_sibling = q[0]
    elif q and q[-1] is not None: # To diverge away from an infinite loop
        q.append(None)

print '====='
print root
