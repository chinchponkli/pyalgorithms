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
