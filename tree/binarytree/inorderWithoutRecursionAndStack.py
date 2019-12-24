'''
1. Initialize current as root 
2. While current is not NULL
   If the current does not have left child
      a) Print current’s data
      b) Go to the right, i.e., current = current->right
   Else
      a) Make current as the right child of the rightmost 
         node in current's left subtree
      b) Go to this left child, i.e., current = current->left
      c) It is possible that you have already created a link and in that case you will get
        current's left subtree's rightmost node's right as current and you have to break link.

Time Complexity: 
O(n) If we take a closer look, we can notice that every edge of the tree is traversed at most two times. 
And in the worst case, the same number of extra edges (as input tree) are created and removed.
'''
from tree import Tree

def inorder(root):
    current = root
    while current:
        if current.left is None:
            print(current.key, end = " ")
            current = current.right
        else:
            p = current.left
            while p.right and p.right is not current:
                p = p.right

            if p.right:
                print(current.key, end = " ")
                p.right = None
                current = current.right
            else:
                p.right = current
                current = current.left

a = Tree(1)
a.left = Tree(2)
a.right = Tree(3)
a.left.left = Tree(4)
a.right.left = Tree(5)
a.right.right = Tree(6)

inorder(a)
print()
