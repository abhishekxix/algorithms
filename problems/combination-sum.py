from typing import List


class Solution:
  def combinationSum(
      self, candidates: List[int], target: int
  ) -> List[List[int]]:
    def buildTargetCombinations(candidates, curr, currSum, target, idx, result):
      if currSum > target:
        return
      if currSum == target:
        result.append(curr[:])
        return

      for j in range(idx, len(candidates)):
        curr.append(candidates[j])
        currSum += candidates[j]
        buildTargetCombinations(candidates, curr, currSum, target, j, result)
        tmp = curr.pop()
        currSum -= tmp

    result = []
    buildTargetCombinations(candidates, [], 0, target, 0, result)

    return result
