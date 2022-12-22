import math
import random
from typing import List


class node:
  def __init__(self, k=0, p=None, l=None, r=None) -> None:
    self.key = k
    self.parent = p
    self.left = l
    self.right = r
    self.height = 0


def inorder_tree_walk(root: node, walk: List[int]):
  if root == None:
    return

  inorder_tree_walk(root.left, walk)
  walk.append(root.key)
  inorder_tree_walk(root.right, walk)


class avl_tree:
  def __init__(self, root_key=0) -> None:
    self.root = node(root_key)
    self.size = 1

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

  def insert(self, key: int):
    potential_parent = self.search(self.root, key)
    if potential_parent.key == key:
      return

    self.size += 1
    new_node = node(key, potential_parent)
    new_node.height = 0
    if new_node.key < potential_parent.key:
      potential_parent.left = new_node
    else:
      potential_parent.right = new_node

    potential_parent.height = self.calc_height(potential_parent)

    self.balance(new_node)

  def min(self, x: node):
    tmp = x
    while tmp.left != None:
      tmp = tmp.left
    return tmp

  def max(self, x: node):
    tmp = x
    while tmp.right != None:
      tmp = tmp.right
    return tmp

  def successor(self, x: node):
    if x.right != None:
      return self.min(x.right)

    p = x.parent
    tmp = x

    while p != None and tmp == p.right:
      tmp = p
      p = p.parent

    return p

  def calc_height(self, x: node):
    lh = self.get_height(x.left)
    rh = self.get_height(x.right)

    return max(lh, rh) + 1

  def get_height(self, x: node):
    if x == None:
      return -1
    return x.height

  def get_balance(self, x: node):
    return self.get_height(x.left) - self.get_height(x.right)

  def balance(self, target: node):
    if target == None:
      return

    target.height = self.calc_height(target)
    bal = self.get_balance(target)
    a = target

    if bal < -1:
      b = a.right
      if self.get_balance(b) == 1:
        self.right_rotate(b)
        self.left_rotate(a)
      elif self.get_balance(b) == -1:
        self.left_rotate(a)

    elif bal > 1:
      b = a.left
      if self.get_balance(b) == 1:
        self.right_rotate(a)
      elif self.get_balance(b) == -1:
        self.left_rotate(b)
        self.right_rotate(a)

    self.balance(target.parent)

  # left rotation

  def left_rotate(self, target: node):
    a = target
    b = a.right
    p = a.parent

    # could be None
    y = b.left

    a.right = y
    if y != None:
      y.parent = a
    a.height = self.calc_height(a)

    b.left = a
    a.parent = b
    b.parent = p
    if p == None:
      self.root = b
    else:
      if b.key > p.key:
        p.right = b
      else:
        p.left = b
    b.height = self.calc_height(b)

  # right rotation
  def right_rotate(self, target: node):
    a = target
    b = a.left
    p = a.parent
    # could be None
    x = b.right

    a.left = x
    if x != None:
      x.parent = a
    a.height = self.calc_height(a)

    b.right = a
    a.parent = b
    b.parent = p
    if p == None:
      self.root = b
    else:
      if b.key > p.key:
        p.right = b
      else:
        p.left = b

    b.height = self.calc_height(b)

  def replace(self, target: node, replacement: node):
    p = target.parent

    if p == None:
      self.root = replacement
    else:
      if p.right == target:
        p.right = replacement
      else:
        p.left = replacement

    if replacement != None:
      replacement.parent = p

  def delete(self, target: node):
    if target.left == None:
      p = target.parent
      self.replace(target, target.right)
      if p != None:
        p.height = self.calc_height(p)
    elif target.right == None:
      p = target.parent
      self.replace(target, target.left)
      if p != None:
        p.height = self.calc_height(p)
    else:
      replacement = self.min(target.right)
      if replacement != target.right:
        rp = replacement.parent
        self.replace(replacement, replacement.right)

        if replacement.right == None:
          self.balance(rp)
        else:
          self.balance(replacement.right)

        replacement.right = target.right
        replacement.right.parent = replacement

      self.replace(target, replacement)
      replacement.left = target.left
      replacement.left.parent = replacement
      self.balance(replacement)

    self.size -= 1


tree = avl_tree()
for i in range(1, 101):
  tree.insert(i)

print(f'height: {tree.root.height}')

# for i in range(1, 20):
#   k = random.randint(1, 100)
#   target = tree.search(tree.root, k)
#   if target.key == k:
#     tree.delete(target)

for i in range(101):
  tree.delete(tree.root)
walk = []
inorder_tree_walk(tree.root, walk)
if len(walk) == tree.size:
  print('ok')
else:
  print('something is wrong')


""" # inorder_tree_walk(tree.root)
print(
    'possible min height',
    math.floor(math.log2(10**6)),
    'tree height', tree.root.height
) """
