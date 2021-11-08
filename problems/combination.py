from typing import List


class Solution:
  def combine(self, n: int, k: int) -> List[List[int]]:
    def buildCombination(n, k, idx, curr, result):
      if len(curr) == k:
        result.append(curr[:])
        return

      for j in range(idx + 1, n + 1):
        curr.append(j)
        buildCombination(n, k, j, curr, result)
        curr.pop()

    result = []
    buildCombination(n, k, 0, [], result)
    return result


print(Solution().combine(4, 2))
