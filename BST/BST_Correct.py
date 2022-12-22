class node:
  def __init__(self, k=0, l=None, r=None, p=None) -> None:
    self.key = k
    self.l = l
    self.r = r
    self.p = p


class T:
  def __init__(self, root_key=0) -> None:
    self.root = node(root_key)

  def tree_search(self, x: node, key: int):
    tmp = x
    p = None

    while tmp != None and tmp.key != key:
      p = tmp
      if key < tmp.key:
        tmp = tmp.l
      else:
        tmp = tmp.r

    if tmp == None:
      return p
    return tmp

  def tree_min(self, x: node):
    tmp = x
    while tmp.l != None:
      tmp = tmp.l

    return tmp

  def tree_max(self, x: node):
    tmp = x
    while tmp.r != None:
      tmp = tmp.r

    return tmp

  def tree_successor(self, x: node):
    tmp = x
    if tmp.r != None:
      return self.tree_min(tmp.r)

    y = tmp.p

    while y != None and tmp == y.r:
      tmp = y
      y = y.p

    return y

  def tree_insert(self, key: int):
    possible_parent = self.tree_search(self.root, key)
    if possible_parent.key == key:
      return

    new_node = node(key, None, None, possible_parent)

    if possible_parent == None:
      self.root = new_node
    elif new_node.key < possible_parent.key:
      possible_parent.l = new_node
    else:
      possible_parent.r = new_node

  def transplant(self, target: node, replacement: node):
    if target == self.root:
      self.root = replacement
    elif target == target.p.l:
      target.p.l = replacement
    else:
      target.p.r = replacement

    if replacement != None:
      replacement.p = target.p

  def tree_delete(self, target: node):
    if target.l == None:
      self.transplant(target, target.r)
    elif target.r == None:
      self.transplant(target, target.l)
    else:
      replacement = self.tree_min(target.r)
      if replacement.p != target:
        self.transplant(replacement, replacement.r)
        replacement.r = target.r
        replacement.r.p = replacement

      self.transplant(target, replacement)
      replacement.l = target.l
      replacement.l.p = replacement
