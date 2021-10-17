
from operator import truediv
from os import replace


class BSTNode:
  def __init__(self, key=0, left=None, right=None, parent=None) -> None:
    self.key = key
    self.left = left
    self.right = right
    self.parent = parent


class BinarySearchTree:
  # constructor
  def __init__(self, k=0) -> None:
    self.root = BSTNode(key=k)

  def find(self, root: BSTNode, key: int) -> BSTNode:
    if root == None or root.key == key:
      return root

    if root.key > key:
      if root.left != None:
        return self.find(root.left, key)
      return root

    if root.right != None:
      return self.find(root.right, key)

    return root

  # left descendant

  def left_descendant(self, curr: BSTNode) -> BSTNode:
    temp = curr
    while temp.left != None:
      temp = temp.left

    return temp

  # right ancestor
  def right_ancestor(self, curr: BSTNode) -> BSTNode:
    if curr.parent == None:
      return curr

    if curr.key < curr.parent.key:
      return curr.parent

    return self.right_ancestor(curr.parent)

  # next element in the sorted order
  def next(self, curr: BSTNode) -> BSTNode:
    if curr.right != None:
      return self.left_descendant(curr.right)

    return self.right_ancestor(curr)

  # insert a node with key k
  def insert(self, key: int):
    parent = self.find(self.root, key)
    if parent.key == key:
      return False

    child = BSTNode(key=key)

    if parent.key > key:
      parent.left = child

    else:
      parent.right = child

    child.parent = parent
    return True

  # replace nodes
  def __replace__(self, node, replacement):
    parent = node.parent
    left = node.left
    right = node.right

    # replace parent
    if parent == None:
      self.root = replacement
    else:
      if parent.key > node.key:
        parent.left = replacement
      else:
        parent.right = replacement

    if replacement != None:
      replacement.parent = parent
      # Replace left child
      if left != replacement:
        replacement.left = left
        if left != None:
          left.parent = replacement

        # replace the right child
        if right != replacement:
          replacement.right = right
          if right != None:
            right.parent = replacement

  # delete a node

  def __delete_node__(self, node: BSTNode):
    if node.right == None:
      self.__replace__(node, node.left)
      return

    else:
      nxt = self.next(node)

      nxtp = nxt.parent
      nxtr = nxt.right

      if nxtr != None:
        nxtr.parent = nxtp

      if nxtp == node:
        nxtp.right = nxtr
      else:
        nxtp.left = nxtr

      self.__replace__(node, nxt)

  # delete a node with key

  def delete(self, key: int):
    target = self.find(self.root, key)
    if target.key == key:
      self.__delete_node__(target)


tree = BinarySearchTree(5)
tree.insert(3)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(8)
tree.insert(6)
tree.insert(13)
tree.insert(10)
tree.insert(12)
tree.insert(11)
tree.insert(9)
tree.insert(17)
tree.insert(20)
tree.insert(15)
tree.insert(16)
tree.insert(14)
tree.delete(20)
tree.delete(13)
tree.delete(12)
tree.delete(5)

while tree.root != None:
  tree.__delete_node__(tree.root)
print('done')
