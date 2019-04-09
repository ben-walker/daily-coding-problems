'''
Given two singly linked lists that intersect at some point, find the
intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return
the node with value 8.

In this example, assume nodes with the same value are the exact same node
objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and
constant space.
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if not self.head:
            self.head = node
            return

        p = self.head
        while p.next:
            p = p.next
        p.next = node

    def show(self):
        p = self.head
        while p:
            print(f'-> {p.val} ', end='')
            p = p.next
        print()

    def intersect(self, compList):
        p = self.head
        q = compList.head
        while p and q:
            if p.val == q.val:
                return p.val
            p = p.next
            q = q.next

B = LList()

A = LList()
A.insert(Node(3))
A.insert(Node(7))
A.insert(Node(8))
A.insert(Node(10))

B = LList()
B.insert(Node(99))
B.insert(Node(1))
B.insert(Node(8))
B.insert(Node(10))

# Testing

assert A.intersect(B) == 8
