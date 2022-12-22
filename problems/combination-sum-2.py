from typing import List


class Solution:
  def combinationSum2(
      self, candidates: List[int], target: int
  ) -> List[List[int]]:
    def buildTargetCombinations(candidates, curr, currSum, target, idx, result):
      if currSum > target:
        return
      if currSum == target:
        result.append(curr[:])
        return

      usedOnThisLevel = set()

      for j in range(idx, len(candidates)):
        if candidates[j] not in usedOnThisLevel:
          curr.append(candidates[j])
          currSum += candidates[j]
          buildTargetCombinations(candidates, curr, currSum, target, j, result)
          tmp = curr.pop()
          currSum -= tmp

    result = []
    candidates.sort()
    buildTargetCombinations(candidates, [], 0, target, 0, result)

    return result
