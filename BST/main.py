class node:
  def __init__(self, k=0, p=None, l=None, r=None) -> None:
    self.key = k
    self.left = l
    self.right = r
    self.parent = p


class bst:
  def __init__(self, root_key=0) -> None:
    self.root = node(root_key)

  def search(self, x: node, key: int):
    p = x.parent
    tmp = x

    while tmp != None and tmp.key != key:
      p = tmp

      if key < tmp.key:
        tmp = tmp.left
      else:
        tmp = tmp.right

    if tmp == None:
      return p

    return tmp

  def minimum(self, x: node):
    tmp = x
    while tmp.left != None:
      tmp = tmp.left
    return tmp

  def maximum(self, x: node):
    tmp = x
    while tmp.right != None:
      tmp = tmp.right
    return tmp

  def successor(self, x: node):
    if x.right != None:
      return self.minimum(x.right)

    p: node = x.parent
    tmp = x

    while p != None and p.right == tmp:
      tmp = p
      p = p.parent

    return p

  def insert(self, key: int):
    possible_parent = self.search(self.root, key)
    if possible_parent.key == key:
      return

    new_node = node(key, possible_parent)

    if possible_parent == None:
      self.root = new_node
    elif new_node.key < possible_parent.key:
      possible_parent.left = new_node
    else:
      possible_parent.right = new_node

  def replace(self, target: node, replacement: node):
    if self.root == target:
      self.root = replacement
    elif target.parent.left == target:
      target.parent.left = replacement
    else:
      target.parent.right = replacement

    if replacement != None:
      replacement.parent = target.parent

  def delete(self, target: node):
    if target.left == None:
      self.replace(target, target.right)
    elif target.right == None:
      self.replace(target, target.left)
    else:
      replacement: node = self.minimum(target.right)
      if replacement.parent != target:
        self.replace(replacement, replacement.right)
        replacement.right = target.right
        replacement.right.parent = replacement

      self.replace(target, replacement)
      replacement.left = target.left
      replacement.left.parent = replacement


tree = bst(3)
tree.insert(3)
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

# while tree.root != None:
#   tree.delete(tree.root)
# print('done')


def inorder_tree_walk(root: node):
  if root == None:
    return

  inorder_tree_walk(root.left)
  print(root.key)
  inorder_tree_walk(root.right)


inorder_tree_walk(tree.root)
