'''
Like arrays, Linked List is a linear data structure. Unlike arrays, linked list
elements are not stored at contiguous location; the elements are linked using
pointers.
'''

'''
The first node of the linked list is called Head. Each node has some data and
points to next node. The last node points to null.
For example:
head -> 1 -> 2 -> 3 -> 4 -> 5 -> null
'''

'''
Representation:
A linked list is represented by a pointer to the first node of the linked list.
The first node is called head. If the linked list is empty, then value of head is NULL.
Each node in a list consists of at least two parts:
1) data
2) Pointer (Or Reference) to the next node
'''

'''
Below is a python implementation for linked list and its node
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert new node at head
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # Append a new node at end of list
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            # if list is empty make new node as head
            self.head = newNode
        else:
            # if list is not empty find last node and do lastNode.next = newNode
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertAfter(self, prevNode, data):
        if prevNode:
            newNode = Node(data)
            newNode.next = prevNode.next
            prevNode.next = newNode

    def printList(self):
        current = self.head
        while current:
            print(current.data, end = " ")
            current = current.next
        print()

    def printFormatted(self):
        print("head ->", end = " ")
        current = self.head
        while current:
            print(current.data, end = " ")
            current = current.next
            print("->", end = " ")
        print("null")
        print

    # deletes first node where data == key
    def deleteKey(self, key):
        node, prevNode = self.head, None
        while node and node.data != key:
            prevNode = node
            node = node.next
        # if node is none means there is no matching node
        if node:
            # if prevNode is None means node is head
            if prevNode:
                prevNode.next = node.next
            else:
                self.head = node.next

    # deletes node at index. index is zero based
    def deleteAt(self, index):
        if index < 0:
            raise Exception("index cannot be less than zero")
        node, prevNode = self.head, None
        while node and index != 0:
            prevNode = node
            node = node.next
            index -= 1
        # if node is none means index is out of bounds
        if node:
            # if prevNode is None means node is head
            if prevNode:
                prevNode.next = node.next
            else:
                self.head = node.next

    def deleteAll(self):
        while self.head:
            self.deleteAt(0)

if __name__ == "__main__":
    l = LinkedList()
    l.push(1)
    l.append(2)
    l.append(4)
    l.append(5)
    l.insertAfter(l.head.next, 3)
    l.deleteAll()
    l.printFormatted()
