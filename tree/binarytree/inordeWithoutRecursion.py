'''
1) Create an empty stack s.
2) Initialize current node as root
3) Push the current node to s and set current = current->left until current is None.
4) If current is None and stack is not empty then
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
Time Complexity: O(n)
Space Complexity: O(n) - size of stack.
'''
from tree import Tree

def inorder(root):
    current = root
    s = []              
    while True:
        if current:
            s.append(current)
            current = current.left
        else:
            if len(s) == 0:
                break
            else:
                node = s.pop(len(s) - 1)
                print(node.key, end = " ")
                current = node.right
            
a = Tree(1)
a.left = Tree(2)
a.right = Tree(3)
a.left.left = Tree(4)
a.right.left = Tree(5)
a.right.right = Tree(6)

inorder(a)
print()
