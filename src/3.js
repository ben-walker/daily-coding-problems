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

/* Implementation */
const nullNode = '#';

class Node {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }

  serialize() {
    const serializor = (node) => {
      if (node) {
        this.treeElements.push(node.val);
        serializor(node.left); // serialize the entire left branch...
        serializor(node.right); // before serializing the right branch
      } else this.treeElements.push(nullNode); // null node found
    };

    this.treeElements = []; // array of serialized tree elements
    serializor(this);
    return this.treeElements.join(' ');
  }

  static deserialize(serialTree) {
    const deserializor = (treeElements) => {
      const element = treeElements.shift();
      if (element === nullNode) return null;
      const node = new Node(element); // form a new node from the serialized value
      // build this new node's left and right branches
      node.left = deserializor(treeElements);
      node.right = deserializor(treeElements);
      return node;
    };

    return deserializor(serialTree.split(' '));
  }
}

/* Testing */
const node = new Node('root', new Node('left', new Node('left.left')), new Node('right'));
console.assert(Node.deserialize(node.serialize()).left.left.val === 'left.left');
