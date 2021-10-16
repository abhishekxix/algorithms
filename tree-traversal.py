class Node:
  def __init__(self, val: int, parent=None, left=None, right=None) -> None:
    self.val = val
    self.parent = parent
    self.left = left
    self.right = right


class BST:
  def __init__(self) -> None:
    self.root = Node(6)

  @staticmethod
  def inorder(root):
    if root == None:
      return

    BST.inorder(root.left)
    print(root.val)
    BST.inorder(root.right)

  @staticmethod
  def bfs(root):
    if root == None:
      return

    q = [root]

    while len(q) != 0:
      temp = q.pop(0)

      if temp.left != None:
        q.append(temp.left)

      if temp.right != None:
        q.append(temp.right)

      print(temp.val)
