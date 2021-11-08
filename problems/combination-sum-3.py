from typing import List


class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    def buildTargetCombination(
        upperBound,
        target,
        result,
        idx=1,
        curr=[],
        currSum=0,
    ):
      if currSum > target:
        return

      if len(curr) > upperBound:
        return

      if currSum == target and len(curr) == upperBound:
        result.append(curr[:])
        return

      if currSum < target and len(curr) >= upperBound:
        return

      for j in range(idx, 10):
        curr.append(j)
        currSum += j
        buildTargetCombination(
            upperBound, target, result, j + 1, curr, currSum
        )
        currSum -= j
        curr.pop()

    result = []
    buildTargetCombination(k, n, result)
    return result


print(Solution().combinationSum3(3, 9))
