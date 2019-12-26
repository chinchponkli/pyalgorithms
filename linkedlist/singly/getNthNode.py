'''
Write a function that takes a linked list and an integer index and returns
the node at that index position.
Input:  1->10->30->14,  index = 2
Output: 30
For index = 5, return null. Please see that the list is zero indexed.
'''
from linkedlist import Node
from linkedlist import LinkedList

def getNthNode(node, n):
    if n < 0:
        raise Exception("Index cannot be negative")
    while node and n != 0:
        node = node.next
        n -= 1
    return node

a = LinkedList()
a.append(1)
a.append(10)
a.append(30)
a.append(14)
a.printList()
for i in range(a.size() + 1):
    nthNode = getNthNode(a.head, i)
    print(nthNode.data if nthNode is not None else None)
#nthNode = getNthNode(a.head, -1)
#print(nthNode.data if nthNode is not None else None) - will raise exceptions
