'''
Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string back
into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    def _serializer(node, components=None):
        if components is None:
            components = []
        if node is not None:
            components.append(node.val)
            _serializer(node.left, components)
            _serializer(node.right, components)
        else:
            components.append('#')
    components = []
    _serializer(root, components)
    return ' '.join(components)


def deserialize(s):
    def _deserializer(components):
        nodeVal = components.pop(0)
        if nodeVal == '#':
            return None
        node = Node(nodeVal)
        node.left = _deserializer(components)
        node.right = _deserializer(components)
        return node
    return _deserializer(s.split(' '))

# Testing
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
