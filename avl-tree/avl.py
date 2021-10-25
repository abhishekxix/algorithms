class node:
  def __init__(self, k=0, p=None, l=None, r=None) -> None:
    self.key = k
    self.parent = p
    self.left = l
    self.right = r
    self.height = 0


class avl_tree:
  def __init__(self, root_key=0) -> None:
    self.root = node(root_key)

  def search(self, x: node, key: int):
    p = x.parent
    tmp = x

    while tmp != None and tmp.key != None:
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


tree = avl_tree()
for i in range(10):
  tree.insert(i)
print('done')
