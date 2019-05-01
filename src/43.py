'''
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there
are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no
elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
'''


class Stack(object):
    def __init__(self):
        self.elements = []

    def push(self, val):
        self.elements.append(val)

    def pop(self):
        return self.elements.pop()

    def max(self):
        return max(self.elements)

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.pop()
print(stack.max())
