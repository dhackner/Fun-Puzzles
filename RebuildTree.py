#!/usr/bin/env python

"""Given two arrays representing the inorder and postorder traversals of a binary tree 
with unique elements, rebuild the tree."""

__author__ = "Dan Hackner"
__maintainer__ = "Dan Hackner"
__email__ = "dan.hackner@gmail.com"
__status__ = "Production"

class Node:
    def __init__(self, val, l, r):
        self.value = val
        self.left = l
        self.right = r 

    def __str__(self):
        return_string = ''
        if self.left != None:
            return_string += self.left.__str__()
        return_string += self.value
        if self.right != None: 
            return_string += self.right.__str__()
        return return_string

"""Example:

       A
     /   \
    B     C
  /  \      \
 D    E      F
     /
    G

"""

inorder = ['D', 'B', 'G', 'E', 'A', 'C', 'F']
postorder = ['D', 'G', 'E', 'B', 'F', 'C', 'A']

def recreate_tree(inorder, postorder):
    if len(inorder) == len(postorder) == 0:
        return None
    splitting_letter = postorder[-1]
    split_index = inorder.index(splitting_letter)
    # The recursion splits inorder based on knowing that the last letter of a
    # postorder must be a parent node. The two children come from Recursing
    # with the split of the inorder, and a matching set of postorder. 
    # i.e. inorder=[1,2,3,4] postorder=[1,3,4,2] so we know that the
    # 2 is a parent; when we split the inorder on 2 we learn that 1 is a
    # left child and [3,4] are a right child. We can thus recurse 
    # with ([1], [1]) and ([3,4], [3,4]). Critical to skip the consumed
    # 'splitting letter' on each (2 in this case).
    return Node(splitting_letter,
            recreate_tree(inorder[0:split_index], postorder[0:split_index]),
            recreate_tree(inorder[split_index+1:], postorder[split_index:-1]))

print recreate_tree(inorder, postorder)
