from typing import List


class Solution:
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    def buildPermutations(nums, result, present=set(), curr=[], i=0):
      if i == len(nums):
        result.append(curr[:])
        return

      usedAtCurrentLevel = set()
      j = 0
      while j < len(nums):
        if j not in present and nums[j] not in usedAtCurrentLevel:
          curr.append(nums[j])
          usedAtCurrentLevel.add(nums[j])
          present.add(j)
          buildPermutations(nums, result, present, curr, i + 1)
          curr.pop()
          present.remove(j)
        j += 1

    result = []
    buildPermutations(nums, result)
    return result


print(Solution().permuteUnique([1, 2, 3]))
