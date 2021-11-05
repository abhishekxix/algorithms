from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(root, cs, ts):
      if not root:
        return False
      if not root.left and not root.right:
        if ts == cs:
          return True

        return False

      return (
          dfs(root.left, (cs + root.left.val) if root.left else cs, ts)
          or
          dfs(root.right, (cs + root.right.val) if root.right else cs, ts)
      )
    if not root:
      return False
    return dfs(root, root.val, targetSum)
