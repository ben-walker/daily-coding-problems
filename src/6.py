'''
An XOR linked list is a more memory efficient doubly linked list. Instead of
each node holding next and prev fields, it holds a field named both, which is
an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index)
which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you
have access to get_pointer and dereference_pointer functions that converts
between nodes and memory addresses.
'''

from operator import xor


class Node:
    def __init__(self, val):
        self.val = val
        self.both = None


class XorList:
    def __init__(self):
        self.head = None

    def add(self, element):
        element.both = xor(None, get_pointer(self.head))
        if self.head is not None:
            next = xor(None, self.head.both)
            self.head.both = xor(get_pointer(element), next)
        self.head = element

    def get(self, index):
        curr = self.head
        prev = None
        i = 0

        while curr is not None and i != index:
            next = xor(get_pointer(prev), curr.both)
            prev = curr
            curr = dereference_pointer(next)
            i += 1
        return curr if i == index else None
