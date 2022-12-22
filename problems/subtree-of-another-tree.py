from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    stack = []
    curr = root
    potentialSubtrees = []
    while curr or len(stack):
      while curr:
        stack.append(curr)
        curr = curr.left

      curr = stack.pop()
      if curr.val == subRoot.val:
        potentialSubtrees.append(curr)

      curr = curr.right

    def dfs(a, b):
      if not a and not b:
        return True

      if not a or not b:
        return False

      if a.val != b.val:
        return False

      return (
          dfs(a.left, b.left)
          and
          dfs(a.right, b.right)
      )

    for subTree in potentialSubtrees:
      if dfs(subTree, subRoot):
        return True

    return False
