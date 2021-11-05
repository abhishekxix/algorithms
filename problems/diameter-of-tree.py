from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def dfs(root):
      if not root:
        return 0, 0

      lh, ld = dfs(root.left)
      rh, rd = dfs(root.right)

      height = max(lh, rh) + 1

      return height, max(lh + rh, ld, rd)

    h, d = dfs(root)

    return d
