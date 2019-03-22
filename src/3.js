/* Given the root to a binary tree, implement serialize(root), which serializes the tree
into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left' */

class Node {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }

  serialize() {
    this.treeComponents = [];

    const serializor = (node) => {
      if (node) {
        this.treeComponents.push(node.val);
        serializor(node.left);
        serializor(node.right);
      } else this.treeComponents.push('#');
    };
    serializor(this);
    return this.treeComponents.join(' ');
  }

  static deserialize(serialTree) {
    const deserializor = (treeComponents) => {
      const comp = treeComponents.shift();
      if (comp === '#') return null;
      const node = new Node(comp);
      node.left = deserializor(treeComponents);
      node.right = deserializor(treeComponents);
      return node;
    };
    return deserializor(serialTree.split(' '));
  }
}

const node = new Node('root', new Node('left', new Node('left.left')), new Node('right'));
console.assert(Node.deserialize(node.serialize()).left.left.val === 'left.left');
