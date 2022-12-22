from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    walkp = []
    walkq = []

    def dfs(root, walk):

      if not root:
        walk.append(root)
        return

      walk.append(root.val)
      dfs(root.left, walk)
      dfs(root.right, walk)

    dfs(p, walkp)
    dfs(q, walkq)

    if len(walkp) != len(walkq):
      return False

    for i in range(len(walkp)):
      if walkp[i] != walkq[i]:
        return False

    return True


p = TreeNode(1, TreeNode(1))
q = TreeNode(1, None, TreeNode(1))

sol = Solution()
sol.isSameTree(p, q)
