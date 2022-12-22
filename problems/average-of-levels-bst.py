from typing import Optional, List
from queue import Queue


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    q = Queue()
    result = []
    q.put(root)

    while not q.empty():
      count = q.qsize()
      sum = 0
      tmp = count
      while tmp:
        curr = q.get()
        sum += curr.val

        if curr.left != None:
          q.put(curr.left)

        if curr.right != None:
          q.put(curr.right)
        tmp -= 1

      result.append(sum / count)

    return result


sol = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.averageOfLevels(root))
