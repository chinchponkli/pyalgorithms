'''
Height of a generic tree from parent array

We are given a tree of size n as array parent[0..n-1] where every index i in parent[] represents a node 
and the value at i represents the immediate parent of that node. For root node value will be -1. 
Find the height of the generic tree given the parent links.
'''
from graph import Graph

def height(parentArray):
    levels = [0] * len(parentArray)
    # Convert to graph
    for i in range(0, len(parentArray)):
        if parentArray[i] != -1:
            levels[i] = levels[parentArray[i]] + 1
    print(max(levels))

parentArray = [1, -1, 1, 1, 3, 0, 0, 2]
height(parentArray)