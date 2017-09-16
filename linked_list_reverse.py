"""
Linked Lists in Python

Taken from InterviewCake August 2016
"""


class LinkedListNode(object):
    """Singly Linked List Node"""

    def __init__(self, value):
        super(LinkedListNode, self).__init__()
        self.value = value
        self.next = None


# Build a singly linked list

a = LinkedListNode(5)
b = LinkedListNode(1)
c = LinkedListNode(9)

a.next = b
b.next = c





class Node:
    pointer = None

    def __init__(self, value):
        self.value = value

    def next(self):
        return self.pointer
