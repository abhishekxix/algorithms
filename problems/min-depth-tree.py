from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


""" 
# DFS solution

class Solution:
  def minDepth(self, root: Optional[TreeNode]) -> int:
    def explore_depth(node):
      if node == None:
        return 0

      depth = 0

      if not node.left and not node.right:
        depth = 1
      elif not node.left:
        depth = explore_depth(node.right) + 1
      elif not node.right:
        depth = explore_depth(node.left) + 1
      else:
        depth = min(explore_depth(node.left),
                    explore_depth(node.right)) + 1

      return depth

    return explore_depth(root)
 """
